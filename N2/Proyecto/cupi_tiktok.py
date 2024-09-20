# -*- coding: utf-8 -*-
"""
CupiTikTok:

@author: Cupi2
"""


def construir_creador(
    nombre: str,
    pais: str,
    categorias: str,
    likes: int,
    vistas: int,
    seguidores: int,
    fecha_ultima_publicacion: int,
) -> dict:
    """
    Crea un diccionario con la información de un creador de contenido.

    Parámetros:
    nombre (str): Nombre del creador de contenido.
    pais (str): País de origen del creador de contenido.
    categorias (str): Categoría de los videos del creador de contenido.
    likes (int): Cantidad de likes que ha recibido el creador de contenido.
    vistas (int): Cantidad de vistas que ha recibido el creador de contenido.
    seguidores (int): Cantidad de seguidores que tiene el creador de contenido.
    fecha_ultima_publicacion (int): Fecha de la última publicación del creador
        de contenido en formato YYYYMMDD.

    Retorno:
    dict: Diccionario con la información del creador de contenido.
    """
    creador = {
        "nombre": nombre,
        "pais": pais,
        "categorias": categorias,
        "likes": likes,
        "vistas": vistas,
        "seguidores": seguidores,
        "fecha_ultima_publicacion": fecha_ultima_publicacion,
    }
    
    return creador


def buscar_creador_por_nombre(nombre: str, c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    """
    Busca si entre los creadores de contenido dados, hay uno con el nombre ingresado.

    Parámetros:
        nombre (str): Nombre del creador de contenido a buscar.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        dict: Diccionario del creador de contenido con el nombre ingresado por el usuario.
            Retorna None si no hay ningún creador con ese nombre. Si dos creadores
            o más tienen el mismo nombre, retorna el primero encontrado.
    """
    # TODO1: Implemente la función tal y como se describe en la documentación.
    creador = {}
    if(c1["nombre"] == nombre):
        creador = c1
    if(c2["nombre"] == nombre):
        creador = c2
    if(c3["nombre"] == nombre):
        creador = c3
    if(c4["nombre"] == nombre):
        creador = c4
    return creador


def filtrar_creadores_por_categoria(categoria: str, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Filtra a los creadores de contenido dados según la categoría ingresada.

    Parámetros:
        categoria (str): Categoría de interés para el usuario.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        str: Nombres de los creadores que hacen contenido de la categoría dada,
            separados por comas. Retorna None si no hay ningún creador que haga
            parte de la categoría de interés ingresada.
    """
    # TODO2: Implemente la función tal y como se describe en la documentación.
    resultados = ""
    creadores_encontrados = []
    if(categoria.lower() in c1["categorias"].lower()):
        creadores_encontrados.append(c1["nombre"])
    if(categoria.lower() in c2["categorias"].lower()):
        creadores_encontrados.append(c2["nombre"])
    if(categoria.lower() in c3["categorias"].lower()):
        creadores_encontrados.append(c3["nombre"])
    if(categoria.lower() in c4["categorias"].lower()):
        creadores_encontrados.append(c4["nombre"])
    resultados = ", ".join(creadores_encontrados)
    return resultados

def calcular_promedio_vistas(c1: dict, c2: dict, c3: dict, c4: dict) -> float:
    """
    Calcula el promedio de vistas de todos los creadores de contenido dados.

    Parámetros:
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        float: Promedio de vistas de todos los creadores de contenido dados,
            redondeado a dos cifras decimales.
    """
    # TODO3: Implemente la función tal y como se describe en la documentación.
    return round((c1["vistas"] + c2["vistas"] + c3["vistas"] +c4["vistas"]) / 4, 2)


def filtrar_creadores_por_vistas(minimo_vistas: int, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Filtra a los creadores de contenido dados que superen un mínimo de vistas (umbral).

    Parámetros:
        minimo_vistas (int): Umbral de vistas.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        str: Nombres de los creadores de contenido dados que superan el mínimo
            de vistas ingresado, separados por comas. Retorna el mensaje "Ninguno"
            si ningún creador de contenido supera el umbral.
    """
    # TODO4: Implemente la función tal y como se describe en la documentación.
    creadores_encontrados = []
    if( c1["vistas"] >= minimo_vistas):
        creadores_encontrados.append(c1{"nombre"})
    if(c2["vistas"] >= minimo_vistas):
        creadores_encontrados.append(c2{"nombre"}) 
    if(c3["vistas"] >= minimo_vistas):
        creadores_encontrados.append(c3{"nombre"})
    if(c4{"vistas"} >= minimo_vistas):
        creadores_encontrados.append(c4{"nombre"})
    return ", ".join(creadores_encontrados)


def calcular_rating_creador(creador: dict) -> float:
    """
    Calcula el rating de un creador de contenido con base en su número de
    seguidores, likes y vistas usando la fórmula F1.

    Parámetros:
        creador (dict): Diccionario que representa a un creador de contenido.

    Retorno:
        float: El rating del creador de contenido, redondeado a dos cifras
            decimales. Este valor se encuentra entre 0 y 100.
    """
    # TODO5: Implemente la función tal y como se describe en la documentación.
    pass


def calcular_puntaje_afinidad(creador: dict, categoria: str, minimo_rating: float, pais: str) -> float:
    """
    Calcula el puntaje de afinidad entre un creador de contenido y un
    usuario basándose en una categoría, un país y un rating mínimo dados.

    Parámetros:
        creador (dict): Diccionario que representa a un creador de contenido.
        categoria (str): Categoría de interés para el usuario.
        minimo_rating (float): Rating mínimo que debe tener el creador de contenido.
            Este valor se encuentra entre 0 y 100.
        pais (str): Nombre del país de interés para el usuario.

    Retorno:
        float: El puntaje de afinidad que tiene un creador con un usuario,
            redondeado a dos cifras decimales.
    """
    # TODO6: Implemente la función tal y como se describe en la documentación.
    pass


def buscar_creador_favorito(categoria: str, rating: float, pais: str, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Busca el creador de contenido con el mayor puntaje de afinidad, teniendo
        en cuenta la categoría, el país y un rating mínimo especificados.

    Parámetros:
        categoria (str): Categoría de interés para el usuario.
        rating (float): Rating mínimo que debe tener el creador de contenido.
        pais (str): Nombre del país de interés para el usuario.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        str: El nombre del creador de contenido con mayor puntaje de afinidad
            y su puntaje obtenido como sigue: "{nombre} con puntaje {puntaje_afinidad}",
            por ejemplo: "Code_Destroyer2002 con puntaje 100".
            Si dos creadores resultan con el mismo puntaje de afinidad, se retorna la
            información del que tenga el nombre alfabéticamente anterior/menor 
            (considerando el orden de sus caracteres en el abecedario). 
    """
    # TODO7: Implemente la función tal y como se describe en la documentación.
    pass


def buscar_creador_inactivo(fecha_de_referencia: int, c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    """
    Busca al creador de contenido que lleva el mayor tiempo sin publicar
        con base en una fecha ingresada por parámetro y la llave
        fecha_ultima_publicacion.

    Parámetros:
        fecha_de_referencia (int): Fecha con la que se busca hacer el análisis
            de actividad en formato YYYYMMDD.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        dict: Diccionario con las llaves: "nombre", "dias", "meses" y "anios",
            cuyos valores son respectivamente el nombre del creador más inactivo y 
            el tiempo de inactividad en años, meses y días.
            Si dos creadores tienen el mismo tiempo sin publicar, retorna el
            que tenga menos seguidores.
            Si la fecha ingresada es anterior a todas las fechas de última publicación,
            retorna None.
    """
    # TODO8: Implemente la función tal y como se describe en la documentación.
    # TIP: Puede usar una función auxiliar para calcular la cantidad de días
    #      que han pasado entre dos fechas.
    pass

