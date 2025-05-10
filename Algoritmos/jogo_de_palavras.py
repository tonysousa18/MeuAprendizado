"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


# Define a palavra secreta que o jogador precisa adivinhar
palavra_secreta = 'perfume'

# Variável para armazenar as letras que o jogador acertou
letras_acertadas = ''

# Variável para contar o número de tentativas feitas pelo jogador
numero_tentativas = 0

# Loop infinito para continuar solicitando letras até que a palavra seja adivinhada
while True:
    # Solicita ao jogador que insira uma letra
    letra_digitada = input('Digite uma letra: ')
    
    # Incrementa o número de tentativas a cada letra digitada
    numero_tentativas += 1

    # Verifica se o jogador digitou mais de uma letra
    if len(letra_digitada) > 1:
        # Exibe mensagem de erro e continua para a próxima iteração
        print('Digite apenas uma letra.')
        continue

    # Verifica se a letra digitada está na palavra secreta
    if letra_digitada in palavra_secreta:
        # Se a letra estiver presente, ela é adicionada à lista de letras acertadas
        letras_acertadas += letra_digitada

    # Inicializa uma string vazia que será usada para formar a palavra até o momento
    palavra_formada = ''
    
    # Loop para verificar cada letra da palavra secreta
    for letra_secreta in palavra_secreta:
        # Se a letra secreta já foi acertada, ela é adicionada à palavra formada
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            # Se a letra ainda não foi acertada, é substituída por um '*'
            palavra_formada += '*'

    # Exibe a palavra formada até o momento, com as letras acertadas e os '*' restantes
    print('Palavra formada:', palavra_formada)

    # Verifica se a palavra completa foi adivinhada (sem '*' restantes)
    if palavra_formada == palavra_secreta:
        # Se o jogador adivinhar a palavra, exibe uma mensagem de vitória
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        
        # Exibe o número de tentativas feitas
        print('Tentativas:', numero_tentativas)
        
        # Reseta as variáveis para que o jogo possa ser jogado novamente
        letras_acertadas = ''
        numero_tentativas = 0
