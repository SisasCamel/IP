def encriptar_mensaje(mensaje: str)->str:
    """ Encriptador de mensajes
    Parámetros:
      mensaje (str): Mensaje que se debe encriptar
    Retorno:
      str: Mensaje encriptado siguiendo las reglas especificadas
    """
    if("cupi" in mensaje):
        mensaje = mensaje
    else:
        if("ae" in mensaje or "ai" in mensaje or "ao" in mensaje or "au" in mensaje):
            mensaje = mensaje.replace("a", "-")
        if("x" in mensaje):
            mensaje = "Cupi2" + mensaje.replace("x", "")
        if("i" not in mensaje):
            mensaje = mensaje.upper()
            mensaje = mensaje.replace("A", "V")
            mensaje = mensaje.replace("E", "V")
            mensaje = mensaje.replace("I", "V")
            mensaje = mensaje.replace("O", "V")
            mensaje = mensaje.replace("U", "V")
        if("seneca" in mensaje):
            mensaje = mensaje.swapcase()
    return mensaje
print(encriptar_mensaje("debemos tener cuidado con la aerodinamia"))