from socket import *
from termcolor import colored as col
from datetime import datetime

"""
Listens on specified port for an incoming connection, when received the sent data is logged locally.
This script is the first part of a two part program, log_client being the second.
Listening port is hardcoded in to match the client.
Uncomment line 37 for user defined port but also change the client port.
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

                print(f"{col('[*]', 'yellow')} Server shutting down")

def main():
    port = 5432
    # port = input("[*] Enter port number to listen on: ")
    server = Server(port)
    server.start()

if __name__ == '__main__':
    main()
