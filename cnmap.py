import sys
import nmap
import pymysql
import pymysql.cursors

DB_USER = "your-name"
DB_NAME = "fingers_db"
DB_PASS = "your-password"
DB_HOST = "localhost"
DB_CHAR = "utf8mb4"


class DB(object):
    def __init__(self):
        self.connector = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME, charset=DB_CHAR,
                    cursorclass=pymysql.cursors.DictCursor)

        self.cursors = self.connector.cursor()

    def insert_items(self, items, isa="os"):
        if isa == "os":
            sql = "INSERT INTO osfingers(address,mac,name,accuracy,type,vendor,osfamily,osgen) VALUES(%s, %s, %s, %s,%s, %s, %s, %s)"
        else:
            sql = "INSERT INTO ssfingers(port,state,reason,name,product,version,extrainfo,conf) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

        #print("current sql stament ", sql)
        #print("cuurent items ", items)

        try:
            with self.connector.cursor() as cursor:
                cursor.executemany(sql, items)

                self.connector.commit()
        except Exception as e:
            print(e)
            self.connector.rollback()
        #finally:
        #    self.connector.close()


class NewScanner(object):
    def __init__(self):
        self.nmap = nmap.PortScanner()

    def detection(self, target, args="-O -sV -T4"):
        results = self.nmap.scan(hosts=target, arguments=args)
        osfingers = []
        ssfingers = []
        if results["scan"]:
            if results["scan"][target]["osmatch"]:
                for osmatch in results["scan"][target]["osmatch"]:
                    ositems = {}
                    for os in osmatch["osclass"]:
                        try:
                            ositems["address"] = results["scan"][target]["addresses"]["ipv4"]
                        except KeyError:
                            ositems["address"] = target

                        try:
                            ositems["mac"] = results["scan"][target]["vendor"]["mac"]
                        except KeyError:
                            ositems["mac"] = "Unknow"

                        ositems["name"] = osmatch["name"]
                        ositems["accuracy"] = osmatch["accuracy"]
                        ositems["type"] = os["type"]
                        ositems["vendor"] = os["vendor"]
                        ositems["osfamily"] = os["osfamily"]
                        ositems["osgen"] = os["osgen"]
                        osfingers.append(ositems)

                    for port in self.nmap[target].all_tcp():
                        ssitems = {}
                        ssitems["port"] = port
                        ssitems["state"] = self.nmap[target]["tcp"][port]["state"]
                        ssitems["reason"] = self.nmap[target]["tcp"][port]["reason"]
                        ssitems["name"] = self.nmap[target]["tcp"][port]["name"]
                        ssitems["product"] = self.nmap[target]["tcp"][port]["product"]
                        ssitems["version"] = self.nmap[target]["tcp"][port]["version"]
                        ssitems["extrainfo"] = self.nmap[target]["tcp"][port]["extrainfo"]
                        ssitems["conf"] = self.nmap[target]["tcp"][port]["conf"]
                        ssfingers.append(ssitems)

                    osfingers = [dict(t) for t in set([tuple(d.items()) for d in osfingers])]
                    ssfingers = [dict(t) for t in set([tuple(d.items()) for d in ssfingers])]

            return osfingers, ssfingers

        return [], []


def main(target):
    osf = []
    ssf = []
    scanner = NewScanner()
    db = DB()
    osfingers, ssfingers = scanner.detection(target)

    if len(osfingers) == 0 and len(ssfingers) == 0:
        print("not matches !")
        return

    for item in osfingers:
        osf.append(tuple(item.values()))

    for item in ssfingers:
        ssf.append(tuple(item.values()))

    tosf = tuple(osf)
    tssf = tuple(ssf)
    print("insert data ...")
    db.insert_items(tosf)
    db.insert_items(tssf, "ss")
    print("done !")



if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except KeyboardInterrupt:
        exit(0)
