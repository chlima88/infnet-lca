Algoritmo "semnome"
// Disciplina   : LCA
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

// Autor(a)    : Charles Costa
// Data atual  : 03/02/2022

funcao calculaPontos(): inteiro
inicio
   retorne (vitorias * 3 ) + empates
fimfuncao

procedimento impressao()
var pontos: inteiro
inicio
   pontos <- calculaPontos()
   escreva("O time ",time," esta com ",pontos)
fimprocedimento

var
   time: caracter
   vitorias: inteiro
   empates: inteiro

inicio
   escreva("informe o nome do time: ")
   leia(time)
   
   escreva("informe o numero de vitorias: ")
   leia(vitorias)
   
   escreva("Informe o numero de empates: ")
   leia(empates)

   impressao()

fimalgoritmo