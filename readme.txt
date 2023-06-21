The same program in two different forms.
log_local is stand-alone and logs all keystrokes to a local file.
log_client works with log_listener to monitor keyboard input and "on press" of a key, the key 'value' is sent to an IP
address on a specified port to a waiting server, that logs the data to a local file.
For more information read the docstrings contained within the scripts.
Bar log_local.py, all scripts contain command line help menus.
Use only on systems that you have permission to.
NOTE: Windows will flag any script that contains the pynput.keyboard Listener method, that's log_client.py and log_local.py so disable security or make a file exception.
