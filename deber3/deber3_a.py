import random
import numpy as np

avion = []

#ocupados indicates that the criteria (last passenger reaches their seat) is fulfilled & vice versa

ocupados = 0 # indica que el asiento del ultimo pasajero esta lleno
desocupados = 0 # indica que el asiento del ultimo pasajero esta vacio
asientos = 100 # numero de asientos
iteraciones = 100000 # numero de iteraciones para encontrar la probabilidad (entre mayor es mas exacto, pero demora mas)

for i in range (1, (asientos+1)): # recorre el numero de asientos del avion
    avion.append(i) # agrega al array avion

def evaluar():    
    global avion
    global ocupados
    global desocupados

    # primer pasajero
    avion.remove(np.random.choice(avion))

    # siguentes pasajeros 
    for i in range (2, asientos):
        if i in avion: # si existe el asiento ocupado en el avion
            avion.remove(i) # ocupa el asiento con un valor dado
        else: # si no existe el asiento o el asiento esta vacio
            avion.remove(np.random.choice(avion)) # ocupa el asiento con un valor aleatorio

    if asientos in avion:
        ocupados += 1 # cuenta el numero de asientos ocupados
    else:
        desocupados += 1 # cuenta el numero de asientos desocupados

    avion = [] # vacia el array avion

    for i in range (1, (asientos + 1)):
        avion.append(i)

for i in range (0, iteraciones):
    evaluar()

probabilidad = ocupados/(ocupados+desocupados)*100

print("La probabilidad es del ", probabilidad)