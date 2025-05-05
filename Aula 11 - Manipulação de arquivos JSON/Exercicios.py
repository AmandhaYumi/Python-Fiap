import pandas as pd
import json

json_data ='''
[
    {"name": "John", "age": 28, "city": "New York"},
    {"name": "Anna", "age": 22, "city": "London"},
    {"name": "Mike", "age": 32, "city": "Chicago"}
]
'''
df = pd.read_json(json_data)
print(df)

#Prova Python
-Fazer um programa com menu
-Tem que ter opção de ler dados, criar registro, remover registro, alterar registro e pesquisar por estado.
-1-Listagem de todos os registros que está no dict.>Try
-2-Criar um registro no arquivo json que será aumentado e reduzido de acordo com as opções.>Dict
-3-Remover registro.>Dict
-4-Opção de alterar um resgistro.>Dict
-5-Opção de escolha de pesquisa por estado.

___
|nome-str
|idade-int
|sexo-str
|idade-int
|estado-st
|__                        (Estado é tupla)



