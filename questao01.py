#1) Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
#valor com o acréscimo dos 10% da gorjeta do garçom

valor_conta = float(input("Digite o valor da conta: "))
gorjeta = valor_conta * 0.1
valor_total = valor_conta + gorjeta

print(f"O valor total a ser pago é R${valor_total:.2f}")
