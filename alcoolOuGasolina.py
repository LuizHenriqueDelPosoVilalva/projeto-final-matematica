#Segundo o engenheiro Gabriel Branco, especialista em motores, um veículo abastecido com etanol rende, em média, 30% a menos do que se estivesse com gasolina
#Calculo de álcool e gasolina
alcool = float(input("Digite o valor do álcool por litro(Etanol) em reais, com ponto, não virgula: R$:"))
gasolina = float(input("Digite o valor da gasolina por litro em reais, com ponto, não virgula: R$:"))

def verificacao (red):
  #comparando qual é melhor
  if red > 0 and red <= 0.7:
    resultado ="Vale mais a pena abastecer com álcool!"
  if red > 0.7:
    resultado = "Vale mais a pena abastecer com gasolina!"
  
  return resultado

#verificando valores digitados pelo usuário 
if gasolina and alcool > 0:
  rendimento = alcool/gasolina
  apresentar = verificacao(rendimento)
  print(apresentar)
else:
  print("Digite valores maiores que 0")
