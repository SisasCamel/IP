# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:31:25 2024

@author: gsanc
"""
import cupi_quesos as c

costo_leche = float(input("Ingrese el costo de la leche: "))
cantidad_leche = float(input("Ingrese la cantidad de leche: "))
costos_adicionales = float(input("Ingrese los costos adicionales: "))
costo_almacenamiento = float(input("Ingrese el costo de almacenamiento: "))
temperatura_almacenamiento = float(input("Ingrese la temperatura de almacenamiento: "))
humedad_relativa = float(input("Ingrese la humedad relativa: "))

print(c.calcular_costo_queso_madurado(costo_leche, cantidad_leche, costos_adicionales, costo_almacenamiento, temperatura_almacenamiento, humedad_relativa))