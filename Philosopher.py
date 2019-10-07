import threading
state = []
for i in range(5):
    state.append(0)


class Philosopher(threading.Thread):
    def __init__(self, n, i):
        threading.Thread.__init__(self)
        self.N = n
        self.i = i
        self.LEFT = (i + self.N - 1) % self.N
        self.RIGHT = (i + 1) % self.N
        self.THINKING = 1
        self.HUNGRY = 2
        self.EATING = 3

        while True:
            self.think(self.i)
            self.take_first(self.i)
            self.eat(self.i)
            self.put_forks(self.i)

    def think(self, i):
        print("Pensador " + str(i) + " Pensando")

    def eat(self, i):
        print("Pensador " + str(i) + " Comendo")

    def take_first(self, i):
        # entra na regiao critica
        state[i] = self.HUNGRY
        self.test(i)
        # sai da regiao critica
        # bloqueia se não pegou garfo

    def put_forks(self, i):
        # entra na regiao critica
        state[i] = self.THINKING
        self.test(self.LEFT)
        self.test(self.RIGHT)
        # sai da regiao critica

    def test(self, i):
        if state[i] == self.HUNGRY and state[self.LEFT] != self.EATING and state[self.RIGHT] != self.EATING:
            state[i] = self.EATING
            # sobe semáforo


qtd_filosofos = 5
filosofos = [threading.Lock() for n in range(qtd_filosofos)]

Philosophers = []
for i in range(qtd_filosofos):
    Philosophers.append(Philosopher(qtd_filosofos, filosofos[i]))

for p in Philosophers:
    p.start()
