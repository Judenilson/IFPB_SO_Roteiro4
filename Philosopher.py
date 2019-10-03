# Jantar dos Filósofos Descrito no Livro Sistemas Operacionais Modernos - Tenenbaum Pág.115 A vida de um filósofo consiste em alternar 
# períodos de alimentação e pensamento. (Trata-se de um tipo de abstração, mesmo para filósofos, mas as outras atividades são 
# irrelevantes aqui.) Quando um filósofo fica suficientemente faminto, ele tenta pegar seus garfos à esquerda e à direita, um de 
# cada vez, não importa a ordem. Se for bem sucedido em pegar dois garfos, ele come por um tempo, então larga os garfos e continua 
# a pensar. A ques- tão fundamental é: você consegue escrever um programa para cada filósofo que faça o que deve fazer e jamais 
# fique travado?

state = []


# s = []

class Philosopher:
    def __init__(self, n, i):
        self.N = n
        self.i = i
        self.LEFT = (i + self.N - 1) % self.N
        self.RIGHT = (i + 1) % self.N
        self.THINKING = 0
        self.HUNGRY = 1
        self.EATING = 2

        while 1:
            self.think(self.i)
            self.take_first(self.i)
            self.eat(self.i)
            self.put_forks(self.i)

    def think(self, i):
        print("Pensador " + str(i) + " oo´°°°")

    def eat(self, i):
        print("Pensador " + str(i) + " o_o")

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
