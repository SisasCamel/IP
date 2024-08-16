# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:37:19 2024

@author: gsanc
"""

def onzas_jugo(jugos: int)->float:
    """ Jugos de lulo
    Parámetros:
      jugos (int): Número de jugos de lulo en caja que hay en el gabinete de Cupitaller (N).
    Retorno:
      float: Onzas de jugo las cuales deben estar redondeadas a dos cifras decimales.
    """
    #1 caja = 1 L
    # 1 onza = 0.0296L
    return(round(jugos/0.0296, 2))