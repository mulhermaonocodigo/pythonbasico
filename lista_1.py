#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:29:45 2020

@author: mm
"""
frutas = ['maçã','banana','manga']

print(frutas[:])

print(frutas[0])

print(frutas[1])

print(frutas[2])

#último elemento
print(frutas[-1])


if "maçã" in frutas:
    print("Sim, 'maçã' está na lista de frutas")

#---------------------------------------------------
cores = []

cores.append('amarelo')
cores.append('azul')
cores.append('vermelho')
cores.append('verde')
cores.append('rosa')

print('As cores selecionadas foram:',cores[:])


#---------------------------------------------------
list_numeros = list(range(1,6))

print(list_numeros)


#---------------------------------------------------
numeros = [1,2,3,4,5,6,7,8]

print(numeros)


#---------------------------------------------------

variado = ['amarelo',2,3,4,5,6,7,8]

print(variado)