import socket

IP = 'www.google.com'
PORT = 80
ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

client.send(b'GET / HTTP/1.1\r\n\r\n')

response = client.recv(4096)

print(response)
