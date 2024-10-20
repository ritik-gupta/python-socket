import socket
import pickle

HEADER_SIZE = 10 # Similar headersize as server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    # Basic functionality to get full message, using a small buffer size.
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(HEADER_SIZE)
        if new_msg:
            print(f"New Message Length: {msg[:HEADER_SIZE]}") 
            msglen = int(msg[:HEADER_SIZE])
            new_msg = False
            
        full_msg += msg

        if len(full_msg)-HEADER_SIZE == msglen:
            print("Full Message Received")
            # (full_msg[HEADER_SIZE:])
            print(pickle.loads(full_msg[HEADER_SIZE:]))
            new_msg = True
            full_msg = b''
