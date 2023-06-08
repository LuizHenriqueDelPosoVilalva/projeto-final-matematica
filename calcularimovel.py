def calcular_parcelas_price(valor_imovel, entrada, taxa_juros, prazo):
    if valor_imovel <= 0 and entrada <= 0 and taxa_juros <= 0 and prazo <= 0:
        parcela = "Digite valores maiores que zero"
    else:
      valor_financiado = valor_imovel - entrada
      taxa_juros_mensal = taxa_juros / 100 / 12
      parcela = (valor_financiado * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -prazo)
      return parcela

def calcular_parcelas_sac(valor_imovel, entrada, taxa_juros, prazo):
    if valor_imovel <= 0 and entrada <= 0 and taxa_juros <= 0 and prazo <= 0:
        parcelas = "Digite valores maiores que zero"
    else:
      valor_financiado = valor_imovel - entrada
      taxa_juros_mensal = taxa_juros / 100 / 12
      amortizacao = valor_financiado / prazo
      parcelas = []
      saldo_devedor = valor_financiado

    for mes in range(prazo):
        juros = saldo_devedor * taxa_juros_mensal
        parcela = amortizacao + juros
        saldo_devedor -= amortizacao
        parcelas.append(parcela)

    return parcelas

def simulador_financiamento():
    print("Simulador de Financiamento de Imóvel")
    print("Opções de Financiamento:")
    print("1 - Price")
    print("2 - SAC")

    opcao = int(input("Digite o número da opção de financiamento desejada: "))

    valor_imovel = float(input("Digite o valor do imóvel: "))
    entrada = float(input("Digite o valor da entrada: "))
    taxa_juros = float(input("Digite a taxa de juros ao ano: "))
    prazo = int(input("Digite o prazo em meses: "))

    if opcao == 1:
        parcelas = calcular_parcelas_price(valor_imovel, entrada, taxa_juros, prazo)
        print("Valor da parcela mensal (Price): R$", parcelas)
    elif opcao == 2:
        parcelas = calcular_parcelas_sac(valor_imovel, entrada, taxa_juros, prazo)
        print("Valor das parcelas mensais (SAC):")
        for mes, parcela in zip(range(1, prazo + 1), parcelas):
            print("Mês", mes, "- R$", parcela)
    else:
        print("Opção inválida. Por favor, selecione 1 ou 2.")

#Executar o simulador
simulador_financiamento()
