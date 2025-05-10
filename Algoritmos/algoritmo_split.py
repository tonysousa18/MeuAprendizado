frase = "        Olha so,     que lixo       "
frase_crua = frase.split(",")

lista_frase = []

for i, frase in enumerate(frase_crua):
    lista_frase.append(frase_crua[i].strip())

print(lista_frase)

frases_unidas = ", ".join(lista_frase)
print(frases_unidas)