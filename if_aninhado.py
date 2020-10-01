#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:22:50 2020

@author: mm
"""

preco =0.00

pizza = "muçarela"

ingrediente_extra =True
num_ingredientes_extra = 3
borda_recheada = True 


if pizza == "muçarela" :
     preco = 25.50
	
     if num_ingredientes_extra > 0:
         preco = preco + num_ingredientes_extra*3.00
         if borda_recheada == True:
             preco = preco + 4.00


print("O preço final da pizza é de: ", preco )
