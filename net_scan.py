import scapy.all as scapy

IP = '192.168.0.5/24'

def scan(ip):
    scapy.arping(ip)


if __name__ == '__main__':    
    scan(IP)