Algoritmo "semnome"
// Disciplina   : [L�gica, Computa��o e Algoritmos]
// Professor   : Elberth Lins Costa de Moraes
// Descri��o   : Desafio 02 - Dimens�es do triangulo
//             Escreva um algoritmo para ler as dimens�es de um tri�ngulo
//             base e altura), calcular e escrever a �rea do tri�ngulo.
//             Sabendo que para calcular a �rea devemos usar a f�rmula a
//             seguir: =(base * altura) / 2
// Autor(a)    : Charles de Jesus Lima da Costa
// Data atual  : 03/02/2022
Var
altura: real
base: real
area: real

Inicio

escreva("Informe a altura do triangulo em cm: ")
leia(altura)
escreva("Informe a base do triangulo em cm: ")
leia(base)

area <- (base * altura) / 2

escreval("A �rea � de", area, " centimetros")

Fimalgoritmo