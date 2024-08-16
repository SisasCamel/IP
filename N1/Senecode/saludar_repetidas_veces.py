# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:42:28 2024

@author: gsanc
"""

def saludar_repetidas_veces(nombre: str, veces: int)->str:
    """ Saludo prolongado
    Parámetros:
      nombre (str): Nombre a incluir en el saludo
      veces (int): Cantidad de veces a repetir las letras
    Retorno:
      str: Cadena con el saludo con letras repetidas
    """
    return('H'+ 'o'*veces + 'l' + 'a'*(veces//2) + ' '+ nombre)