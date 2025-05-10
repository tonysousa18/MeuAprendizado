from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter, UserDict, UserList, UserString


#NAMEDTUPLE - 
BookClass = namedtuple('Book', ['name', 'ISBN', 'quantity'])
Book1 = BookClass('Hands on Data Structures', '21987712', '50')

#Acessando itens de dados
print(Book1.name)
print(Book1.ISBN)
print(20 * '-')

#DEQUE (DOUBLE ENDED QUEUE) - Fila de duas extremidades
print(20 * '-')

my_queue = deque([1, 2, 3])

#Inserindo a direita
my_queue.append(4)

#Inserindo a esquerda
my_queue.appendleft(0)

print(*my_queue)

#Tirando a direita
my_queue.pop()

#Tirando a esquerda
my_queue.popleft()
print(*my_queue)

#ORDERED DICTS - Preserva a ordem de entrada de um dicionario
print(20 * '-')

od = OrderedDict({'my': 2, 'name': 4, 'is': 2, 'Tony': 5})
od['Hello'] = 4
print(od)

#DEFAULT DICT - Sem KeyErrors
print(20 * '-')

d = defaultdict(int)
words = str.split('Data python data structure data python')

for word in words:
    d[word] += 1
print(d)

#CHAINMAP - Lista de dicionarios
print(20 * '-')

dict1 = {'data': 1, 'structure': 2}
dict2 = {'python': 3, 'structure': 4}
chain = ChainMap(dict1, dict2)

print(chain)
print(list(chain.keys()))
print(list(chain.values()))
print(chain['data'])
print(chain['structure'])

#COUNTER 
print(20 * '-')

inventory = Counter('hello')
print(inventory)
print(inventory['l'])

#USER DICT - Encapsula objetos de um dicionario
print(20 * '-')

class MyDict(UserDict):
    def push(self, key, value):
        raise RuntimeError('Cannot Insert')

d = MyDict({'ab': 1, 'bc': 2, 'cd': 3})
d.push('b', 2)

#USER LIST - Encapsula objetos de um dicionario
print(20 * '-')

class MyList(UserList):
    def push(self, key, value):
        raise RuntimeError('Cannot Insert')

l = MyDict([1, 2, 3, 4, 5, 6])
l.push(1, 2)

#USER STRING - Strings personalizadas
print(20 * '-')

class MyString(UserString):
    def change(self, value):
        self.data += value

s1 = MyString('Algo')
print(s1)
s1.change('H')
print(s1)
