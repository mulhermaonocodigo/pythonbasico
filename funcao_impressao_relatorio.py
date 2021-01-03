#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:46:00 2020

@author: mm
"""

#for usuario, series in favorita_serie_tv.items():
#    print(usuario.title(), " : ")	
#    for item_serie in series:
 
def imprime_relatorio(lista):
    for us, dados in usuarios.items():
        print("Nome:",dados[0])
        print("Endereço:",dados[1])
        print("Documento:",dados[2])
            
            
    

usuarios = {'joana':['Joana Vieira','Av. Curtilo, 234, Blumenal, SC','1223423-8']
,'karla':['karla magnolia','Rua B , 678, Rio Grande da Serra, SP','7889754-1']
,'miriam':['Miriam Vaconcelos','Rua Alegre, 212, Duque de Caxias, RJ','2288994-6']
,'joão pedro':['Joao Pedro Tibe','Travessa do Ouro, 3, Belém, PA', '9992267-0']
}
imprime_relatorio(usuarios)

