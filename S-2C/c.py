import os
import socket , threading
import time
HOST="140.134.174.3"
PORT = 60000


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def cls():
    	os.system('clear')
            
def listen():
	global sent
	while True:
		data = b""
		while not data:
			data = s.recv(1024)
			print("\b\b\b\b\b\b\b\b\b\b\b\b\b:", data.decode(), "\n> ", end = "")
			time.sleep(0.5)

def get_input():
	global sent
	while True:
		data = b""
		while not data:
			data = input('\033[1A> ').encode()
			print('\033[1A'+"> "+ '\033[K')
		if(data.decode()=="cls"):
			cls()
		else:
			sent = data
		time.sleep(0.5)



while True:

	cls()

	s.connect((HOST, PORT))
	sent = b""

	listen_thread = threading.Thread(target = listen)
	input_thread = threading.Thread(target = get_input)

	listen_thread.start()
	input_thread.start()
	while True:
		if sent:
			s.sendall(sent)
			sent = b""
		time.sleep(0.5)
s.close()
