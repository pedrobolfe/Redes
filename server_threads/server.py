from threading import Thread
from time import sleep

class Contador(Thread):
    def __init__(self, n, segundos, nome ):
        Thread.__init__(self)
        self.n = n
        self.segundos = segundos
        self.nome = nome
        
    def run(self):
        for i in range(self.n):
            print(i+1)
            sleep(self.segundos)
        print(f'Thread {self.nome} finalizada')

def main():
    Contador(5, 2, "cleitin").start()
    Contador(10, 2, "Siuu").start()
    Contador(15, 1, "Magaiver").start()

if __name__ == "__main__":
    main()
    
# print("Esperando threads terminarem")
# sleep(15)
# print("Fim")