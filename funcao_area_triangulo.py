#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:46:00 2020

@author: mm
"""
import numpy as np

def calcula_area_triangulo(lado_a, lado_b, lado_c):
	p = (lado_a + lado_b + lado_c)/2
	area_triangulo = np.sqrt(p*(p-lado_a)*(p-lado_b)*(p-lado_c)	)
	return area_triangulo


a = float(input('Digite o tamanho do primeiro lado do triângulo em cm: '))
b = float(input('Digite o tamanho do segundo lado do triângulo em cm:' ))
c = float(input('Digite o tamanho do terceiro lado do triângulo em cm:' ))
area = calcula_area_triangulo(a,b,c)
print('A área desse triângulo em cm2 é: ',area)

