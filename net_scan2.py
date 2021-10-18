import scapy.all as scapy

IP = '192.168.0.5'

def scan(ip):
    arp_request = scapy.ARP()
    arp_request.pdst = ip
    print(arp_request.summary())
    # scapy.ls(scapy.ARP())

if __name__ == '__main__':    
    scan(IP)