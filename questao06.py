#Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
#ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
#exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
#do mês.

# Passo 1: Leia o nome do vendedor
nome_vendedor = input("Digite o nome do vendedor: ")

# Passo 2: Leia o salário fixo do vendedor
salario_fixo = float(input("Digite o salário fixo do vendedor: "))

# Passo 3: Leia o total de vendas efetuadas pelo vendedor
total_vendas = float(input("Digite o total de vendas efetuadas: "))

# Passo 4: Calcule a comissão do vendedor (15% sobre o total de vendas)
comissao = total_vendas * 0.15

# Passo 5: Calcule o salário completo do vendedor (salário fixo + comissão)
salario_completo = salario_fixo + comissao

# Passo 6: Exiba o nome do vendedor, o salário fixo, a comissão e o salário completo
print("Nome do vendedor: ", nome_vendedor)
print("Salário fixo: ", salario_fixo)
print("Comissão: ", comissao)
print("Salário completo: ", salario_completo)
