#Estrutura de repetição
Laço pré-condicional
(enquanto | while)
O laço while executa um bloco de código enquanto uma condição for verdadeira. A condição é verificada antes da execução do código, ou seja, o bloco de código pode não ser executado nenhuma vez, caso a condição seja falsa desde o início.
contador = 0
while contador < 5:
    print(contador)
    contador += 1
#------------------------------------
Laço pós-condicional
(Repita | *do while)
O laço do-while é semelhante ao while, mas a principal diferença é que ele executa o bloco de código pelo menos uma vez, pois a condição é verificada após a execução do código. Esse tipo de laço é comum em linguagens como C e Java (no Python, o do-while não é nativo, mas pode ser simulado).
int i = 0;
do {
    printf("%d\n", i);
    i++;
} while (i < 5);
#------------------------------------
#Estruturas de repetição
Os comandos break, continue e else são utilizados para controlar o fluxo de execução dentro de laços (como for e while) e estruturas condicionais (if). Cada um tem uma funcionalidade específica para alterar a maneira como o código é executado, proporcionando maior flexibilidade e controle.

#1. Comando break
O comando break é utilizado para interromper imediatamente a execução de um laço (seja for, while ou do-while) ou de uma estrutura de switch. Quando o break é encontrado, o laço ou a estrutura de controle é finalizado e a execução do programa continua após o laço ou estrutura.

#2. Comando continue
O comando continue faz com que a execução do laço continue na próxima iteração, ignorando o restante do código na iteração atual. Em outras palavras, o continue faz com que o laço pule o código que vem após ele na mesma iteração e vá diretamente para a próxima verificação da condição do laço.

#3. Comando else 
O comando else é normalmente utilizado em estruturas condicionais (if, elif, else), mas também pode ser utilizado com laços. A principal diferença é que, quando usado com laços, o bloco de código dentro do else será executado somente se o laço terminar normalmente, ou seja, sem ser interrompido por um break.
