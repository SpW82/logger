#!/usr/bin/python

from socket import *
from termcolor import colored as col
from datetime import datetime
import optparse

"""
Listens on specified port for an incoming connection, when received the sent data is logged locally.
This script is the first part of a two part program, logger_client_parser2.py being the second.
Use the -p or --prt flag followed by the desired port number to set a port.
If no port is specified, the server will run on 12345.
The default settings will run locally.
"""

class Server:

    def __init__(self, port):
        self.port = port

    def start(self):
        with socket(AF_INET, SOCK_STREAM) as s:
            print(f"{col('[*]', 'blue')} Server starting ...")
            s.bind(('', self.port))
            s.listen()
            print(f"{col('[*]', 'yellow')} Listening on {self.port}")

            try:

                while True:
                    c, a = s.accept()
                    k = c.recv(1024).decode()
                    with open('logd.txt', 'a') as f:
                        f.write(f"{datetime.now()}: {k}\n")

            except KeyboardInterrupt:

                print(f"\n{col('[*]', 'yellow')} Server shutting down")

def main():
    parser = optparse.OptionParser('A simple server to log received data to a file')
    parser.add_option('-p','--prt', dest='prt', type='int', help='port to listen for connection (12345 is default)')
    (options, args) = parser.parse_args()
    port = 12345

    if options.prt is None:
        pass
    else:
        port = options.prt

    server = Server(port)
    server.start()

if __name__ == '__main__':
    main()
