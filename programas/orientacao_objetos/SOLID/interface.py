from abc import ABC, abstractmethod


class Trabalhador(ABC): #Interface
    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def horario_de_almosso(self) -> None:
        pass

class  Professor(Trabalhador):
    def trabalhar(self):
        print('O Professor está trabalhando...')

    def ir_para_casa(self):
        print('O Professor está indo para casa...')
    
    def horario_de_almosso(self):
        print('O Professor esta almossando...')

class  Engenheiro(Trabalhador):
    def trabalhar(self):
        print('O Engenheiro está trabalhando...')

    def ir_para_casa(self):
        print('O Engenheiro está indo para casa...')
    
    def horario_de_almosso(self):
        print('O Engenheiro esta almossando...')


def comunicar_trabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print('\nComunicar o trabalhador para ir almossar')
    trabalhador.horario_de_almosso()
    print('\nComunicar o trabalhador para ir pra casa')
    trabalhador.ir_para_casa()

p1 = Professor()
p2 = Engenheiro()
comunicar_trabalhador(p1)
comunicar_trabalhador(p2)