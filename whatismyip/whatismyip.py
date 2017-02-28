#!/usr/bin/python

import requests
import sys


try:
  getserver = sys.argv[1]
except:
  getserver = 0

ipservers = [ 'http://ifconfig.co/ip', 'http://icanhazip.com']

def getmyip(ipservers,getserver):
  
  srvno = 0

  if getserver == 'all':
    for server in ipservers:
      r = requests.get(server)
      print("IP Supplied by : " + server)
      print("Your IP is : " + r.text)
      print("[+]" + "-"*30)

  if getserver == 'list':
    for server in ipservers:
      print(str(srvno) + ") " + server)
      srvno += 1

  if getserver != 'all' and getserver != 'list':
    r = requests.get(ipservers[int(getserver)])
    print("IP Supplied by : " + ipservers[int(getserver)])
    print("Your IP is : " + r.text)


getmyip(ipservers, getserver)
