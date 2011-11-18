#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Adivina el número! 50
#Demasiado grande.

#Adivina el número! 40
#Demasiado pequeño.

#Adivina el número! 48
#Demasiado pequeño.

#Adivina el número! 49
#Correcto! Necesitabas 4 pruebas.

import random

respuesta = random.randint(1, 10)

numero = 0

pruebas = 0

while numero != respuesta:

    numero = int(raw_input('Adivina el nummero!'))
    
    pruebas = pruebas + 1
      
    if numero < respuesta:
        print 'Demasiado pequeño.'

    if numero > respuesta:
        print 'Demasiado grande.'

    if numero == respuesta:
        print 'Correcto!, Necesitaba %d Pruebas' % (pruebas)





