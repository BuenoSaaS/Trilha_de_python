while True: ## Loop para garantir que o usuário insira valores válidos
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
      break

  except ValueError:
    print("Insira valores válidos para os dados requisitados ")


