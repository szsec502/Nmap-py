package main

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/Ullaakut/nmap/v2"
	"gorm.io/gorm"
)

var (
	db  *gorm.DB
	err error
)

type OSFingerprint struct {
	gorm.Model
	IP           string
	Name         string
	Accuracy     int
	Vendor       string
	OSGeneration string
	Type         string
	Family       string
}

type OSServices struct {
	gorm.Model
	IP         string
	Port       uint16
	Protocol   string
	State      string
	Reason     string
	DeviceType string
	ExtraInfo  string
	Hostname   string
	Name       string
	OSType     string
	Product    string
	ServiceFP  string
	Version    string
}

/*
func InitDB() {
	dsn := "root:password@tcp(127.0.0.1:3306)/finger_db?charset=utf8&parseTime=True&loc=Local"
	db, err = gorm.Open(mysql.New(mysql.Config{
		DSN:                       dsn,
		DisableDatetimePrecision:  true,
		SkipInitializeWithVersion: false,
	}), &gorm.Config{})

	if err != nil {
		panic("Can't Open the database connection!")
	}

	db.AutoMigrate(&OSFingerprint{}, &OSServices{})

	sqlDB, err := db.DB()
	if err != nil {
		panic("Init database pool failed!")
	}
	sqlDB.SetConnMaxIdleTime(10)
	sqlDB.SetMaxOpenConns(100)
}
*/

func runNmap(target string) ([]OSFingerprint, []OSServices, error) {
	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Minute)
	defer cancel()

	var osFingerprints []OSFingerprint
	var osServices []OSServices

	scanner, err := nmap.NewScanner(
		nmap.WithTargets(target),
		nmap.WithTimingTemplate(nmap.TimingAggressive),
		nmap.WithOSDetection(),
		nmap.WithServiceInfo(),
		nmap.WithPorts("22-9000"),
		nmap.WithContext(ctx),
	)

	if err != nil {
		return nil, nil, err
	}

	result, _, err := scanner.Run()
	if err != nil {
		return nil, nil, err
	}

	for _, host := range result.Hosts {
		var st OSServices
		for _, port := range host.Ports {
			st.Port = port.ID
			st.Protocol = port.Protocol
			st.State = port.State.String()
			st.Reason = port.State.Reason
			st.DeviceType = port.Service.DeviceType
			st.ExtraInfo = port.Service.ExtraInfo
			st.Hostname = port.Service.Hostname
			st.Name = port.Service.Hostname
			st.Version = port.Service.Version
			st.OSType = port.Service.OSType
			st.ServiceFP = port.Service.ServiceFP
			st.IP = host.Addresses[0].Addr
			osServices = append(osServices, st)
		}

		for _, finger := range host.OS.Matches {
			var osfinger OSFingerprint
			osfinger.Name = finger.Name
			osfinger.Accuracy = osfinger.Accuracy
			for _, osf := range finger.Classes {
				osfinger.OSGeneration = osf.OSGeneration
				osfinger.Vendor = osf.Vendor
				osfinger.Type = osf.Type
				osfinger.Family = osf.Family
			}

			osFingerprints = append(osFingerprints, osfinger)
		}
	}

	return osFingerprints, osServices, nil
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage : centrum IP Address")
		return
	}

	osfingers, osServices, err := runNmap(os.Args[1])
	if err != nil {
		fmt.Printf("error : %+v\n", err)
	}

	fmt.Println(osServices)
	fmt.Println(osfingers)
}
