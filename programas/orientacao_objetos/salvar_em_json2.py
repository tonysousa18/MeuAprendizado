from orientacao_objetos.salvar_em_json import Pessoa, fazerDump
import json

# Caminho do arquivo JSON a ser lido
file_path = 'json/dados.json'

# Lendo o conteúdo do arquivo JSON
with open(file_path, 'r') as json_file:
    dados = json.load(json_file)

# Exibindo os dados carregados

p1 = Pessoa(**dados[0])
p2 = Pessoa(**dados[1])
p3 = Pessoa(**dados[2])

print(p1.retornarCoisas())
print(p2.retornarCoisas())
print(p3.retornarCoisas())