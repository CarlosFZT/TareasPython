#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Escribir un programa que lista los números cuadrados hasta un limite.
#Entrar el limite: 100
#Los números cuadrados son:
#    1
#    4
#    9
#    16
#    25
#    36
#    49
#    64
#    81
#    100

limite = int(raw_input('Entrar el limite:'))
cuadrado = 1
resultado = cuadrado * cuadrado

while resultado <= limite:
    print resultado
#    print 'El cuadrado de (%d) es (%d)' % (cuadrado,resultado++)
    cuadrado = cuadrado + 1 
    resultado = cuadrado * cuadrado        
    
#numero = limite que ingresa el usuario
# yo:  corrupto
# German:  cuadrado esta bien
#resultado igual esta bien
#tu condicion va a ser
#mientras limite (MENOR O IGUAL) a cuadrado:
#primero aumentas en 1 cuadrado
# yo:  osea q tengo q definir limite y darle valor 0
#corrupto
# German:  sino, te va a queda en 0
#y ahi vas
# yo:  yap
# German:  va a llegar un momento en q resultado va a ser mayor que cuadrado
#y es ahi donde el programa se va a salor
#salir
 #'yo:  corrupto
 
   



