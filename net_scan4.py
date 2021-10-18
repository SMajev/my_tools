import scapy.all as scapy

IP = '192.168.0.5/24'

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_lst = scapy.srp(arp_request_broadcast, timeout=1)[0]
    
    for element in answered_lst:
        print(element[1].show())
        print('--------------------------------------------------------------------------------------------------')


if __name__ == '__main__': scan(IP)