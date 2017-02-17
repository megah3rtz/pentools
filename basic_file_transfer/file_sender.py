#!/usr/bin/python

import sys
import socket

readfile = sys.argv[1]
destip = sys.argv[2]
destport = sys.argv[3]

print('Sending File:' + readfile)
print('To:' + destip + ':' + destport)

def sendfile(readfile,destip,destport):
  try:
    openfile = open(readfile, 'r')
    s=socket.socket()
    s.connect((destip,int(destport)))
    s.send('Starting')
    s.send(openfile.readlines())
    s.send('Finished')
    s.close
    print('File sent ok')
  except Exception as e:
    print(e)
    print('Failed')

if __name__ == '__main__':
  sendfile(readfile,destip,destport)
    
