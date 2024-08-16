# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:45:53 2024

@author: gsanc
"""
import math
def area_poligono_regular(num_lados: int, longitud: float)->float:
    """ Área de un polígono regular
    Parámetros:
      num_lados (int): Número de lados del polígono
      longitud (float): Longitud de uno de los lados del polígono
    Retorno:
      float: Área del polígono regular redondeada a dos cifras decimales.
    """
    return(round((num_lados*longitud**2)/(4 * math.tan(3.1416/num_lados)), 2))