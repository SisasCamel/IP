# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:39:57 2024

@author: gsanc
"""

def altura_en_mts(pies: int, pulgadas: int)->float:
    """ Altura de una persona
    Parámetros:
      pies (int): Número de pies que componen la altura de la persona
      pulgadas (int): Número de pulgadas que componen la altura de la persona
    Retorno:
      float: Altura de la persona en metros, la cual debe estar redondeada a dos cifras decimales.
    """
    pies_a_metros = pies*0.0254*12 #12 Pulgadas = 1 Pies
                                    #1 Pulgada * 12 = 0.0254m *12 
    pulgadas_a_metros = pulgadas * 0.0254
    return round(pies_a_metros+pulgadas_a_metros, 2)
