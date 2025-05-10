import os  # Importa o módulo os para realizar operações no sistema, como limpar o terminal

lista = []  # Inicializa uma lista vazia

# Loop infinito para permitir ao usuário continuar interagindo com o programa até que ele seja encerrado manualmente
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')  # Solicita que o usuário escolha uma das opções

    if opcao == 'i':  # Verifica se o usuário escolheu a opção de inserir
        os.system('cls')  # Limpa o terminal (no Windows, use 'cls' em vez de 'clear')
        valor = input('Valor: ')  # Solicita ao usuário o valor a ser inserido
        lista.append(valor)  # Adiciona o valor à lista

    elif opcao == 'a':  # Verifica se o usuário escolheu a opção de apagar
        indice_str = input('Escolha o índice para apagar: ')  # Solicita o índice do item a ser apagado

        try:
            indice = int(indice_str)  # Tenta converter o índice em um número inteiro
            del lista[indice]  # Apaga o item da lista pelo índice
        except ValueError:
            print('Por favor digite número int.')  # Se o valor não for um número inteiro, exibe essa mensagem
        except IndexError:
            print('Índice não existe na lista')  # Se o índice estiver fora dos limites da lista, exibe essa mensagem
        except Exception:
            print('Erro desconhecido')  # Captura quaisquer outros erros desconhecidos

    elif opcao == 'l':  # Verifica se o usuário escolheu a opção de listar
        os.system('cls')  # Limpa o terminal

        if len(lista) == 0:  # Verifica se a lista está vazia
            print('Nada para listar')  # Exibe uma mensagem caso a lista esteja vazia

        # Itera sobre os itens da lista e os exibe com seus respectivos índices
        for i, valor in enumerate(lista):
            print(f"Tarefa {i + 1}: {valor}")

    else:
        print('Por favor, escolha i, a ou l.')  # Exibe essa mensagem se a opção inserida for inválida
    