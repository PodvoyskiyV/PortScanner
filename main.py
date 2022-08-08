import pyfiglet
import sys
import socket
from datetime import datetime

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

try:
    if len(sys.argv) == 3:
        target = socket.gethostbyname(sys.argv[1])
        ports_number = sys.argv[2]

    else:
        print('Port Scanner will scan all ports from 0 to LAST')
        ports_number = input('[*] Enter Last PORT: ')

        while True:
            try:
                if int(ports_number) > 65535 or int(ports_number) < 0:
                    print('E: Last PORT is incorrect.')
                    ports_number = input('[*] Enter Last PORT from 0 to 65535: ')
                else:
                    break

            except ValueError:
                print('E: Last PORT is incorrect.')
                ports_number = input('[*] Enter Last PORT from 0 to 65535: ')

        target = input('[*] Enter Target IP like xxx.xxx.xxx.xxx: ')

    flag = True
    while flag:
        target = (target.split(sep='.'))

        if len(target) != 4:
            print('E: Target IP is incorrect.')
            target = input('[*] Enter Target IP like xxx.xxx.xxx.xxx where xxx is from 0 to 255: ')
        else:
            for quater in target:
                try:
                    quater = int(quater)
                except ValueError:
                    print('E: Target IP is incorrect.')
                    target = input('[*] Enter Target IP like xxx.xxx.xxx.xxx where xxx is from 0 to 255: ')
                    break

                if quater < 0 or quater > 255:
                    print('E: Target IP is incorrect.')
                    target = input('[*] Enter Target IP like xxx.xxx.xxx.xxx where xxx is from 0 to 255: ')
                    break
            else:
                flag = False
                target = '.'.join(target)

    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    for port in range(0, int(ports_number) + 1):
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
