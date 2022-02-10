Algoritmo "desafio3"
// Disciplina   : LCA
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Charles Costa
// Data atual  : 09/02/2022


   funcao calcularQtdeDias(): inteiro
   inicio
     retorne anos * 365 + meses * 30 + dias
   fimfuncao

   procedimento impressao()
   inicio
     escreval("a sua idada em dias é igual a", calcularQtdeDias())
   fimprocedimento

var
  anos: inteiro
  meses: inteiro
  dias: inteiro

inicio
  escreva("Informe quantos anos você tem:" )
  leia(anos)

  escreva("Informe quantos meses você tem:" )
  leia(meses)

  escreva("Informe quantos dias você tem:" )
  leia(dias)

  impressao()




Fimalgoritmo