# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserirEndereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listarEnderecos(self):
        for endereco in self.enderecos:
           print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('Maria')
cliente1.inserirEndereco('Rua Bagé', 289)
cliente1.inserirEndereco('Rua Bagé', 29)
cliente1.listarEnderecos()
