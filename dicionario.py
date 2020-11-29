#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:15:10 2020

@author: mm
"""

######-----------Exemplo 1

favorita_serie_tv = {'serie':'Star trek Discovery', 'plataforma':'Netflix', 'Gênero':'ficção-científica'}

print("Série favorita de Joana: ",favorita_serie_tv['serie'])

######-----------Exemplo 2

for serie_dados, dados in favorita_serie_tv.items():
    print(serie_dados.title() + " : " +dados.title() + ".")

######-----------Exemplo 3
favorita_serie_tv = {'joana':['Star trek Discovery','Vida incompleta','Coisa mais linda']
,'karla':['As five']
,'miriam':['Umbrella Academy']
,'joão pedro':['Abismo mágico','Aggrestsuko']
}

for usuario, series in favorita_serie_tv.items():
    print(usuario.title(), " : ")	
    for item_serie in series:
        print("\t" + item_serie.title())

