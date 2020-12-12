import time
import random, math
import matplotlib.pyplot as plt

random.seed()

def numero_dado():
    return random.randint(1, 6)

n = 2 # numero de lanzadas
prob = 1
for x in range(n):
    numero = numero_dado()
    print("Dado : ", numero)
    prob = prob * numero/6 # probabilidad de que salga un numero en una lanzada

print("Probabilidad de que no salga al menos un numero en "+str(n)+" lanzadas es ", 1 - prob)