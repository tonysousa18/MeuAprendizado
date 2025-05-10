# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None


    @property
    def motor(self):
        return self._motor
    

    @property
    def fabricante(self):
        return self._fabricante
    

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante



class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome



motor1 = Motor('V8')
fabricante1 = Fabricante('Sony')

carro1 = Carro('Carrao')
carro1.motor = Motor('v8')
carro1.fabricante = fabricante1

print(carro1.nome, '\n', carro1.motor.nome, '\n', carro1.fabricante.nome)