import threading
import time
import random

mutex = threading.Semaphore(1)  # Criando um semáforo


class Philosopher(threading.Thread):
    def __init__(self, n, i):
        threading.Thread.__init__(self)
        self.N = n
        self.i = i
        self.LEFT = (i + self.N - 1) % self.N
        self.RIGHT = (i + 1) % self.N
        self.THINKING = 0
        self.HUNGRY = 1
        self.EATING = 2

        while True:
            self.think(self.i)                  # Pensando
            time.sleep(random.randint(0, 2))
            self.take_forks(self.i)             # Pegando os garfos
            self.put_forks(self.i)              # Liberando os garfos

    def think(self, i):
        print("Filósofo " + str(i) + " Pensando")

    def take_forks(self, i):
        print("Filósofo " + str(i) + " Quer Comer")
        mutex.acquire()             # entra na regiao critica
        state[i] = self.HUNGRY
        self.eat(i)
        mutex.release()             # sai da regiao critica

    def put_forks(self, i):
        mutex.acquire()             # entra na regiao critica
        state[i] = self.THINKING
        self.eat(self.LEFT)
        self.eat(self.RIGHT)
        print("Filósofo " + str(i) + " Liberou os Garfos")
        mutex.release()             # sai da regiao critica

    def eat(self, i):
        if state[i] == self.HUNGRY:
            if state[self.LEFT] != self.EATING:
                if state[self.RIGHT] != self.EATING:
                    state[i] = self.EATING
                    time.sleep(random.randint(0,2))
                    print("Filósofo " + str(i) + " Comendo")


if __name__ == '__main__':

    qtd_filosofos = 5
    state = []  # Lista para guardar o estado de cada filósofo

    for i in range(qtd_filosofos):
        state.append(0)

    Philosophers = []
    for i in range(qtd_filosofos):
        Philosophers.append(threading.Thread(target=Philosopher, args=(qtd_filosofos, i))) #Criando as threads

    for p in Philosophers:
        p.start()           # Iniciando as Threads
