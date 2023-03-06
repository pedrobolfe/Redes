import socket

port = 10506

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(('0.0.0.0', port))

server.listen()


print(f'=3D=3D=3D Server aguardando coenx=C3=B5es na porta {port} =3D=3D=3D=')
conn, addr = server.accept()
print(f'conex=C3=A3o recebida de {addr}')

# while True:

#recebe os dados eviados do cliente
data = conn.recv(4096)

cliente = data.decode().split()


print(f'Cliente: {data.decode()}')


calculo = int(cliente[0]) + int(cliente[2])


print(calculo)

calculostr = str(calculo)

conn.send(calculostr.encode())

#encerra a conexao
conn.close()





