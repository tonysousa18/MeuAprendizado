import json 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def retornarCoisas(self):
        return self.nome, self.idade
 
pessoa1 = Pessoa('Tony', 18)
pessoa2 = Pessoa('Leticia', 19)
pessoa3 = Pessoa('Petrucio', 29)


todos_dados = [pessoa1.__dict__, pessoa2.__dict__, pessoa3.__dict__]

caminho = 'json/dados.json'

def fazerDump():
    with open(caminho, 'w') as json_file:
        json.dump(todos_dados, json_file, ensure_ascii=False, indent=4)    

