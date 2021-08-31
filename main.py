"""Construindo a chamada super calculadora"""
from aritmetica import soma, divisao


valor1 = int(input("Digite valor 1: "))

operacao = input("Qual a operacao +:Soma -:Subtracao *:Multiplicacao /:Divisao ")

valor2 = int(input("Digite valor 2: "))

if operacao == "+":
    print(soma(valor1, valor2))
elif operacao == "/":
    print(divisao(valor1, valor2))
