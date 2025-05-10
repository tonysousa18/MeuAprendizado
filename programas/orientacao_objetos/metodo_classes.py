#metodos de classes + factories

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodoDeClasse(cls):
        print('Hey')


    @classmethod
    def criarComCinquentaAnos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criarAnonimo(cls, idade):
        return cls('Anônima', 50)

#cls é como se fosse o self, para para a classe em si, nao a instancia


Pessoa.metodoDeClasse()
p2 = Pessoa.criarComCinquentaAnos('Helena')
p3 = Pessoa.criarAnonimo(50)
print(p3.nome, p3.idade)
print(p2.nome, p2.idade) 