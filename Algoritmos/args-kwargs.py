#args recebe coisas idependente de nome e quantidade
def arg(*args):
    return sum(args)

print(arg(1, 2, 3, 54))

#kwargs recebem apenas coisas com nome
def kwarg(**kwargs):
    print(kwargs)

kwarg(numero = 2)