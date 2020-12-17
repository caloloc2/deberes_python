import random, math
import matplotlib.pyplot as plt

random.seed()

def obtener_parametros_circulo():
    # genera numeros aleatorios para el centro y el radio del circulo entre los limites establecidos
    Cx = random.randint(4, 6) # centro en x
    Cy = random.randint(4, 6) # centro en y
    R = random.randint(1, 4) # radio
    return Cx, Cy, R # retorna valores

def obtener_parametros_rectangulo():
    # genera numeros aleatorios para obtener la posicion inicial, ancho y alto del rectangulo
    W = random.randint(1, 4) # ancho de rectangulo
    H = random.randint(1, 4) # alto de rectangulo
    Ox = random.randint(0, 6) # origen en x
    Oy = random.randint(0, 6) # origen en y
    return W, H, Ox, Oy # retorna valores

def generacion_puntos(cantidad):
    # genera puntos aleatorios en toda el area
    lista_puntos = [] # array de puntos
    for x in range(cantidad): # itera en numero asignado
        x = random.uniform(0,10) # obtiene punto en x
        y = random.uniform(0,10) # obtiene punto en y
        
        lista_puntos.append([x,y]) # agrega a array de puntos

    return lista_puntos # retorna array

def dentro_circulo(punto):
    # determina si un punto se encuentra dentro del circulo con sus parametros
    return math.sqrt((punto[0] - Cx)**2 + (punto[1] - Cy)**2) <= R

def dentro_rectangulo(punto):
    # determina si un punto se encuentra dentro de un rectangulo
    retorno = False # variable de retorno
    
    # si en punto en x se encuentra dentro del origen y el ancho, y el punto en y se encuentra dentro del origen y el alto
    if (((punto[0] > Ox) and (punto[0] < (Ox+W))) and ((punto[1] > Oy) and (punto[1] < (Oy+H)))):
        retorno = True # si cumple la condicion setea como verdadero
    
    return retorno # retorna valor

numero_puntos = 2500
Cx, Cy, R = obtener_parametros_circulo() # obtiene parametros de circulo
W, H, Ox, Oy = obtener_parametros_rectangulo() # obtiene parametros de rectangulo
puntos = generacion_puntos(numero_puntos) # genera puntos dentro del area

fig, ax = plt.subplots() # crea cuadro para grafica

plt.xlim(0, 10) # limites de la grafica en x
plt.ylim(0, 10) # limites de la grafica en y
plt.grid(linestyle='--') # setea linea cortada para ejes
ax.set_aspect(1) # aspecto cuadrado de grafica

circulo = plt.Circle((Cx, Cy), R, edgecolor='r', facecolor='none') # grafica el circulo
rectangulo = plt.Rectangle((Ox, Oy), W, H, linewidth=1, edgecolor='b', facecolor='none') # grafica el rectangulo

puntos_area = [] # array de puntos en area de interseccion
for punto in puntos: # recorre todos los puntos generados
    if (dentro_rectangulo(punto) and dentro_circulo(punto)): # si cumple las dos condiciones => se encuentra dentro del area de interseccion
        puntos_area.append(punto) # agrega punto al array de puntos
        ax.add_artist(plt.Circle((punto[0], punto[1]), 0.03, edgecolor='g')) # grafica punto en el area de interseccion en verde
    else: # si no cumple condicion => no esta dentro del area de interseccion
        ax.add_artist(plt.Circle((punto[0], punto[1]), 0.03, edgecolor='gray'))  # grafica punto en el area de interseccion en gris

ax.add_artist(circulo) # agrega grafica al cuadro
ax.add_artist(rectangulo) # agrega grafica al cuadro

area = 0
n = len(puntos_area) # numero total de puntos dentro del area de interseccion
area = (n/ numero_puntos) * 100 # calcula el area a partir del numero de puntos dentro del area de interseccion con el total de puntos generados

plt.title('Area encontrada = '+str(area)+ " u", fontsize=8) # agrega un titulo a la grafica

plt.show() # muestra la grafica