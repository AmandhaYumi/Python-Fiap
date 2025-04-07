#Tupla é uma lista que não muda como os estados do brasil
tupla_vazia = ()
tupla_simples = (5,)
tupla_variada = (1, "hello", 3.14)

#Acessando elementos:
#Ultilize indices para acessar elementos individuais da tupla, éndices começam em 0
primeiro = tupla_variada[0] #Retorna 1
ultimo = tupla_variada[-1] #Retorna 3.14

#Operações comuns
-Contatenar Tuplas: tupla1 + tupla2
-Repetir Tuplas: tupla * n
-Verificar Existência: elemento in tupla

#Imutabilidade
- Tuplas não permitem a alteração de seus elementos após a criação.
- Exemplo: tupla_variada[0] = 2 resultará em um erro.

#Métodos Comuns
- count(valor): Conta quantas vezes um valor aparece na tupla.
- index(valor): Retorna o índice da primeira ocorrência do valor.

#Desempacotamento de Tuplas
- Tuplas permitem que múltiplas variáveis sejam atribuídas de uma vez.
a, b, c = tupla_variada # a=1, b="hello", c=3.14

#Tuplas vs Listas
- Imutabilidade: Tuplas são imutáveis, listas são mutáveis.
- Uso: Use tuplas quando a integridade dos dados é crítica e você deseja 
garantir que eles não sejam alterados

