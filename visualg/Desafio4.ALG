Algoritmo "semnome"
// Disciplina   : LCA
// Professor   : Elberth Lins Costa de Moraes
// Descri��o   : Desafio 04 - Relat�rio de funcion�rio
//             Receba o nome, o sobrenome, a idade, o sal�rio e o desconto do
//             funcion�rio.
//             Exiba a seguinte frase: "O funcion�rio aaa bbb nasceu em ccc e
//             ganha R$ddd". Onde:
//             aaa � o nome do funcion�rio e bbb � o sobrenome;
//             ccc � o ano de nascimento do funcion�rio;
//             ddd � o sal�rio l�quido = sal�rio - desconto.
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
   escreva("informe o sal�rio: ")
   leia(salario)
   escreva("Informe o desconto: ")
   leia(desconto)

   // anoNascimento <- 2022 - idade
   // salarioLiquido <- salario - desconto

   // escreval("O funcionario ",nome," ",sobrenome," nasceu em ",anoNascimento," e ganha ",salarioLiquido)

   impressao()

Fimalgoritmo
