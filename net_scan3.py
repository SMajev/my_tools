import scapy.all as scapy

IP = '192.168.0.5/24'

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    scapy.srp(arp_request_broadcast)


if __name__ == '__main__': scan(IP)