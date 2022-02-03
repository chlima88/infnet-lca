Algoritmo "semnome"
// Disciplina   : [Lógica, Computação e Algoritmos]
// Professor   : Elberth Lins Costa de Moraes
// Descrição   : Desafio 03: data em dias
//             Faça um algoritmo que leia a idade de uma pessoa expressa em
//             anos, meses e dias e escreva a idade dessa pessoa expressa
//             apenas em dias.
//             Considerar ano com 365 dias e mês com 30 dias.
// Autor(a)    : Charles de Jesus Lima da Costa
// Data atual  : 03/02/2022
Var
idadeDias: inteiro
idadeMeses: inteiro
idadeAnos: inteiro
idadeFinal: inteiro

Inicio

escreva("Informe a quantidade de anos: ")
leia(idadeAnos)
escreva("Informe a quantidade de meses: ")
leia(idadeMeses)
escreva("Informe a quantidade de dias: ")
leia(idadeDias)

idadeFinal <- (idadeAnos * 365) + (idadeMeses * 30) + idadeDias

escreval("A idade em dias é", idadeFinal)

Fimalgoritmo