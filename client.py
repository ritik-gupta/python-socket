import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# Basic functionality to get full message, using a small buffer size.
full_msg = ''
while True:
    msg = s.recv(1) # Very small buffer size
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
