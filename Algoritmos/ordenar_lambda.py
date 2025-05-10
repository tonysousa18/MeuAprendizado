lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista):
    for i in lista:
        print(i)
    print()


lista.sort(key=lambda item: item['nome'])
l1 = sorted(lista, key= lambda item: item['nome'])

exibir(lista)
print()
exibir(l1)
