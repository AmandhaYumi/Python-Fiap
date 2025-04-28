#List
• Em Python, uma lista (list) é uma coleção ordenada de
itens que pode conter elementos de diferentes tipos,
como inteiros, strings, ou até outras listas.
• As listas são mutáveis, o que significa que os itens
podem ser alterados após a criação da lista.

#Criação de uma lista

# Lista vazia
lista_vazia = []

# Lista com elementos
numeros = [1, 2, 3, 4, 5]
palavras = ['python', 'é', 'legal']
mista = [1,
'hello', 3.5, [1, 2, 3]]

#Acessando Elementos
• Use índices para acessar elementos individuais.
• Índices começam em 0.
primeiro_elemento = numeros[0] # Retorna 1
ultimo_elemento = numeros[-1] # Retorna 5

#Modificando elementos
• Modifique um item diretamente pelo índice.
numeros[0] = 10 # Muda o primeiro elemento para 10

#Métodos Comuns
• append(item): Adiciona um item ao final da lista.
• insert(index , item): Adiciona item no índice especificado.
• remove(item): Remove a primeira ocorrência do item.
• pop(index): Remove e retorna o item no índice especificado.
• sort(): Ordena a lista in-place.
• reverse(): Inverte a ordem dos elementos da lista.

#Operações comuns:

# Concatenar listas
lista_concatenada = numeros + palavras
# Repetir listas
lista_repetida = numeros * 2
# Tamanho da lista
tamanho = len(numeros)
# Checar se um item está na lista
existe = 3 in numeros
# Fatiamento
• Fatie listas para acessar sublistas.
sublista = numeros[1:3] # Retorna [2, 3]
#Compreensão de Lista
• Crie listas de forma concisa usando expressões.
quadrados = [x**2 for x in numeros] # [1, 4, 9, 16, 25]
#Iterando Sobre Listas
• Use loops para percorrer os elementos de uma lista.
for numero in numeros:
 print(numero)

 

