Algoritmo "semnome"
// Disciplina   : [Lógica, Computação e Algoritmos]
// Professor   : Elberth Lins Costa de Moraes
// Descrição   : Desafio 01: Atribuição de variáveis
//             Escreva um algoritmo que armazene o valor 10 em uma variável A e
//             o valor 20 em uma variável B.
//             A seguir troque os seus conteúdos fazendo com que o valor que
//             está em A passe para B e vice-versa.
//             Ao final, escrever os valores que ficaram armazenados nas
//             variáveis.
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