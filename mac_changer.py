import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--interface', dest='interface',
                    help='Interface to change its MAC address.')

    parser.add_option('-m', '--mac', dest='MAC',
                    help='New MAC address example (00:11:22:33:44:66): ')

    (options, arguments) = parser.parse_args()

    return options.interface, options.MAC

def change_mac(interface, new_mac):
    print(f'[*] Changing MAC address for {interface} to {MAC}')
    subprocess.call(['sudo', "ifconfig", interface, 'down'])
    subprocess.call(['sudo', "ifconfig", interface, 'hw', 'ether', MAC])
    subprocess.call(['sudo', "ifconfig", interface, 'up'])


INTERFACE, MAC = get_args()

if __name__ == '__main__': change_mac(INTERFACE, MAC)


