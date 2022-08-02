# to start you should use command 'python3 PortScanner/main.py {xxx.xxx.xxx.xxx} {last port}'
# or 'python3 PortScanner/main.py {hostname} {last port}'

import pyfiglet
import sys
import socket
from datetime import datetime

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

if len(sys.argv) >= 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    target = '192.168.0.100'
    print("Invalid argument you must enter the IP like xxx.xxx.xxx.xxx as second parameter")

try:
    ports_number = sys.argv[2]
    if ports_number > 65535 or ports_number < 0:
        print('port must be 0-65535.')
except:
    ports_number = 65535

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
    for port in range(0, ports_number + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Program finished !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\n Server not responding !!!!")
    sys.exit()
