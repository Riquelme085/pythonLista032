#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
#em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.

preco_custo = float(input("Digite o preço de custo do produto: "))

percentual_acrescimo = float(input("Digite o percentual de acréscimo: "))


acrescimo = preco_custo * percentual_acrescimo / 100

valor_venda = preco_custo + acrescimo


print(f"O valor de venda do produto é: R$ {valor_venda:.2f}")
