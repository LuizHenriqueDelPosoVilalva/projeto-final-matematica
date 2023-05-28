#Segundo o engenheiro Gabriel Branco, especialista em motores, um veículo abastecido com etanol rende, em média, 30% a menos do que se estivesse com gasolina

#Calculo de álcool e gasolina
alcool = float(input("Digite o valor do álcool por litro(Etanol) em reais, com ponto, não virgula: R$:"))
gasolina = float(input("Digite o valor da gasolina por litro(Etanol) em reais, com ponto, não virgula: R$:"))

def verificacao (red, al,gas):
  #Verificando valores inserido pelo usuário
  if al and gas > 0:
    #comparando qual é melhor
    if red <= 0.7:
      resultado ="Vale mais a pena abastecer com álcool!"
    else:
      resultado = "Vale mais a pena abastecer com gasolina!"
  else:
    resultado = "Digite valores maiores que 0"
  return resultado

rendimento = alcool/gasolina
apresentar =verificacao(rendimento,alcool,gasolina)
print(apresentar)
