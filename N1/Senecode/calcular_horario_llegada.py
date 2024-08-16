def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int)->str:

    total_segundos = segundo_salida+duracion_segundos
    residuo_segundos = total_segundos % 60
    truncados_segundos = total_segundos // 60
    total_minutos = minuto_salida+duracion_minutos + truncados_segundos
    residuo_minutos = total_minutos % 60
    truncados_minutos = total_minutos // 60
    total_horas = (hora_salida+duracion_horas+truncados_minutos)%24

    return str(total_horas)+":"+str(residuo_minutos)+":"+str(residuo_segundos)

print(calcular_horario_llegada(23,56, 15, 2, 5, 51))
""" Hora de llegada de vuelo
    Parámetros:
      hora_salida (int): Hora de salida del vuelo (valor entre 0 y 23)
      minuto_salida (int): Minuto de salida del vuelo (valor entre 0 y 59)
      segundo_salida (int): Segundo de salida del vuelo (valor entre 0 y 59)
      duracion_horas (int): Número de horas que dura el vuelo
      duracion_minutos (int): Número de minutos (adicionales al número de horas) que dura el vuelo
      duracion_segundos (int): Número de segundos (adicionales al número de horas y minutos) que dura el
                               vuelo
    Retorno:
      str: Cadena que indica la hora de llegada del vuelo a su destino, la cadena debe estar con el formato
           “HH:mm:ss”.
"""