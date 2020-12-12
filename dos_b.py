import math, random
import matplotlib.pyplot as plt


def aleatorio(max):
    return random.randint(1, max)

def combinatorio(n, k):
    return factorial(n)//(factorial(n-k)*factorial(k)) 

def factorial(n):
    respuesta = 1
    for i in range(2, n+1):
        respuesta *= i
    return respuesta 


n = 20 # numero de bolas
k = aleatorio(n) # numero de bolas sacadas

try:
    resp_a = combinatorio(n, k) / pow(n, k) # calcula la probabilidad
except OverflowError:
    resp_a = 0 # cuando la probabilidad tiende a cero

print("Probabilidad de que la secuencia sea estrictamente incremental :", resp_a)

j = aleatorio(k) # numero perteneciente a k y donde se verifica su secuencia

sumatoria = 1
for seq in range(j):
    sumatoria += combinatorio(n, seq) * combinatorio((k-1), (seq-1))    

try:
    resp_b = sumatoria / pow(n, k)
except OverflowError:
    resp_b = 0

print("Probabilidad de que la secuencia sea incremental :", resp_b)