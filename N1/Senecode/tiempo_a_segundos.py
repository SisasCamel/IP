# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:34:19 2024

@author: gsanc
"""

def tiempo_a_segundos(dias: int, horas: int, mins: int, seg: int)->int:
    """ Unidades de tiempo a segundos
    Parámetros:
      dias (int): Número de dias del periodo de tiempo
      horas (int): Número de horas del periodo de tiempo
      mins (int): Número de minutos del periodo de tiempo
      seg (int): Número de segundos del periodo de tiempo
    Retorno:
      int: Número de segundos al que equivale el periodo de tiempo dado como parámetro
    """
    return(dias*86400 + horas*3600 + mins*60 + seg)

print(tiempo_a_segundos(1, 2, 15, 14))