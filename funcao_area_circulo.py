#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:46:00 2020

@author: mm
"""
import numpy as np

def calcula_area_circulo(raio):
    area = np.pi * raio**2
    
    return area

raio_circ = float(input('Digite o valor do raio do circulo: '))
area_circulo = calcula_area_circulo(raio_circ)
print("A Área desse círculo em cm2 é: ",area_circulo)

