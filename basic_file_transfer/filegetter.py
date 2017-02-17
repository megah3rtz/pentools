#!/usr/bin/python

import sys
import socket

destfile = sys.argv[1]
listenport = int(sys.argv[2])

print('Listening on Port:' + str(listenport))

def listenforfile(destfile,listenport):
  try:
    ofile = open(destfile, 'w')
    s=socket.socket()
    host = socket.gethostname()
    s.bind((host,listenport))
    s.listen(5)
    while True:
      c, addr = s.accept()
      print('Got connection!')
      sentfile = c.recv(64)
      print(sentfile)
      if sentfile.strip() == 'Finished':
        print("Got Finished")
    	s.close()
        sys.exit("Recieved finished message")
      elif sentfile:
        ofile.write(sentfile)
  except Exception as e:
    print('Failed :(')
    print(e)


if __name__ == '__main__':
  listenforfile(destfile,listenport)


