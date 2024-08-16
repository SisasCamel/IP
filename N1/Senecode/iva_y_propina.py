def calcular_iva_propina_total_factura(costo_factura: int)->str:
  iva = round((costo_factura * 19)/100)
  propina = round(costo_factura / 10)
 
  costo_total = round(costo_factura + propina + iva)
  
  return str(iva) + ',' + str(propina) + ',' + str(costo_total)

print(calcular_iva_propina_total_factura(57250))