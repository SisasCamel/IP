def despacho_buses(personas_bus: int, personas_estacion: int)->bool:
    """ La estación de Transmilenio
    Parámetros:
      personas_bus (int): Número de personas en el bus que va a detenerse
      personas_estacion (int): Número de personas esperando el bus en la estación
    Retorno:
      bool: Retorna el valor True si se debe despachar un bus nuevo y retorna False de lo contrario.
    """
    debe_salir_bus = False
    if(personas_bus >= 150):
        debe_salir_bus = True
    elif(personas_estacion+personas_bus >= 150 and personas_estacion > 40):
        debe_salir_bus = True

    return debe_salir_bus
