import socket
import time
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
# We use headers to inform client about the size of data etc
HEADER_SIZE = 10

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    d = {
    1: 'Hey',
    2: 'Hello',
    3: 'There'
    }

# Save python object using pickle. Any python object can use saved, and then we can
# send it over using sockets!
    msg = pickle.dumps(d)
    msg = bytes(f'{len(msg):<{HEADER_SIZE}}', 'utf-8') + msg
    clientsocket.send(msg)

'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADER_SIZE}}' + msg
    clientsocket.send(bytes(msg, "utf-8"))
    # clientsocket.close()

    while True:
        time.sleep(3)
        msg = f"The time is : {time.time()}"
        msg = f'{len(msg):<{HEADER_SIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
'''