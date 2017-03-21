#!/usr/bin/python

import sys
import socket

helptext = "grabanner.py <IP> <Port>"

def GetBanner(ip_address,port):
  try:
    s = socket.socket()
    s.connect((ip_address,port))
    banner = s.recv(1024)
    print(banner)
  except socket.error:
    print "Connection Error"

def main():
  try:
    ip_address = sys.argv[1]
  except Exception as e:
    print(helptext)
    return
  try:
    port = int(sys.argv[2])
  except:
    print(helptext)
    return
  GetBanner(ip_address,port)
  
if __name__ == '__main__':
  main()
