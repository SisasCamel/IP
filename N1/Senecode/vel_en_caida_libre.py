# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:51:36 2024

@author: gsanc
"""
import math
def vel_en_caida_libre(altura: float)->float:
    """ Caída libre
    Parámetros:
      altura (float): Altura desde la cual cae el objeto
    Retorno:
      float: Velocidad del objeto al tocar el suelo tras la caída libre, la velocidad debe estar redondeada a dos
             cifras decimales.
    """
    return(round(math.sqrt(2*9.8*altura), 2))

print(vel_en_caida_libre(9.8))