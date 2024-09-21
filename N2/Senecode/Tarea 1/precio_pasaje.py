def calcular_precio_pasaje(temporada: str, compania: str, edad: int, estudiante: bool)->int:
    """ Precio de un Pasaje
    Parámetros:
      temporada (str): Cadena que indica la temporada, puede ser "ALTA" o "BAJA"
      compania (str): Cadena que indica la compañía con la que se hace el vuelo, puede ser "ALAS" o "VOLAR"
      edad (int): Edad del pasajero
      estudiante (bool): True en caso que el pasajero sea estudiante, False de lo Contrario
    Retorno:
      int: Precio calculado del pasaje Bogotá-Tokio según los parámetros
    """
    tarifa_final = 5_000_000
    if(compania == "ALAS"):  
      if(temporada == "ALTA"):
         tarifa_final *= 1.3
      if(edad<18):
         tarifa_final -= 5_000_000*0.5
      if(estudiante and edad >= 18 and temporada == "BAJA"):
         tarifa_final *= 0.9
    elif(compania == "VOLAR"):
      if(temporada == "ALTA") :
        tarifa_final = tarifa_final*1.2
      if(edad<18):
         tarifa_final -= 5_000_000*0.5
      if(edad>=60):
         tarifa_final += 100_000    
    return round(tarifa_final)
print(calcular_precio_pasaje("ALTA", "VOLAR", 17, False))