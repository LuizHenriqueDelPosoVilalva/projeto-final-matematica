#Segundo o engenheiro Gabriel Branco, especialista em motores, um veículo abastecido com etanol rende, em média, 30% a menos do que se estivesse com gasolina
#Calculo de álcool e gasolina
alcool = float(input("Digite o valor do álcool por litro(Etanol) em reais, com ponto, não virgula: R$:"))
gasolina = float(input("Digite o valor da gasolina por litro em reais, com ponto, não virgula: R$:"))

def verificacao (al,gas):
  rendimento = al/gas
  #comparando qual é melhor
  if rendimento > 0 and rendimento <= 0.7:
    resultado ="Vale mais a pena abastecer com álcool!"
  if rendimento > 0.7:
    resultado = "Vale mais a pena abastecer com gasolina!"
  
  return resultado

#verificando valores digitados pelo usuário 
if gasolina and alcool > 0:
  apresentar = verificacao(alcool,gasolina)
  print(apresentar)
else:
  print("Digite valores maiores que 0")
