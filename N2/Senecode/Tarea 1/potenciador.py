import math
def potenciador(x: int, n: int)->bool:
    """ Potenciador
    Parámetros:
      x (int): Número sospechoso como posible número elevado del número misterioso
      n (int): Potencia a la cual se debe elevar el número misterioso
    Retorno:
      bool: Valor booleano que indica si existe un número entero que elevado a la n, da como resultado x
    """
    existe_potenciador = False
    if(n == 1 or  n<= 0):
        existe_potenciador = False
    elif(int(f"{math.pow(x, 1/n): .0f}") == math.pow(x, 1/n)): #detectar si i^n = x
        existe_potenciador = True
    else:
        existe_potenciador = False
    return existe_potenciador

print(potenciador(16,3))
