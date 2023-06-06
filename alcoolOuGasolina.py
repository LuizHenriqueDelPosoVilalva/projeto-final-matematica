#Calculo de álcool e gasolina
alcool = float(input("Digite o valor do álcool por litro(Etanol) em reais, com ponto, não virgula: R$:"))
gasolina = float(input("Digite o valor da gasolina por litro em reais, com ponto, não virgula: R$:"))

def verificacao (al,gas):
  #verificando os valores inseridos pelo usuario
  if al <= 0 and gas <= 0:
    resultado = "Digite valores maiores que zero"
  else:
    rendimento = al/gas
  #comparando qual é melhor
  if rendimento > 0 and rendimento <= 0.7:
    resultado ="Vale mais a pena abastecer com álcool!"
  else:
    resultado = "Vale mais a pena abastecer com gasolina!"
  
  return resultado

calculo = verificacao (alcool, gasolina)
print(calculo)

#Segundo o engenheiro Gabriel Branco, especialista em motores, um veículo abastecido com etanol rende, em média, 30% a menos do que se estivesse com gasolina