import socket

port = 10502

dest = '192.168.246.250'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'=== conectando ao servidor {dest}:{port}')
client.connect((dest, port))

while True:
    msg = '''
    Traceback (most recent call last):
    File "/home/aluno/Redes/server_threads/server.py", line 58, in <module>
        main()
    File "/home/aluno/Redes/server_threads/server.py", line 49, in main
        conn, addr = server.accept() # espera conexoes
    File "/usr/lib/python3.10/socket.py", line 293, in accept
    fd, addr = self._accept()
        KeyboardInterrupt
    Exception ignored in: <module 'threading' from '/usr/lib/python3.10/threading.py'>
    Traceback (most recent call last):
        File "/usr/lib/python3.10/threading.py", line 1567, in _shutdown
        lock.acquire()
    KeyboardInterrupt: 
    '''# envia uma msg

    client.send(msg.encode())

    #recebe os dados eviados do cliente
    data = client.recv(4096)
    print(f'servidor: {data.decode()}')


client.close()
