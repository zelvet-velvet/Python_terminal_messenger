# socket estimating and sending data
import socket
import pickle
import struct
import imutils
import threading
import base6
import sys

# handling local ip and 
try:
	local_ip = sys.argv[1]
	if local_ip == "--help":
		print("usage: python3 UDP_C.py [local_IP_addr]")
		exit()
except:
	print("error : missing local IP parameter")
	print("usage: python3 webcam_openpifpaf.py [local_IP_addr]")
	exit()

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print('HOST IP:', local_ip)
port = 60050
socket_address = (local, port)
server_socket.bind(socket_address)
print('Server bind completed')
indata, Client_addr = server_socket.recvfrom(1024)


def :




