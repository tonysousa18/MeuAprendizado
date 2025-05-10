import os

class Produto:
    #Classe que representa um produto no estoque.
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def calcular_valor_total(self):
        #Calcula o valor total do produto no estoque.
        return self.quantidade * self.preco

class Estoque:
    #Classe para gerenciar o estoque de produtos.
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, quantidade, preco):
        #Adiciona ou atualiza um produto no estoque.
        if nome in self.produtos:
            self.produtos[nome].quantidade += quantidade
        else:
            self.produtos[nome] = Produto(nome, quantidade, preco)

    def remover_produto(self, nome, quantidade):
       #Remove uma quantidade específica de um produto do estoque.
        if nome in self.produtos:
            if self.produtos[nome].quantidade >= quantidade:
                self.produtos[nome].quantidade -= quantidade
                if self.produtos[nome].quantidade == 0:
                    del self.produtos[nome]
            else:
                print(f"Erro: Estoque insuficiente para {nome}.")
        else:
            print(f"Erro: Produto {nome} não encontrado.")

    def listar_produtos(self):
        #Lista todos os produtos no estoque.
        os.system("cls" if os.name == "nt" else "clear")
        if not self.produtos:
            print("Estoque vazio.")
        else:
            print("Produtos no estoque:")
            for produto in self.produtos.values():
                print(f"{produto.nome} - Quantidade: {produto.quantidade}, Preço: R${produto.preco:.2f}")

    def calcular_valor_total_estoque(self):
        #Calcula o valor total de todos os produtos no estoque (Paradigma Funcional).
        return sum(produto.calcular_valor_total() for produto in self.produtos.values())

# Código Imperativo (Fluxo principal do programa)
estoque = Estoque()

while True:
    print("\nSelecione uma opção:")
    opcao = input("[A]dicionar [R]emover [L]istar [V]alor Total [S]air: ").strip().lower()

    if opcao == "a":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        estoque.adicionar_produto(nome, quantidade, preco)

    elif opcao == "r":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade a remover: "))
        estoque.remover_produto(nome, quantidade)

    elif opcao == "l":
        estoque.listar_produtos()

    elif opcao == "v":
        print(f"Valor total do estoque: R${estoque.calcular_valor_total_estoque():.2f}")

    elif opcao == "s":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Escolha A, R, L, V ou S.")
