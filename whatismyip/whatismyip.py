#!/usr/bin/python

import requests
import sys


try:
  getserver = sys.argv[1]
except:
  getserver = 0

ipservers = [ 'http://ifconfig.co/ip', 'http://icanhazip.com', 'http://ifconfig.me/ip']

def getmyip(ipservers,getserver):
  
  srvno = 0

  if getserver == 'all':
    for server in ipservers:
      try:
        r = requests.get(server)
        print("IP Supplied by : " + server)
        print("Your IP is : " + r.text)
        print("[+]" + "-"*30)
      except:
        print("Server Unreachable")
        next

  if getserver == 'list':
    for server in ipservers:
      print(str(srvno) + ") " + server)
      srvno += 1

  if getserver != 'all' and getserver != 'list':
    try:
      r = requests.get(ipservers[int(getserver)])
      print("IP Supplied by : " + ipservers[int(getserver)])
      print("Your IP is : " + r.text)
    except:
      print("Server Unreachable")


getmyip(ipservers, getserver)
