#Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
#minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
#09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
#quantos minutos já se passaram desde às 00:00h deste dia.

# Recebendo valores das horas e minutos atuais do usuário

horas_atuais = int(input("Informe as horas atuais (formato 24 horas): "))

minutos_atuais = int(input("Informe os minutos atuais: "))


# Calculando a quantidade de minutos desde às 00:00h do dia

minutos_passados = (horas_atuais * 60) + minutos_atuais


# Exibindo o resultado

print("Desde às 00:00h deste dia, já se passaram", minutos_passados, "minutos.")