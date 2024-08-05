# Primera forma de importar una librería
# Esta forma importa absolutamente todas las funciones de la librería random, sobrecargando un poco más el programa
import random as rd

# Segunda forma de importar la librería
# Esta forma solo llamará específicamente a la función randint, siendo más óptima para el programa
# from random import randint as ri 

import matplotlib.pyplot as plt

# pip install matplotlib (Este comando se usa en la terminal, no dentro del script)

# Crear un arreglo unidimensional (vector) con 10 elementos inicializados a 0
x = [0] * 10
print("Vector inicial x:", x)

# En Python no existe menor o igual o mayor o igual (Nota: esto es incorrecto, Python sí soporta <= y >=)

print("Llenando el vector x con números aleatorios usando un bucle for")
for i in range(10):
    x[i] = rd.randint(1, 10)  # Esta forma utiliza la primera forma de importar
    # x[i] = ri(1, 10)  # Esta forma utiliza la segunda forma de importar

# Segunda forma simplificada de cargar un vector
print("Llenando el vector y con números aleatorios usando una comprensión de listas")
y = [rd.randint(1, 10) for _ in range(10)]

print("Vector x:", x)
print("Vector y:", y)

# Graficar los vectores x e y
# Esto significa puntos en un gráfico de dispersión
#grafico de puntos
plt.scatter(x, y)
#grafico lineales
plt.scatter(x, y)
#graficos de barra
plt.plot(x, y)
plt.title('Gráfico de dispersión de x y y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
