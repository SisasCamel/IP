# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:57:28 2024

@author: gsanc
"""

def convertir_eficiencia_combustible(millas_por_galon: float)->float:
    """ Eficiencia de combustible
    Parámetros:
      millas_por_galon (float): Eficiencia de combustible en millas por galón
    Retorno:
      float: Eficiencia de combustible en litros por 100 km con dos decimales.
    """
    # 1 Milla = 1.6km
    #1 Galon = 3.78 L
    #1 Milla / Galón = 1.6km/3.78L
    km = millas_por_galon*1.6
    reciproco = 3.78/km
    return(round(reciproco*100, 2))

print(convertir_eficiencia_combustible(25))