import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option('-i', '--interface', dest='interface',
                 help='Interface to change its MAC address.')

parser.add_option('-m', '--mac', dest='MAC',
                 help='New MAC address example (00:11:22:33:44:66): ')


parser.parse_args()

interface = input('Interface: ')
MAC = input('MAC address example(00:11:22:33:44:66): ')

print(f'[*] Changing MAC address for {interface} to {MAC}')

subprocess.call(['sudo', "ifconfig", interface, 'down'])
subprocess.call(['sudo', "ifconfig", interface, 'hw', 'ether', MAC])
subprocess.call(['sudo', "ifconfig", interface, 'up'])
