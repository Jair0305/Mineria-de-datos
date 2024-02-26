''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 47. Escribe una función que reciba dos tuplas como parámetro, las cuales representan dos puntos en el espacio Euclidiano 2D, y que devuelva la distancia euclidiana entre esos puntos.
'''

import math

def distancia_euclidiana(punto1, punto2):
    # Desempaquetar las coordenadas de los puntos
    x1, y1 = punto1
    x2, y2 = punto2

    # Calcular la distancia euclidiana
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distancia

# Ejemplo de uso
punto_a = (1, 2)
punto_b = (4, 6)

resultado = distancia_euclidiana(punto_a, punto_b)
print(f"La distancia euclidiana entre {punto_a} y {punto_b} es: {resultado}")
