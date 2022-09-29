
import os
import socket , threading
HOST="127.0.0.1"
PORT = 12345

import random

def cls():
    	os.system('clear')
            
def listen():
	global sent
	while True:
		data = b""
		while not data:
			data = s.recv(1024)
		print("\b\b\b", data.decode(), "\n > ", end = "")

def get_input():
	global sent
	while True:
		data = b""
		while not data:
			data = input(" >").encode()
		sent = IDcolor.encode()+a+"\033[1;0m".encode()+": ".encode()+data

def listen_userID():
	b = s.recv(1024)
	c = s.recv(1024)
	print("\rOther users are ready.          \nEnter your User ID: ", end = "")
	get_userID.join()
	cls()

def get_userID():
	global	a
	print("Enter your User ID: ", end = "")
	a = input().encode()
	s.sendall(a)
	print("Waiting for other users log in.")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	cls()
	s.connect((HOST, PORT))

	listen_userID = threading.Thread(target = listen_userID)
	get_userID = threading.Thread(target = get_userID)

	listen_userID.start()
	get_userID.start()

	listen_userID.join()
	get_userID.join()
	
	global IDcolor
	x = random.randint(0, 1)
	if x==0:
		IDcolor = "\033[1;"+str(random.randint(31, 36))+"m"
	else:
		IDcolor = "\033[1;"+str(random.randint(41, 46))+"m"

	sent = b""



	listen_thread = threading.Thread(target = listen)
	input_thread = threading.Thread(target = get_input)

	listen_thread.start()
	input_thread.start()

	while True:
		if sent:
			s.sendall(sent)
			sent = b""
