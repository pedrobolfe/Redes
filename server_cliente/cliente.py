import socket

port = 10501

dest = '192.168.246.50'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'=== conectando ao servidor {dest}:{port}')
client.connect((dest, port))

while True:

    msg = input(': ')

    client.send(msg.encode())

    #recebe os dados eviados do cliente
    data = client.recv(4096)
    print(f'servidor: {data.decode()}')


client.close()
