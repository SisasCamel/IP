# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:23:49 2024

@author: gsanc
"""

def calcular_BMI(peso_lb: float, altura_inch: float)->float:
    """ Índice de masa corporal
    Parámetros:
      peso_lb (float): Peso en libras de la persona
      altura_inch (float): Altura en pulgadas de la persona
    Retorno:
      float: Índice de masa corporal de la persona, el valor de retorno debe estar redondeado a dos decimales.
    """
    #BMI = kg/m ** 2
    #1lb = 0.45kg
    #1in = 0.025m
    
    return(round((peso_lb*0.45)/((altura_inch*0.025)**2),2))

print(calcular_BMI(140, 80))