from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from random import randint


port = 8084
address = '0.0.0.0'
sessions= {}
SESSION_ID_LEN = 10

class SessionHendler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.cookie = None
        try:
            response = 200
            cookies = self.parse_cookies(self.headers["Cookie"])

            if cookies:
                if 'session_id' in cookies:
                    sid = cookies['session_id']
                    sessions[sid] += 1
                    content = f'''
                    <html>
                        <body>
                            <h1>Esta e a sua visita de numero {sessions[sid]}.</h1>
                            <img src="data:image/jpeg;base64,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"></img>
                        </body>
                    </html>
                    '''
            else:
                content = '''
                    <html>
                        <body>
                            <h1>Esta e sua primeira visita.</h1>
                            <img src="data:image/jpeg;base64,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"></img>
                        </body>
                    </html>
                    '''
                sid = self.generate_sid()
                sessions[sid] = 1
                self.cookie = f'session_id={sid}'

        except:

            response = 404
            content = '''
                    <html>
                        <body>
                            <h1>Erro ao processar a pagina, tente novamente</h1>
                        </body>
                    </html>
                    '''
            sid = self.generate_sid()
            sessions[sid] = 1
            self.cookie = f'session_id={sid}'

        self.send_response(response)
        self.send_header('Content-type', 'text/html')

        if self.cookie:
            self.send_header('Set-Cookie', self.cookie)

        self.end_headers()

        self.wfile.write(bytes(content, 'utf-8'))
        return

    def generate_sid(self):
        return "".join(str(randint(0,9)) for _ in range(SESSION_ID_LEN) )
    
    def parse_cookies(self, cookie_list):
        return dict(((c.split("=")) for c in cookie_list.split(";"))) if cookie_list else {}


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def main():
    try:
        server = ThreadedHTTPServer((address, port), SessionHendler)
        server.serve_forever()
    except KeyboardInterrupt: 
        print('Exiting server')
        server.socket.close()

if __name__ == "__main__":
    main()