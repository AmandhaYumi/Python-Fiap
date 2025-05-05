#Em Python, por exemplo, os arquivos JSON podem ser abertos com:
import json
with open('data.json', 'r') as file: # Para leitura
 data = json.load(file)
with open('output.json', 'w') as file: # Para escrita
 json.dump(data, file)

#Métodos Associados
• json.load(): Lê o conteúdo de um arquivo JSON e converte em um objeto (como um dicionário ou 
lista em Python).
• json.dump(): Escreve um objeto Python em um arquivo no formato JSON.
• json.loads(): Converte uma string JSON em um objeto Python.
• json.dumps(): Converte um objeto Python em uma string no formato JSON.
with open('data.json') as file:
 data = json.load(file)
with open('output.json', 'w') as file:
 json.dump(data, file)
data = json.loads('{"key": "value"}')
json_string = json.dumps(data)

#De JSON para DataFrame
Exemplo: Carregar um JSON e converter para DataFrame
import pandas as pd
# Lendo o arquivo JSON e convertendo para DataFrame
df = pd.read_json('data.json')
# Exibindo o DataFrame
print(df)
 name age city
0 John 28 New York
1 Anna 22 London
2 Mike 32 Chicago
------------------------------
import pandas as pd
import json
# String JSON
json_data = '''
[
 {"name": "John", "age": 28, "city": "New York"},
 {"name": "Anna", "age": 22, "city": "London"},
 {"name": "Mike", "age": 32, "city": "Chicago"}
]
'''
# Converter string JSON para DataFrame
df = pd.read_json(json_data)
print(df)

#método to_json().
import pandas as pd
# Criando um DataFrame
data = {
 'name': ['John', 'Anna', 'Mike'],
 'age': [28, 22, 32],
 'city': ['New York', 'London', 'Chicago']
}
df = pd.DataFrame(data)
# Convertendo o DataFrame para JSON
json_data = df.to_json(orient='records')
# Exibindo o JSON
print(json_data)
-----------------------------------------
#• orient='records': Lista de registros (o padrão).
• orient='split': Divide o DataFrame em dicionários com chaves: “index”, “columns”, e “data”.
• orient='index': Usa os índices como chave principal.
• orient='columns': Usa as colunas como chave principal.
json_data_split = df.to_json(orient='split')
print(json_data_split)
{"columns":["name","age","city"],"index":[0,1,2],"data":[["John",28,"New York"], 
["Anna",22,"London"], ["Mike",32,"Chicago"]]}

#Contudo, JSON é uma string e, para ser manipulada por
linguagens de programação, precisa ser parseada (convertida) para uma estrutura nativa da
linguagem, como o dicionário no Python.
import json
json_string = '{"name": "John", "age": 30, "city": "New York"}’
data_dict = json.loads(json_string)
print(data_dict)
# Saída: {'name': 'John', 'age': 30, 'city': 'New York'}


