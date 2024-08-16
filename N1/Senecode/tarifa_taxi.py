# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:29:32 2024

@author: gsanc
"""

def calcular_tarifa_taxi(kms_recorridos: float)->int:
    """ Tarifa de un taxi
    Parámetros:
      kms_recorridos (float): Kilómetros recorridos en el viaje
    Retorno:
      int: Tarifa a cobrar por el recorrido en taxi, la cual debe estar redondeada al entero mas cercano.
    """
    return(round(4000 + 82*(kms_recorridos*10)))

print(calcular_tarifa_taxi(1.5))