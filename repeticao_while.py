#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:52:51 2020

@author: maysa
"""



lista_frutas = ['maça', 'banana', 'manga']
f=0
while f < len(lista_frutas):
	print(lista_frutas[f] , 'foi adicionada 	à lista.\n\n')	
	f = f+1

#----------------------

lista_recheio =[]
limite_numero_recheios = 3

print("Você pode escolher ", limite_numero_recheios, "recheios.")

i=0
while  i < limite_numero_recheios :

    input_recheio = input('Entre com o '+str(i+1)+'o.    	 recheio: ')
    lista_recheio.append(input_recheio)
    i=i+1

print("Você escolheu esses recheios:",lista_recheio[:])

#-____________________________________________________________________________--------
    
lista_recheio =[]

print("\n\nVocê pode escolher quantos recheios quiser.")

continuar = True 
while  continuar == True:

    input_recheio = input('Entre com um recheio: ')
    lista_recheio.append(input_recheio)
    input_continuar = input('Deseja informar mais algum recheio? Informe NAO para parar e qualquer outra palavra para continuar: ')
    if input_continuar == 'NAO':
        continuar = False

print("Você escolheu esses recheios:",
lista_recheio[:])
