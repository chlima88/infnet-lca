Algoritmo "semnome"
// Disciplina   : [Lógica, Computação e Algoritmos]
// Professor   : Elberth Lins Costa de Moraes
// Descrição   : Desafio 02 - Dimensões do triangulo
//             Escreva um algoritmo para ler as dimensões de um triângulo
//             base e altura), calcular e escrever a área do triângulo.
//             Sabendo que para calcular a área devemos usar a fórmula a
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

escreval("A área é de", area, " centimetros")

Fimalgoritmo