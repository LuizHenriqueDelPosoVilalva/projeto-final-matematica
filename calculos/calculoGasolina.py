#inputs que para o usuario digitar
distancia = float(input("Informe a distância a ser percorrida em quilómetros com ponto e não virgula: "))
consumo_medio = float(input("Informe o consumo médio de combustivel do veiculo em litros: "))
preco = float(input("Iforme o valor da gasolina em reais: R$"))

def valor_combustivel_a_pagar (dis, cons, preco):
#verificando valores digitados pelo usuário 
  if dis <=0 or cons <=0 or preco <= 0:
   apresentar = "Digite valores maiores que zero"
  else:
  #Formula de calculo do valor a pagar na gasolina de acordo com a distancia a ser percorrida e o consumo médio do usuario
    resultado = (dis/cons)*preco
    apresentar = f"O valor a pagar na gasolina é R${resultado:.2f}"
  return apresentar

valor = valor_combustivel_a_pagar(distancia,consumo_medio,preco)
print(valor)
