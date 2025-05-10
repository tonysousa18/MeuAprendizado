class Elemento():
    def executar(self) -> None:
        print('Executando')

class Principal:
    def __init__(self) -> None:
        self.__elemento = Elemento()

    def run(self):
        self.__elemento.executar()
        print('Executado a classe Principal')


cl1 = Principal()
cl1.run()