"""
Created on Sun Aug 18 16:29:21 2024

@author: gsanc
"""

def calcular_costo_queso_fresco(costo_leche: float, cantidad_leche: float, costos_adicionales: float) -> float:
    """
    Parameters
    ----------
    costo_leche : float
        costo de leche/litro.
    cantidad_leche : float
        litros de leche.
    costos_adicionales : float
        costos adicionales.

    Returns
    -------
    float
        costo de queso fresco en pesos redondeado a dos cifras
    """
    
    return round(costo_leche*cantidad_leche + costos_adicionales, 2)

def calcular_cantidad_queso(cantidad_leche: float) -> float:
    """
    Parameters
    ----------
    cantidad_leche : float
        cantidad de leche en litros.

    Returns
    -------
    float
        cantidad de queso en kg redondeado a dos cifras.
    """
    return round((cantidad_leche*1.03)/10, 2)

def calcular_dias_maduracion(cantidad_leche: float, temperatura_almacenamiento: float, humedad_relativa: float) -> int:
    """
    

    Parameters
    ----------
    cantidad_leche : float
        cantidad de leche.
    temperatura_almacenamiento : float
        temperatura.
    humedad_relativa : float
        humedad.

    Returns
    -------
    int
        calcula los dias de maduracion.

    """
    
    return round(5 + 0.1*(humedad_relativa*calcular_cantidad_queso(cantidad_leche))/temperatura_almacenamiento)

def calcular_costo_queso_madurado(costo_leche: float, cantidad_leche: float, costos_adicionales: float, costo_almacenamiento: float, temperatura_almacenamiento: float, humedad_relativa)-> float:
    """
    

    Parameters
    ----------
    costo_leche : float
        costo de la leche.
    cantidad_leche : float
        cantidad de la leche.
    costos_adicionales : float
        costos adicionales, trabajo, etc.
    costo_almacenamiento : float
        costo de almacenamiento.
    temperatura_almacenamiento : float
        temperatura .
    humedad_relativa : TYPE
        humedad.

    Returns
    -------
    float
        calcula el costo de todo el queso madurado.

    """
    return round(calcular_costo_queso_fresco(costo_leche, cantidad_leche, costos_adicionales) + costo_almacenamiento*calcular_dias_maduracion(cantidad_leche, temperatura_almacenamiento, humedad_relativa), 2)

def calcular_tamanio_porcion(angulo_corte: float) -> float:
    """
    

    Parameters
    ----------
    angulo_corte : float
        angulo de donde se corta con el cuchillo.

    Returns
    -------
    float
        calcula el tamaño de la porcion del queso.

    """
    return round((angulo_corte/360), 2)

def calcular_costo_porcion_madurado(costo_leche: float, cantidad_leche: float, costos_adicionales: float, costo_almacenamiento: float, temperatura_almacenamiento: float, humedad_relativa: float, angulo_corte: float) -> float:
    """
    

    Parameters
    ----------
    costo_leche : float
        costo de la leche.
    cantidad_leche : float
        cantidad de leche.
    costos_adicionales : float
        costos adicionales, trabajo, etc.
    costo_almacenamiento : float
        costo de almacenamiento.
    temperatura_almacenamiento : float
        temperatura.
    humedad_relativa : float
        humedad.
    angulo_corte : float
        angulo del cual se esta cortando.

    Returns
    -------
    float
        calcula el precio de LA PORCION de queso madurado.

    """
    return round(calcular_costo_queso_madurado(costo_leche, cantidad_leche, costos_adicionales, costo_almacenamiento, temperatura_almacenamiento, humedad_relativa) * calcular_tamanio_porcion(angulo_corte), 2)