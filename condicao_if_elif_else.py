#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:00:21 2020

@author: mm
"""


idade =12
if idade<4:
	print("Sua entrada custa R$ 0.")
elif idade<=18:
    print("Sua entrada custa R$ 5.")
else:
    print("Sua entrada custa R$ 10.")
    
    
curso = "pos-graduaçao"
if curso =="graduaçao":
	data="8 de março"
elif curso =="pos-graduaçao":
  data = "22 de março"
elif curso =="extensao":
  data = "29 de março"
else:
  data = "05 de abril"

print("Suas aulas recomeçaram no dia " + data  + ".")



curso = "pos-graduacao"

if curso =="graduaçao":
	data="8 de março"

elif curso =="pos-graduaçao":
  data = "22 de março"

elif curso =="extensao":
  data = "29 de março"

elif curso =="MBA":
  data = "05 de abril"

else:
  data = ""

if data!= "":
	print("Suas aulas recomeçarão no dia " + data  + ".")
else:
    print("Erro! Curso inexistente!")
