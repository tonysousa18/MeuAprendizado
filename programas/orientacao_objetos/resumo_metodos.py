# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    #methods sao metodos da instancia(self)
    def __init__(self, host = 'localhost'):
        self.host = host
        self.user = None
        self.password = None

    def setUser(self, user):
        self.user = user

    def setPassword(self, password):
        self.password = password

    #methods sao metodos da classe (cls)
    @classmethod
    def setDefault(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    #staticmethods sao metodos do escopo da classe mas nao recebem cls
    @staticmethod
    def log(msg):
        print('LOG:', msg)

    
    def verificaUsuario(self, usuario, senha):
        if usuario == self.user and senha == self.password:
            Connection.log('Autenticado')
        else:
            Connection.log('Nao autenticado')

        
    
Conexao = Connection.setDefault('Tony', '123')
Conexao.verificaUsuario('Tony', '123')
