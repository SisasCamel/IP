def estado_academico(nota1: float, creditos1: int, nota2: float, creditos2: int, nota3: float, creditos3: int, nota4: float, creditos4: int, nota5: float, creditos5: int, nota6: float, creditos6: int)->str:
    """ Estado académico
    Parámetros:
      nota1 (float): Nota del curso 1 (entre 0 y 5.0)
      creditos1 (int): La cantidad de créditos asignados al curso 1
      nota2 (float): Nota del curso 2 (entre 0 y 5.0)
      creditos2 (int): La cantidad de créditos asignados al curso 2
      nota3 (float): Nota del curso 3 (entre 0 y 5.0)
      creditos3 (int): La cantidad de créditos asignados al curso 3
      nota4 (float): Nota del curso 4 (entre 0 y 5.0)
      creditos4 (int): La cantidad de créditos asignados al curso 4
      nota5 (float): Nota del curso 5 (entre 0 y 5.0)
      creditos5 (int): La cantidad de créditos asignados al curso 5
      nota6 (float): Nota del curso 6 (entre 0 y 5.0)
      creditos6 (int): La cantidad de créditos asignados al curso 6
    Retorno:
      str: Estado académico del estudiante según su promedio ('SUSPENDIDO', 'PRUEBA' o 'NORMAL')
    """
    promedio = (nota1*creditos1 + nota2*creditos2+ nota3*creditos3+ nota4*creditos4+ nota5*creditos5+ nota6*creditos6)/(creditos1+creditos2+creditos3+creditos4+creditos5+creditos6)  
    
    estado_academico = ""

    if(round(promedio,2) < 3.0):
        estado_academico = "SUSPENDIDO"
    elif(round(promedio,2) >= 3.0 and promedio < 3.25):
        estado_academico = "PRUEBA"
    elif(round(promedio,2) >= 3.25):
        estado_academico = "NORMAL"
    return estado_academico
