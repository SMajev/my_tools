import subprocess

interface = input('Interface: ')
MAC = input('MAC address example(00:11:22:33:44:66): ')

print(f'[*] Changing MAC address for {interface} to {MAC}')

# subprocess.call(f'ifconfig {interface} down', shell=True)
# subprocess.call(f'ifconfig {interface} hw ether {MAC}', shell=True)
# subprocess.call(f'ifconfig {interface} up', shell=True)

subprocess.call(['sudo', "ifconfig", interface, 'down'])
subprocess.call(['sudo', "ifconfig", interface, 'hw', 'ether', MAC])
subprocess.call(['sudo', "ifconfig", interface, 'up'])
