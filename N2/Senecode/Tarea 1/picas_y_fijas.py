def picas_y_fijas(numero_secreto: int, intento: int)->dict:
    """ Picas y Fijas
    Parámetros:
      numero_secreto (int): Número el cual se debe adivinar
      intento (int): Número el cual trata de adivinar
    Retorno:
      dict: Diccionario con las llaves "PICAS" y "FIJAS" que describe el resultado de la jugada.
    """
    picas = 0
    fijas = 0
    if(intento[0] == numero_secreto[0]):
        fijas += 1
    if(intento[1] == numero_secreto[1]):
        fijas += 1   
    if(intento[2] == numero_secreto[2]):
        fijas += 1
    if(intento[3] == numero_secreto[3]):
        fijas += 1
    if(intento[0] in numero_secreto):
        picas += 1
    if(intento[1] in numero_secreto):
        picas += 1
    if(intento[2] in numero_secreto):
        picas += 1
    if(intento[3] in numero_secreto):
        picas += 1
    return {"PICAS": picas - fijas, "FIJAS": fijas}
print(picas_y_fijas("1234", "1325"))