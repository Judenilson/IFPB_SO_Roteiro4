from threading import Thread, Lock, Event
import time
import random

mutex = Lock()


class BarberShop:
    waitingCustomers = []

    # construtor, que recebe por parâmetro o barbeiro e a quantidade de cadeira para os clientes aguardarem
    def __init__(self, barber, number_of_seats):
        self.barber = barber
        self.numberOfSeats = number_of_seats

    # inicia a barbearia
    def open_shop(self):
        print('Barbearia Aberta!')
        working_thread = Thread(target=self.barber_go_to_work)
        working_thread.start()  # inicia a thread do barbeiro

    def barber_go_to_work(self):
        while True:
            mutex.acquire()  # realiza o bloqueio

            if len(self.waitingCustomers) > 0:      # verifica se há clientes esperando
                c = self.waitingCustomers[0]
                del self.waitingCustomers[0]
                mutex.release()
                self.barber.cut_hair(c)
            else:
                mutex.release()
                print('Tudo pronto, indo dormir')
                barber.sleep()  # caso nao haja cliente, barbeiro volta a dormir
                print('Barbeiro Acordado')

    # cliente entra na barbearia
    def enter_barber_shop(self, customer):
        mutex.acquire()     # realiza o bloqueio
        print('>> {0} entrou na barbearia e está procurando um lugar'.format(customer.name))

        if len(self.waitingCustomers) == self.numberOfSeats:    # verifica se há cadeiras vagas para aguardar
            print('Sala de espera cheia!, {0} indo embora.'.format(customer.name))
            mutex.release()
        else:
            print('{0} sentou-se na sala de espera'.format(customer.name))
            self.waitingCustomers.append(c)     # se tiver cadeiras para sentar, entra pra lista de espera
            mutex.release()                     # desbloqueia
            barber.wake_up()                    # acorda o barbeiro


class Customer:
    def __init__(self, name):
        self.name = name


class Barber:
    barberWorkingEvent = Event()

    def sleep(self):
        self.barberWorkingEvent.wait()

    def wake_up(self):
        self.barberWorkingEvent.set()

    def cut_hair(self, customer):
        # Define o barbeiro como ocupado
        self.barberWorkingEvent.clear()

        print('{0} está cortando o cabelo'.format(customer.name))
        time.sleep(random.randrange(3, 16))             # tempo do corte do cabelo

        print('{0} pronto!'.format(customer.name))


if __name__ == '__main__':

    customers = list([])
    customers.append(Customer('José'))
    customers.append(Customer('Maria'))
    customers.append(Customer('Biu'))
    customers.append(Customer('Zezim'))
    customers.append(Customer('Chico'))
    customers.append(Customer('Zefinha'))
    customers.append(Customer('Chica'))
    customers.append(Customer('Carlos'))
    customers.append(Customer('Beth'))

    barber = Barber()

    barberShop = BarberShop(barber, 3)
    barberShop.open_shop()

    while len(customers) > 0:
        c = customers.pop()
        barberShop.enter_barber_shop(c)
        time.sleep(random.randrange(5, 16))     # tempo de chegada dos clientes
