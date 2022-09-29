import socket, threading
HOST = "127.0.0.1"
PORT = 12345

def listen(socket):
	while True:
		data = b""
		while not data:
			data = socket.recv(1024)
		sent[socket] = data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	s.bind((HOST, PORT))
	s.listen()

	conn1, addr1 = s.accept()
	print("Connect to", addr1)

	conn2, addr2 = s.accept()
	print("Connect to", addr2)

	conn3, addr3 = s.accept()
	print("Connect to", addr3)

	sent = {conn1:b"",conn2:b"", conn3:b""}

	thread1 = threading.Thread(target = listen, args = (conn1, ))
	thread2 = threading.Thread(target = listen, args = (conn2, ))
	thread3 = threading.Thread(target = listen, args = (conn3, ))		


	thread1.start()
	thread2.start()
	thread3.start()

	while True:
		if sent[conn1]:
			conn2.sendall(sent[conn1])
			conn3.sendall(sent[conn1])
			print(addr1,"sends", sent[conn1].decode())
			sent[conn1] = b""
		if sent[conn2]:
			conn1.sendall(sent[conn2])
			conn3.sendall(sent[conn2])
			print(addr2,"sends", sent[conn2].decode())
			sent[conn2] = b""
		if sent[conn3]:
			conn1.sendall(sent[conn3])
			conn2.sendall(sent[conn3])
			print(addr3,"sends", sent[conn3].decode())
			sent[conn3] = b""
		
		




