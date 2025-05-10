#DECLARAÇAO DE CLASSES

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Tony', 'Sousa')
print(10 * '-')
print(p1.nome, p1.sobrenome)



#METODOS E INSTANCIAS DE CLASSES
class Moto:
    def __init__(self, nome = 'indefinido', marca = 'indefinido', ano = 'indefinido'):
        self.nome = nome
        self.marca = marca
        self.ano = ano

    def acelerar(self,):
        print(f'{self.nome} está acelerando vrum vrum')   

carro1 = Moto()
carro2 = Moto('Factor', 'Yamaha', '2009')

print(10 * '-')
print(carro1.nome, carro1.marca, carro1.ano)
print(carro2.nome, carro2.marca, carro2.ano)

print(10 * '-')
carro1.acelerar()
carro2.acelerar()

#ATRIBUTOS DE CLASSE

class Pessoa():

    ANO_ATUAL = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def anoNascimento(self):
        return Pessoa.ANO_ATUAL - self.idade
    

p1 = Pessoa('Tony', 18)

print(10 * '-')
print(f'{p1.nome} nasceu no ano de {p1.anoNascimento()}.')

#__dict__ E vars PARA ATRIBUTOS DE INSTANCIA

print(10 * '-')
print(p1.__dict__)
print(vars(p1))