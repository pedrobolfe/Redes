import socket
# transforma a mensagem do cliente em maiuscula
port = 10500

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(('0.0.0.0', port))

server.listen()


print(f'=3D=3D=3D Server aguardando conexoes na porta {port} =3D=3D=3D=')
conn, addr = server.accept()
print(f'conex=C3=A3o recebida de {addr}')

# while True:

#recebe os dados eviados do cliente
data = conn.recv(4096)

fraseC = data.decode()

print(f'Cliente: {data.decode()}')

fraseCM = fraseC.upper()

# print(fraseCM)

conn.send(fraseCM.encode())



#encerra a conexao
conn.close()
