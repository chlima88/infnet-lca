Algoritmo "semnome"
// Disciplina   : [Lógica, Computação e Algoritmos]
// Professor   : Elberth Lins Costa de Moraes
// Descrição   : Desafio 05 - Jogo de futebol
//             Receba o nome do time, a quantidade de vitórias, a quantidade de
//             empates.
//             Exiba o seguinte relatório:
//             "O time xxx está com yyy pontos". Onde:
//             xxx é o nome do time;
//             yyy é a quantidade de pontos;
//             A pontuação deve ser calculada da seguinte maneira: quantidade
//             de vitórias * 3 pontos + quantidade de empates

// Autor(a)    : Charles de Jesus Lima da Costa
// Data atual  : 03/02/2022

Var

time: caracter
vitorias: inteiro
empates: inteiro
pontos: inteiro

Inicio

escreva("informe o nome do time: ")
leia(time)
escreva("informe o numero de vitorias: ")
leia(vitorias)
escreva("Informe o numero de empates: ")
leia(empates)

pontos <- (vitorias * 3 ) + empates

escreva("O time ",time," esta com ",pontos)

Fimalgoritmo