from abc import ABC, abstractmethod

class Pessoa(ABC):
    def andar(self):
        print('andando')

    @abstractmethod
    def trabaiar(self):
        print('trabalhando')



class Professor(Pessoa):
    def trabaiar(self):
        print('O fessor esta professando')

class Cozinheiro(Pessoa):
    def trabaiar(self):
        print('O cozinheiro esta cozinando')



p1 =  Professor()
p1.trabaiar()
p2 = Cozinheiro()
p2.trabaiar()