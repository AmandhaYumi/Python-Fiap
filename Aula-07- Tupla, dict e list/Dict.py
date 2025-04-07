#O que é?
- Um dicionário em Python é uma
coleção de pares chave:valor
- É um tipo de dado mutável, o que
significa que você pode alterar,
adicionar ou remover itens após sua
criação.
- Chaves são únicas e imutáveis (strings,
números, tuplas), enquanto os valores
podem ser de qualquer tipo.

#Acessando Valores
- Use a chave para acessar o valor correspondente.
nome = pessoa["nome"] # Retorna "João"

#Modificando Valores
- Modifique um valor existente ou adicione um novo par chave:valor.
pessoa["idade"] = 26 # Modifica o valor existente
pessoa["profissao"] = "Engenheiro" # Adiciona um novo par

#Métodos Comuns
- keys(): Retorna todas as chaves do dicionário.
- values(): Retorna todos os valores do dicionário.
- items(): Retorna uma lista de tuplas (chave, valor).
- get(chave, valor_default): Retorna o valor associado à chave, ou um valor 
padrão se a chave não existir.
- pop(chave): Remove e retorna o valor associado à chave.

#Iterando Sobre um Dicionário
for chave, valor in pessoa.items():
 print(f"{chave}: {valor}")

#Removendo Elementos
- Use `del` para remover um item específico.
del pessoa["cidade"]
