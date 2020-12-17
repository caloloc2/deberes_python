import math, random

def factorial(n):
    respuesta = 1
    for i in range(2, n+1):
        respuesta *= i
    return respuesta 

numero_personas = 3 # numero de personas en el elevador
pisos = 10 # numero de pisos

numero_posibles_combinaciones = pow((pisos-1), numero_personas) # posible numero de combinaciones para el resto de pisos sin contar el primero, y con el numero de personas en el elevador

posibilidades_botones = (pisos - numero_personas) * factorial(numero_personas) # hay 7 probabilidades de presionar 3 botones seguidos desde el segundo piso

probabilidad = posibilidades_botones / numero_posibles_combinaciones # probabilidad encontrada

print("Probabilidad de presionar los botones de 3 pisos consecutivos es de", probabilidad * 100)