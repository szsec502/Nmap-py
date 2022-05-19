import nmap


class NewScanner(object):
    def __init__(self):
        self.nmap = nmap.PortScanner()

    def os_detection(self, target, args="-O"):
        results = self.nmap.scan(hosts=target, arguments=args)
        print(results)

    def services_detection(self, target, args="-sV"):
        results = self.nmap.scan(hosts=target, arguments=args)
        if results["scan"]:
            print(results)


if __name__ == "__main__":
    scanner = NewScanner()
    scanner.os_detection("14.215.177.39")
    scanner.services_detection("14.215.177.39")
