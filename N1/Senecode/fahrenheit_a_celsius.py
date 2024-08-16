def fahrenheit_a_celsius(fahrenheit: float) -> float:
    
    '''
    Convierte una temperatura de Fahrenheit a Celsius y la retorna
    (Celsius = (Fahrenheit - 32) * 5/9))
    
    Parámetros:
        Fahrenheit (Float): la temperatura en Fº
    Retorna:
    (float): La temperatura en Cº
    '''
    return (fahrenheit-32)*(5/9)
print(fahrenheit_a_celsius(2))