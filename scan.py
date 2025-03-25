#!/bin/python

import socket
import sys
from datetime import datetime

# Validate input
if len(sys.argv) != 2:
    print('Invalid input! You must enter the hostname.\nUsage: python scan.py <hostname>')
    sys.exit()


try:
    theip = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print('Hostname doesn’t exist or couldn’t be resolved.')
    sys.exit()


print('-' * 50)
print(f'Scanning the device: {theip}')
print(f'Time started: {datetime.now()}')
print('-' * 50)

# Set timeout once
socket.setdefaulttimeout(1)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((theip, port))

        if result == 0:
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is closed')

        s.close()

except KeyboardInterrupt:
    print('\nExiting the program... Goodbye!')
    sys.exit()
except socket.error:
    print('Network error: Unable to reach the server.')
    sys.exit()
