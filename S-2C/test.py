import socket , threading
import time
def ewe():
	while True:
		input("> ")
		time.sleep(.5)
ok = threading.Thread(target = ewe)
ok.start()
time.sleep(1)
print('\033[1A',end="\r")
print("\nowo")

