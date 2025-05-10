# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor = cor

#esse metodo protege o self.cor, ja que é só usar o metodo ao inves de self.cor, evitando eu avisar quando mudar o nome
#property faz com que seja desnecessario parentenses ()    
    @property
    def getCor(self):
        return self.cor

caneta = Caneta('azul')
print(caneta.getCor)