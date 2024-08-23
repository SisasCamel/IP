# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:29:21 2024

@author: gsanc
"""
import cupi_quesos as c

costo_leche = float(input("Ingrese el costo de la leche: "))
cantidad_leche = float(input("Ingrese la cantidad de leche: "))
costos_adicionales = float(input("Ingrese los costos adicionales: "))

print(c.calcular_costo_queso_fresco(costo_leche, cantidad_leche, costos_adicionales))