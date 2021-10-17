import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--interface', dest='interface',
                    help='Interface to change its MAC address.')

    parser.add_option('-m', '--mac', dest='MAC',
                    help='New MAC address example (00:11:22:33:44:66): ')

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify interface')
    elif not options.MAC:
        parser.error('[-] Please specify MAC')
    return options
    

def change_mac(interface, MAC):
    print(f'[*] Changing MAC address for {interface} to {MAC}')
    subprocess.call(['sudo', "ifconfig", interface, 'down'])
    subprocess.call(['sudo', "ifconfig", interface, 'hw', 'ether', MAC])
    subprocess.call(['sudo', "ifconfig", interface, 'up'])

def get_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface]).decode('utf-8')
    mac_address_search = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if mac_address_search:
        print(ifconfig_result)
        return f'Current MAC: {mac_address_search.group(0)}'
    else:
        return '[-] Could not read MAC address.'

def main():
    options = get_args()
    change_mac(options.interface, options.MAC)
    print(get_mac(options.interface))

if __name__ == '__main__': main()


