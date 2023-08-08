#Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
#programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.

print("Digite seu peso em quilos:")
peso = float(input())

print("Digite sua altura em metros:")
altura = float(input())

peso_em_gramas = peso * 1000
altura_em_centimetros = altura * 100

print("Seu peso em gramas é:", peso_em_gramas)
print("Sua altura em centímetros é:", altura_em_centimetros)
