import nmap


nm = nmap.PortScanner()

res = nm.scan(hosts="192.168.10.1", arguments="-O -sV -T4")

print(res)
