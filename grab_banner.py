#!/usr/bin/python

import sys
#import os
import socket


def getbanner(ip_address,port):
  try:
    s = socket.socket()
    s.connect((ip_address,port))
    banner = s.recv(1024)
    print banner
  except socket.error:
    print "Connection Error"

def main():

  ip_address = sys.argv[1]
  port = int(sys.argv[2])
  getbanner(ip_address,port)

main()
