import scapy.all as scapy

IP = '192.168.0.5/24'

def scan(ip):
    arp_request = scapy.ARP()
    print(arp_request.summary())


if __name__ == '__main__':    
    scan(IP)