"""Calculo do Índice de Massa Corporal (IMC) """

from aritmetica import imc

"""
  Criando uma fórmula para calcular o IMC de uma pessoa
  com base nos parâmetros de peso e idade

  resultado esperado: dividir o peso por altura².
"""

sexo = input("Digite seu sexo: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

print(imc(imc, peso, altura))

