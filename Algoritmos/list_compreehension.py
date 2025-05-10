frases = [
    "Eu adoro programação",
    "Python é uma linguagem incrível",
    "Vamos aprender list comprehension",
    "Exercícios são ótimos para praticar"
]

nova_lista = [len(frase.split()) for frase in frases]
print(nova_lista)