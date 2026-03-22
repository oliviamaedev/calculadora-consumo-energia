aparelho = input("digite o nome do aparelho: ")
potencia = float(input("digite a potencia do aparelho em watts: "))
horasDia = float(input("digite o numero de horas que o aparelho fica ligado por dia: "))

consumoMensal = (potencia * horasDia * 30) / 1000
print(f"O consumo mensal do aparelho {aparelho} é de: {consumoMensal:.2f} KWh por mês")
custoMensal = consumoMensal * 0.70 # valor médio dos watts em reais em São Paulo no ano de 2026
print(f"O custo mensal do aparelho {aparelho} é de: R$ {custoMensal:.2f}")