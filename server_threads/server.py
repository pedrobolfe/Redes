from threading import Thread
from time import sleep
import socket

port = 10500
address = 'localhost'

acessos = 0

def handle_http_request(request):
    # print(request)
    pass

def handle_http_response():
    # response = input(": ")
    response = f'''
    HTTP/1.0 200 OK
    Date: Tue, 14 Mar 2023 15:11:00 GMT-3
    Server: Redes/1.0
    Content-Type: text/HTML

    <html>
        <head>
            <title>
                Aula
            </title>
        </head>
        <body>
            <h1>Aula de Redes de Computadores</h1>
            <h2>IFPR Cascavel</h2>
            Este servidor foi acessado {acessos} vezes.<br>
        </body>
    </html>
    '''
    return response

class Contador(Thread):
    def __init__(self, n, segundos, nome ):
        Thread.__init__(self)
        self.n = n
        self.segundos = segundos
        self.nome = nome
        
    def run(self):
        for i in range(self.n):
            sleep(self.segundos)
            print(f'Thread {self.nome}: {i+1}')


class ThreadServer(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        #recebe os dados eviados do cliente
        data = self.conn.recv(4096)
        msg_recv = data.decode()

        handle_http_request(msg_recv)

        # envia os dados para o cliente
        msg_env = handle_http_response()
        self.conn.send(msg_env.encode())

def main():
    global acessos

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((address, port)) 
    server.listen()

    while True:
        print('== Servidor aguardando conexoes ==')
        acessos +=1
        conn, addr = server.accept() # espera conexoes
        ThreadServer(conn, addr).start() 

    # Contador(5, 2, "cleitin").start()
    # Contador(10, 2, "Siuu").start()
    # Contador(15, 1, "Magaiver").start()

if __name__ == "__main__":
    main()