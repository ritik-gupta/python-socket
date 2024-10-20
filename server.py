import socket
import time

# We use headers to inform client about the size of data etc
HEADER_SIZE = 10

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
