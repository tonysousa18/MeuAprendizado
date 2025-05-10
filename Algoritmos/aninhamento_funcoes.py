def multiplicar(mul):
    def multiplicando(num):
        return num * mul
    return multiplicando

quadruplicar = multiplicar(4)

print(quadruplicar(4))