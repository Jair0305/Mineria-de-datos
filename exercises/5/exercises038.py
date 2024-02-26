''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 38. Escribe un programa que pida una palabra al usuario y una definición para esa palabra, y devuelva un diccionario con todas las palabras y sus definiciones. Si el usuario entra una palabra que ya existe, mandar un mensaje de error.
'''

def main():
    diccionario ={}
    while True:
        palabra = input("Ingrese una palabra: ")
        if palabra == 'exit':
            break
        if palabra in diccionario:
            print("La palabra ya existe")
            continue
        definicion = input("Ingrese la definicion de la palabra: ")
        diccionario[palabra] = definicion

    print(diccionario)

if __name__ == "__main__":
    main()