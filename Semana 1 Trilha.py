

while True:  ## Loop para assegurar que os dados inseridos são válidos, repete o processo em caso de valores negativos ou inválidos
  try:
    Orcamento_disponivel = float(input("Insira o valor disponivel para a viagem ")) 
    Destino = input("Qual o país ou cidade desejado? ")
    Custo_passagem = float(input("Insira o custo para a passagem em reais ")) 
    Custo_hospedagem = float(input("Quanto custará a diária da hospedagem em Euros ")) 
    Duracao_viagem = int(input("Insira a duração da viagem em dias ")) 
  
    Destino_Valido = Destino.isalpha()  ## Verifica se há apenas letras no input Destino

    if Orcamento_disponivel > 0 and Custo_hospedagem > 0 and Custo_passagem > 0 and Duracao_viagem > 0 and Destino_Valido:  ##Verificador para os valores positivos
      break
    else:
      print("Valores inválidos, insira apenas positivos para os referentes a dinheiro e à quantidade de dias ou palavaras para o destino ")
      break

  except ValueError:
    print("Insira valores válidos para os dados requisitados ")