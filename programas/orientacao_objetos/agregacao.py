# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

# Classe que representa um Carrinho de compras
class Carrinho:
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os produtos no carrinho
        self._produtos = []

    # Método que calcula o total do carrinho
    def total(self):
        # Soma os preços de todos os produtos no carrinho
        return sum([p.preco for p in self._produtos])
    
    # Método para adicionar um ou mais produtos ao carrinho
    def inserir_produtos(self, *produtos):
        # Itera sobre os produtos passados e adiciona à lista do carrinho
        for produto in produtos:
            self._produtos.append(produto)
    
    # Método para listar os produtos do carrinho
    def listar_produtos(self):
        print()  # Linha em branco para melhor visualização
        for produto in self._produtos:
            # Exibe o nome e o preço de cada produto
            print(produto.nome, produto.preco)
        print()  # Outra linha em branco para separação visual

# Classe que representa um Produto
class Produto:
    def __init__(self, nome, preco):
        # Inicializa o nome e o preço do produto
        self.nome = nome
        self.preco = preco

# Criação de um objeto da classe Carrinho
carrinho = Carrinho()

# Criação de dois objetos da classe Produto
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

# Adiciona os produtos criados ao carrinho
carrinho.inserir_produtos(p1, p2)

# Exibe os produtos no carrinho
carrinho.listar_produtos()

# Calcula e exibe o total dos produtos no carrinho
print(carrinho.total())
