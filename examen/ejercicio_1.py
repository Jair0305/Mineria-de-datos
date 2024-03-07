# -*- coding: utf-8 -*-
"""
Examen práctico 1
Autor: Chavez Islas Jair
Semestre: 2024-EJ
Curso: Minería de datos
Fecha: 2024-03-04
Descripción: Juego de los dados vs la computadora
"""
import random as rd


def tirar_dados(array_pc, array_pl):
    n1 = rd.randint(1, 6)
    if n1 == 1:
        array_pc.clear()  # Borra la lista si es que sale 1
    else:
        array_pc.append(n1)  # Agrega los elementos a la lista si NO sale 1, para guardar la secuencia

    n2 = rd.randint(1, 6)

    if n2 == 1:
        array_pl.clear()  # Borra la lista si sale 1
    else:
        array_pl.append(n2)

    print(f'Numero para el usuario : {n2}')
    print(f'Numero para la computadora : {n1}')

    print(f'Total de puntos para el usuario: {sum(array_pl)}')
    print(f'Total de puntos para la maquina: {sum(array_pc)}')

    return array_pc, array_pl  # Retorna los 2 arrays que recibe

def mensaje_perdedor(array_pl):
    print('*********************************\n* :( Perdiste ¡Inténtalo mejor! *\n*********************************')
    print(f'secuencia perdedora: {array_pl}')

def mensaje_ganador(array_pl):
    print('*********************************************\n* ¡¡Felicidades, has ganado la partida!! *\n*********************************************')
    print(f'secuencia perdedora: {array_pl}')

def iniciar_juego():
    while sum(array_pl) <= 30 and sum(array_pc) <= 30:
        dec = ''
        while dec != 'j' and dec != 'q':
            dec = input('Entra j para jugar o q para salir del juego: ')
            if dec.lower() == 'j':
                tirar_dados(array_pc, array_pl)
                if sum(array_pl) >= 30:
                    mensaje_ganador(array_pl)
                    return 's'
                if sum(array_pc) >= 30:
                    mensaje_perdedor(array_pl)
                    return 's'
            elif dec.lower() == 'q':
                print('************************\n* ¡¡Gracias por jugar! *\n************************')
                return 'n'
            else:
                print('¡Opción no válida!')
    return 's'

def volver_a_jugar():
    dec = input('¿Quieres volver a jugar? s/n:')
    if dec.lower() == 's':
        array_pc.clear()
        array_pl.clear()
        return 's'
    elif dec.lower() == 'n':
        print('************************\n* ¡¡Gracias por jugar! *\n************************')
        return 'n'
    else:
        print('¡Opción no válida!')
        return volver_a_jugar()

array_pc = []
array_pl = []

dec = 's'
while dec == 's':
    dec = iniciar_juego()
    if dec == 's':
        dec = volver_a_jugar()