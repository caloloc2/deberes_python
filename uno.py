import random, math
import matplotlib.pyplot as plt

random.seed()

def obtener_parametros_circulo():    
    Cx = random.randint(4, 6)
    Cy = random.randint(4, 6)
    R = random.randint(1, 4)
    return Cx, Cy, R

def obtener_parametros_rectangulo():
    W = random.randint(1, 4)
    H = random.randint(1, 4)
    Ox = random.randint(0, 6)
    Oy = random.randint(0, 6)
    return W, H, Ox, Oy 

def generacion_puntos(cantidad):
    point_list = []
    for x in range(cantidad):
        x = random.uniform(0,10)
        y = random.uniform(0,10)
        
        point_list.append([x,y])

    return point_list

def dentro_circulo(punto):
    return math.sqrt((punto[0] - Cx)**2 + (punto[1] - Cy)**2) <= R

def dentro_rectangulo(punto):
    retorno = False
    
    if (((punto[0] > Ox) and (punto[0] < (Ox+W))) and ((punto[1] > Oy) and (punto[1] < (Oy+H)))):
        retorno = True
    
    return retorno

numero_puntos = 2500
Cx, Cy, R = obtener_parametros_circulo()
W, H, Ox, Oy = obtener_parametros_rectangulo()
puntos = generacion_puntos(numero_puntos)

fig, ax = plt.subplots()

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.grid(linestyle='--')

ax.set_aspect(1)

circulo = plt.Circle((Cx, Cy), R, edgecolor='r', facecolor='none')
rectangulo = plt.Rectangle((Ox, Oy), W, H, linewidth=1, edgecolor='b', facecolor='none')

ax.add_artist(circulo)
ax.add_artist(rectangulo)

puntos_area = []


for punto in puntos:    
    if (dentro_rectangulo(punto) and dentro_circulo(punto)):
        puntos_area.append(punto)        
        ax.add_artist(plt.Circle((punto[0], punto[1]), 0.03, edgecolor='g'))    
    else:
        ax.add_artist(plt.Circle((punto[0], punto[1]), 0.03, edgecolor='gray'))

n = len(puntos_area)
area = n / numero_puntos

plt.title('Area encontrada = '+str(area), fontsize=8)

plt.show()