frase = "Tony Sousa Lopes"
indice = 0
maior_frequencia = 0
letra_mais_frequente = ""


while indice < len(frase):
    letra_atual = frase[indice] 

    if letra_atual == " ":
        indice += 1 
        continue 
    
    frequencia_atual = frase.count(letra_atual)
    
    if maior_frequencia < frequencia_atual:
        maior_frequencia = frequencia_atual
        letra_mais_frequente = letra_atual

    indice += 1

print(f"A letra que mais apareceu foi: {letra_mais_frequente}, {maior_frequencia} vezes")
