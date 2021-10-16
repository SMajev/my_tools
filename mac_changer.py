import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option('-i', '--interface', dest='interface',
                 help='Interface to change its MAC address.')

parser.add_option('-m', '--mac', dest='MAC',
                 help='New MAC address example (00:11:22:33:44:66): ')

(options, arguments) = parser.parse_args()

interface = options.interface
MAC = options.MAC

print(f'[*] Changing MAC address for {interface} to {MAC}')

subprocess.call(['sudo', "ifconfig", interface, 'down'])
subprocess.call(['sudo', "ifconfig", interface, 'hw', 'ether', MAC])
subprocess.call(['sudo', "ifconfig", interface, 'up'])
