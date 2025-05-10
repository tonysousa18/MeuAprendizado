from abc import ABC, abstractmethod


class Trabalhador(ABC): #Interface
    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def consultar_beneficios(self) -> None:
        pass
    

class TrabalhadorTemporario(ABC): #Interface segregada
    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass




class  Professor(Trabalhador):
    def trabalhar(self):
        print('O Professor está trabalhando...')

    def ir_para_casa(self):
        print('O Professor está indo para casa...')
    
    def consultar_beneficios(self):
        print('Consultando beneficios')

class  ProfessorSubstituto(TrabalhadorTemporario):
    def trabalhar(self):
        print('O Professor Substituto está trabalhando...')

    def ir_para_casa(self):
        print('O Professor Substituto está indo para casa...')


p1 = Professor()
p2 = ProfessorSubstituto()

p1.consultar_beneficios()
p2.ir_para_casa()