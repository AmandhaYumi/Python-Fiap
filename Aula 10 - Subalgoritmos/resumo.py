#Funções
def soma(a, b):
return a + b
resultado = soma(3, 4)
print(resultado) 
# Saída: 7
------------------------------------
#Procedimentos
def saudacao(nome):
print(f"Olá, {nome}!")
saudacao("João") 
# Saída: Olá, João
------------------------------------------
#Variável de Ambiente __main__
#Arquivo: meu_script.py
def principal():
print("Este é o programa principal.")
if __name__ == "__main__":
principal()

#Importando Subalgoritmos
Criando um Módulo
# Arquivo: meu_modulo.py
def saudacao(nome):
print(f"Olá, {nome}!")
Importando e Usando o Módulo
# Arquivo: principal.py
import meu_modulo
meu_modulo.saudacao("João") 
# Saída: Olá, João!

------------------------------------
#Parâmetros
#Reais
minha_funcao(10, 20)
#Posicionais
def subtracao(a, b):
return a - b
resultado = subtracao(10, 5)
print(resultado) 
# Saída: 5
#Nomeados
def subtracao(a, b):
return a - b
resultado = subtracao(b=5, a=10)
print(resultado) 
# Saída: 5
#Padrão
def saudacao(nome="Mundo"):
print(f"Olá, {nome}!")
saudacao() # Saída: Olá, Mundo!
saudacao("João")# Saída: Olá, João!
#Arbitrários
def soma(*args):
return sum(args)
resultado = soma(1, 2, 3, 4)
print(resultado) # Saída: 10


def informacoes(**kwargs):
for chave, valor in kwargs.items():
print(f"{chave}: {valor}")
informacoes(nome="João", idade=30)
# Saída:
# nome: João
# idade: 30
*args permite passar um
número variável de
argumentos posicionais.
**kwargs permite passar
um número variável de
argumentos nomeados.

