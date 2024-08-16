def precio_minimo(p1: int, p2: int)->int:
    #ej. 7+10 = 17 (a+b)
    #(7-10) = -3 (a-b)
    #a+b -(b-a) = 2a, sucede cuando a es menor
    #
    #a+b-(a-b) = 2b, sucede cuando b es menor
    return ((p1+p2 - abs(p1-p2)) / 2)

print(precio_minimo(10,214))