Algoritmo "desafio3"
// Disciplina   : LCA
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Charles Costa
// Data atual  : 09/02/2022


   funcao calcularQtdeDias(): inteiro
   inicio
     retorne anos * 365 + meses * 30 + dias
   fimfuncao

   procedimento impressao()
   inicio
     escreval("a sua idada em dias � igual a", calcularQtdeDias())
   fimprocedimento

var
  anos: inteiro
  meses: inteiro
  dias: inteiro

inicio
  escreva("Informe quantos anos voc� tem:" )
  leia(anos)

  escreva("Informe quantos meses voc� tem:" )
  leia(meses)

  escreva("Informe quantos dias voc� tem:" )
  leia(dias)

  impressao()




Fimalgoritmo