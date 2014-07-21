#!/usr/bin/env python

import thread
import socket

class ESP:

	def __init__(self):
		tcpsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#tcpsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		tcpsocket.bind(("0.0.0.0",8000))
		tcpsocket.listen(3)

		while True:
			print "waiting for he client"
			(client, (ip,port)) = tcpsocket.accept()

			print "Receiving Data from client IP : ",ip

			data="dummy"
			fp=open("a.txt","a")
			while len(data) :
				data=client.recv(2048)
				print "client sent ",data
				fp.write(data)
				client.send(data)

			print "closing connection"
			client.close()
			fp.close()

ESP()
