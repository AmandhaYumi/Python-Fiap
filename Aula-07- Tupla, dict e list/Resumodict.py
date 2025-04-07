#Um dict em Python é uma coleção poderosa e altamente flexível que armazena pares chave-valor. Ele é implementado como uma tabela hash, tornando a busca por valores extremamente eficiente (em tempo aproximado de O(1) na maioria dos casos). As chaves devem ser únicas e imutáveis, como strings, números ou tuplas, enquanto os valores podem ser de qualquer tipo de dado. Dicionários suportam diversas operações, como:

-Acesso rápido: Usando dict[key] para acessar valores associados a uma chave.

-Métodos úteis: Métodos como .get(), .keys(), .values(), .items() permitem manipular dados de forma prática.

-Iteração: É possível iterar sobre chaves, valores ou pares chave-valor.

-Manipulação dinâmica: Permite adicionar ou remover elementos facilmente.

#Iterando Sobre um Dicionário
for chave, valor in pessoa.items():
 print(f"{chave}: {valor}")

#Removendo Elementos
- Use `del` para remover um item específico.
del pessoa["cidade"]
