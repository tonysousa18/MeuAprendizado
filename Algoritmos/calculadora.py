print("bem vindo(a) a calculadora")

#Condição pro while funcionar e mostrar o menu
saida = True

#enquanto saida for verdadeira, o menu vai rodar
while saida == True:
    #recebe entrada do usuario, tira espaços vazios (strip) e transforma em  minusculo (lower)
    entrada = input("Digite o que quer fazer: \nCalcular [C] \nSair[S]\n").strip().lower()

    #se a entrada do usuario for "s" ou começar com "s", sai  do programa
    if entrada == "s" or entrada.startswith("s"):
        break
    
    #se a entrada for "c", continua
    elif entrada == "c":

        #recebe entrada do usuario, tira espaços vazios (strip) e transforma em  minusculo (lower)
        operação = input("Digite a operação que quer fazer: \n Soma[+] \n Subtração[-] \n \
                         Multiplicação[*] \n Divisão[/]\n").strip().lower()
        contas = ["+", "-", "*", "/"]
        #cria uma lista de operações disponiveis

        #se a operação escolhida pelo usuario estiver na lista de contas aceitas, requisita os numeros desejados
        if operação in contas:
            numero1 = float(input("Digite o primeiro numero: \n"))
            numero2 = float(input("Digite o segundo numero: \n"))

            #cria um match case com a operação escolhida,
            match (operação):
                case "+":
                    resultado = numero1 + numero2
                    print(f" o resultado da soma foi {resultado:.1f}\n")

                case "-":
                    resultado = numero1 - numero2
                    print(f"o resultado da subtração foi {resultado:.2f}\n")

                case "*":
                    resultado = numero1 * numero2
                    print(f"o resultado da multiplicação foi {resultado:.1f}\n")

                case "/":
                    resultado = numero1 / numero2
                    print(f"o resultado da divisão foi {resultado:.2f}\n")
        #se a operaçao escolhida nao estiver na lista, será invalido
        else:             
            print("\nOperação invalida")
            continue

        #se o usuario digitar qualquer coisa alem de S ou C, entrada invalida, e o programa volta a fazer o while   
    else:
        print("\nEntrada invalida\n")
        continue