import os
import socket , threading
HOST="10.22.48.120"
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
			print("\b\b:", data.decode(), "\n> ", end = "")

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
s.close()
