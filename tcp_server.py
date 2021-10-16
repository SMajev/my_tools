#! /usr/bin/env python3

import socket 
import threading

IP = '127.0.0.1'
PORT = 5050
ADDR = (IP, PORT)


server = socket.server(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

server.listen(5)

print(f'[*] Listening on {IP}:{PORT}')

def handle_client(client_socket):
    request = client_socket.recv(4096)
    print(f'[*] Received {request}')

    client_socket.send(b'Yo!')
    client_socket.close()

while True:
    client, addr = server.accept()
    print(f"[*] Accepted connection  from {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()