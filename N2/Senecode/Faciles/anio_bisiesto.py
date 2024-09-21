import doctest

def determinar_bisiesto(year: int) -> bool:
    '''determina si un año es bisiesto o no

    Args:
        year (int): years en ingles

    Returns:
        bool: retorna si es bisiesto o no

    >>> determinar_bisiesto(1500)
    False
    >>> determinar_bisiesto(2000)
    True
    >>> determinar_bisiesto(2020)
    True
    '''    
    if(year%100 == 0 and year%400 != 0):
        return False
    elif(year%4 == 0):
        return True
    else:
        return False
    

doctest.testmod(name='determinar_bisiesto', verbose=True)