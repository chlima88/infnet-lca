Algoritmo "semnome"
// Disciplina   : [L�gica, Computa��o e Algoritmos]
// Professor   : Elberth Lins Costa de Moraes
// Descri��o   : Desafio 01: Atribui��o de vari�veis
//             Escreva um algoritmo que armazene o valor 10 em uma vari�vel A e
//             o valor 20 em uma vari�vel B.
//             A seguir troque os seus conte�dos fazendo com que o valor que
//             est� em A passe para B e vice-versa.
//             Ao final, escrever os valores que ficaram armazenados nas
//             vari�veis.
// Autor(a)    : Charles de Jesus Lima da Costa
// Data atual  : 03/02/2022
Var

a: inteiro
b: inteiro
aux: inteiro

Inicio

a <- 10
b <- 20

aux <- a
a <- b
b <- aux


escreval("Valor de A: ", a)
escreval("Valor de B: ", b)

Fimalgoritmo