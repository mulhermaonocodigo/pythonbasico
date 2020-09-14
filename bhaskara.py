#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:13:50 2020

@author: mm

#descricao: este programa calcula a fórmula de Báskara
"""

import numpy as np

#equação ax2+bx+c=0
a=1
b=5
c=4
delta = (b**2 - 4*a*c)
raiz_delta = np.sqrt(delta)
x_linha = (b.__neg__()  + raiz_delta)/(2*a) 
x_duaslinhas = (b.__neg__()  - raiz_delta)/(2*a)  


print("As raízes dessa equação são:" + str(x_linha) + " e " +str(x_duaslinhas))


