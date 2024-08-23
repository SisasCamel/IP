# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:30:10 2024

@author: gsanc
"""

import cupi_quesos as c

cantidad_leche = float(input("Ingrese la cantidad de leche: "))
temperatura_almacenamiento = float(input("Ingrese la temperatura de almacenamiento: "))
humedad_relativa = float(input("Ingrese la humedad relativa: "))
print(c.calcular_dias_maduracion(cantidad_leche, temperatura_almacenamiento, humedad_relativa))