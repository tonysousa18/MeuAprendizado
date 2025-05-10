class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falarNome(self):
        print(self.__class__.__name__)

class Cliente(Pessoa):
    pass

cliente = Cliente('Tony', 'Sousa')

print(cliente.nome)
cliente.falarNome()