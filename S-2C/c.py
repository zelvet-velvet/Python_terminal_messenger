import os
import socket , threading
import time
HOST="8.8.8.8"
PORT = 60000


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # set socket sending as IPV4 TCP  

twosides_Record = ""			# string storing bothside conversation record
opposite_Record = ""			# string storing opposite conversation record
record_mode = True			# boolean to decide which record mode are we using

def cls():				# a method to import Linux command clear, call it to clear console
    	os.system('clear')		
            
def listen():
	global twosides_Record		# global for the purpose to change their values
	global opposite_Racord		
	while True:
		data = b""
		while not data:
			data = s.recv(1024)
			if(data):
				data = ":"+data
				twosides_Record = twosides_Record + data + "\n"
				opposite_Racord = opposite_Racorf + data + "\n"
			time.sleep(1)
	

def get_input():
	global twosides_Record
	global opposite_Racord
	global record_mode
	while True:
		data = b""
		data = input()
		match data:
			case "!tr":
				record_mode = True
				cls()
				print(twosides_Record)		
			case "!or":
				record_mode = False
				cls()
				print(opposite_Racord)
			case _:			
				twosides_Record = twosides_Record +"> "+ data
				sent = data.encode()

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
