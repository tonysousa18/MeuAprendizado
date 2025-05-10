import os  

estoque = {}  

while True:
    print("\nGerenciador de Estoque")
    opcao = input("[i]nserir [a]pagar [l]istar [t]otal: ").strip().lower()

    if opcao == "i":
        os.system("cls")  
        produto = input("Nome do produto: ").strip()
        preco = input("Preço unitário: ").strip()
        quantidade = input("Quantidade: ").strip()

        try:
            preco = float(preco)
            quantidade = int(quantidade)

            if produto in estoque:
                estoque[produto]["quantidade"] += quantidade
            else:
                estoque[produto] = {"preco": preco, "quantidade": quantidade}

            print(f"{quantidade} unidade(s) de {produto} adicionada(s) ao estoque.")

        except ValueError:
            print("Erro: Preço deve ser um número decimal e quantidade deve ser um número inteiro.")

    elif opcao == "a":
        os.system("cls")
        produto = input("Nome do produto para remover: ").strip()

        if produto in estoque:
            try:
                quantidade = int(input("Quantidade a remover: ").strip())

                if quantidade >= estoque[produto]["quantidade"]:
                    del estoque[produto]
                    print(f"Produto '{produto}' removido do estoque.")
                else:
                    estoque[produto]["quantidade"] -= quantidade
                    print(f"{quantidade} unidade(s) de {produto} removida(s).")

            except ValueError:
                print("Erro: Quantidade deve ser um número inteiro.")
        else:
            print("Produto não encontrado no estoque.")

    elif opcao == "l":
        os.system("cls")

        if not estoque:
            print("Estoque vazio.")
        else:
            print("\nEstoque Atual:")
            for i, (produto, dados) in enumerate(estoque.items(), start=1):
                print(f"{i}. {produto} - R$ {dados['preco']:.2f} | Quantidade: {dados['quantidade']}")

    elif opcao == "t":
        os.system("cls")
        total = sum(dados["preco"] * dados["quantidade"] for dados in estoque.values())
        print(f"Valor total do estoque: R$ {total:.2f}")

    else:
        print("Opção inválida. Escolha entre [i], [a], [l] ou [t].")
