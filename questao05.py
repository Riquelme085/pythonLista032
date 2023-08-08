#Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
#números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
#multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
#do primeiro pelo segundo número.

# solicita os números ao usuário

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))


# realiza os cálculos

soma = num1 + num2

subtracao1 = num1 - num2

subtracao2 = num2 - num1

multiplicacao = num1 * num2

divisao = num1 / num2

resto_divisao = num1 % num2


# exibe os resultados

print(f"A soma entre {num1} e {num2} é: {soma}")

print(f"A subtração de {num1} por {num2} é: {subtracao1}")

print(f"A subtração de {num2} por {num1} é: {subtracao2}")

print(f"A multiplicação entre {num1} e {num2} é: {multiplicacao}")

print(f"A divisão de {num1} por {num2} é: {divisao}")

print(f"O resto da divisão de {num1} por {num2} é: {resto_divisao}")