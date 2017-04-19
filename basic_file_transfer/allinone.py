#!/usr/bin/python

import sys
import socket

mode = sys.argv[1]

file = sys.argv[2]

ip = sys.argv[3]

port = sys.argv[4]

def CheckInput(mode, file, ip, port):

	if mode == "l":
		StartListner()

	if mode == "s":
		StartSender()


def StartListner():
	print("[+] Starting Listner")

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind to any ip on the host
	s.bind(('', port))
# Queue up to 5 connection requests
	serversocket.listen(5)
	while 1:
def StartSender():
	print("[+] Starting Sender")

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))



CheckInput(mode, file, ip, port)