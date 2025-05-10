# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor, cor_tampa):
        self._cor = cor
        self._cor_tampa = cor_tampa

#esse metodo protege o self.cor, ja que é só usar o metodo ao inves de self.cor, evitando eu avisar quando mudar o nome
#property faz com que seja desnecessario parentenses ()    
    @property
    def cor(self):
        return self._cor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor.setter
    def cor(self, valor):
        if valor == 'algo':
            raise ValueError('Eu não aceito isso!')
        self._cor = valor

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self.cor_tampa = valor
    



caneta = Caneta('azul', 'vermelho')
print(f'cor da caneta: {caneta.cor}, cor da tampa: {caneta._cor_tampa}')
caneta.cor = 'Amarelo'
caneta._cor_tampa = 'Verde'
print(f'cor da caneta: {caneta.cor}, cor da tampa: {caneta.cor_tampa}')

#getter --> obter valor