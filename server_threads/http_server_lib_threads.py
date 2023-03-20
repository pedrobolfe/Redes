from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

port = 8084
address = '0.0.0.0'

class Hendler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        content = '''
        <html>
            <head>
                <title>
                    Aula
                </title>
            </head>
            <body>
                <h1>Aula de Redes de Computadores</h1>
                <h2>IFPR Cascavel</h2>
                <input></input>
            </body>
        </html>
        '''
        self.wfile.write(bytes(content, 'utf-8'))
        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def main():
    try:
        server = ThreadedHTTPServer((address, port), Hendler)
        server.serve_forever()
    except KeyboardInterrupt: 
        print('Exiting server')
        server.socket.close()

if __name__ == "__main__":
    main()