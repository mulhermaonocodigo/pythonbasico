#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:19:14 2020

@author: mm

descrição: este programa realiza operações de soma,  multiplicação,  divisão e subtração
"""

print("Operação SOMA:")

valor_a = float(input('Entre com o 1º valor: '))

valor_b = float(input('Entre com o 2º valor: '))

resultado_soma = valor_a + valor_b

print("A soma é: "+ str(resultado_soma))

#multiplicação
print("Operação MULTIPLICAÇÃO:\n")

valor_c = float(input('Entre com o 1º valor: '))

valor_d = float(input('Entre com o 2º valor: '))

resultado_multiplicacao = valor_c * valor_d

print("A multiplicação é: "+ str(resultado_multiplicacao))
#divisão

print("Operação DIVISÃO:\n")

valor_e = float(input('Entre com o 1º valor: '))

valor_f = float(input('Entre com o 2º valor: '))


resultado_divisao = valor_e / valor_f

print("A divisão é: "+str(resultado_divisao))

#subtração

print("Operação SUBTRAÇÃO:\n")

valor_g = float(input('Entre com o 1º valor: '))

valor_h = float(input('Entre com o 2º valor: '))


resultado_subtracao = valor_g - valor_h

print("A  subtração é: "+str(resultado_subtracao))
