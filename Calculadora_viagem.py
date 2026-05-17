while True: ## Loop para garantir que o usuário insira valores válidos e para caso haja algum erro na inserção dos dados
  try:
    Orcamento_disponivel = float(input("Insira o valor disponível para a viagem ")) 
    Destino = input("Qual o país ou cidade desejado? ")
    Custo_passagem = float(input("Insira o custo para a passagem em reais ")) 
    Custo_hospedagem = float(input("Quanto custará a diária da hospedagem em Euros ")) 
    Duracao_viagem = int(input("Insira a duração da viagem em dias ")) 

    if Orcamento_disponivel > 0 and Custo_hospedagem > 0 and Custo_passagem > 0 and Duracao_viagem > 0 and Destino.isalpha(): ## Condição que valida os valores
      break
    else:
      print("Valores inválidos, insira apenas positivos para os referentes a dinheiro e à quantidade de dias ou palavras para o destino ")
      continue

  except ValueError:
    print("Insira valores válidos para os dados requisitados ")
    continue


Valor_euro = 5.9
Valor_hospedagem_reais = Custo_hospedagem * Valor_euro 
Custo_hospedagem_reais = Valor_hospedagem_reais * Duracao_viagem ## Cálculo de conversão e custo em reais

Custo_total_viagem = Custo_passagem + Custo_hospedagem_reais ##Cálculo do custo total da viagem

if Custo_total_viagem <= Orcamento_disponivel: ##Condicional que define se o orçamento é suficiente dado custo
  situacao = "suficiente"
else:  situacao = "insuficiente"

Viagem_viavel = (Custo_total_viagem <= Orcamento_disponivel) and Duracao_viagem > 0 ##Verificação de viabilidade

if Viagem_viavel:
  resultado = "viagem é possível"
else:  
  resultado = "viagem não é possível"

Sobra_ou_Precisa = Orcamento_disponivel - Custo_total_viagem ##Cálculo de sobra ou valor necessário para realizar a viagem


print ("\nResultados:")   ##Exibição dos resultados para o usuário 

print(f"O valor total gasto com a hospedagem é de R$ {Custo_hospedagem_reais:.2f}")
print(f"O custo total da viagem é de R$ {Custo_total_viagem:.2f}")
print(f"O orçamento para a viagem é {situacao}")
print(f"Então, com base nos resultados prévios a {resultado}")

if Sobra_ou_Precisa > 0:  ##Condicional para exibir se haverá sobra ou se precisará de mais dinheiro para realizar a viagem
    print(f"Você terá uma sobra de R$ {Sobra_ou_Precisa:.2f} após a viagem. Arrume suas malas e aproveite sua viagem para {Destino}!")
else:    
  print(f"Você precisará juntar R$ {abs(Sobra_ou_Precisa):.2f} adicionais para realizar a viagem.")