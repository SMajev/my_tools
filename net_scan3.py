import scapy.all as scapy

IP = '192.168.0.5'

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    
    arp_request.show()
    broadcast.show()
    arp_request_broadcast.show()


if __name__ == '__main__': scan(IP)