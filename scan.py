#!/bin/python

import socket
import sys
from datetime import datetime


if len(sys.argv) == 2:
     theip = socket.gethostbyname(sys.argv[1])
else :
     print('invalid or you have forgot to enter the hostname')
     print ('please enter file_name host_name')


print('-' * 50)
print(' scanning the device '+theip)
print('time started \n' +str(datetime.now()))
print('-' * 50)   

try:
     for port in range(50,85):
         s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         socket.setdefaulttimeout(1)
         result = s.connect_ex((theip,port))
        # print('we re currently checking port {}'.format(port))
         if result==0 :
           print ('port {} is open'.format(port))
         else:
           print('port number {} is not open oups'.format(port))
        
 
         s.close()
         
         
     
except KeyboardInterrupt:
       print('\n exiting the program \n oups bye !')
       sys.exit()
except socket.giaerror:
       print('hostname doesnt exist or couldnt be detected')
       sys.exit()
except socket.error:
       print('we cant reach the server')
       sys.exit()
       