Algoritmo "semnome"
// Disciplina   : LCA
// Professor   : Elberth Lins Costa de Moraes
// Descrição   : Desafio 04 - Relatório de funcionário
//             Receba o nome, o sobrenome, a idade, o salário e o desconto do
//             funcionário.
//             Exiba a seguinte frase: "O funcionário aaa bbb nasceu em ccc e
//             ganha R$ddd". Onde:
//             aaa é o nome do funcionário e bbb é o sobrenome;
//             ccc é o ano de nascimento do funcionário;
//             ddd é o salário líquido = salário - desconto.
// Autor(a)    : Charles Costa
// Data atual  : 09/02/2022


funcao calculaAnoNascimento(): inteiro
inicio
  retorne 2022 - idade
fimfuncao

funcao calculaSalarioLiquido(): real
inicio
  retorne salario - desconto
fimfuncao


procedimento impressao()
inicio
  anoNascimento <- calculaAnoNascimento()
  salarioLiquido <- calculaSalarioLiquido()
  escreval("O funcionario ",nome," ",sobrenome," nasceu em ", anoNascimento," e ganha ",salarioLiquido )
fimprocedimento

var

   nome: caracter
   sobrenome: caracter
   idade: inteiro
   anoNascimento: inteiro
   salario: real
   desconto: real
   salarioLiquido: real

Inicio

   escreva("Informe o nome: ")
   leia(nome)
   escreva("Informe o sobrenome: ")
   leia(sobrenome)
   escreva("Informe a idade: ")
   leia(idade)
   escreva("informe o salário: ")
   leia(salario)
   escreva("Informe o desconto: ")
   leia(desconto)

   // anoNascimento <- 2022 - idade
   // salarioLiquido <- salario - desconto

   // escreval("O funcionario ",nome," ",sobrenome," nasceu em ",anoNascimento," e ganha ",salarioLiquido)

   impressao()

Fimalgoritmo
