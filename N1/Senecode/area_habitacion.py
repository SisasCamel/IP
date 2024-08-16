# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:48:46 2024

@author: gsanc
"""

def area_habitacion(largo: float, ancho: float)->float:
    """ Área de una habitación
    Parámetros:
      largo (float): Largo de la habitación
      ancho (float): Ancho de la habitación
    Retorno:
      float: Número (float) que representa el área de la habitación redondeada con dos decimales.
    """
    return(round(largo*ancho, 2))

print(area_habitacion(2.6, 4.23))