#A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
#pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
#prestações.


# Passo 1: Leia o valor da compra
valor_compra = float(input("Digite o valor da compra: "))

# Passo 2: Leia o número de prestações escolhidas
num_prestacoes = int(input("Digite o número de prestações escolhidas: "))

# Passo 3: Calcule o valor das prestações (valor da compra dividido pelo número de prestações)
valor_prestacao = valor_compra / num_prestacoes

# Passo 4: Exiba o valor das prestações
print("Valor das prestações: ", valor_prestacao)