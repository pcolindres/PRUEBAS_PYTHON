# Estructura de Control

#Implementar un programa que solicite al usuario ingresar un número.
#El programa debe determinar si el número es par o impar y repetir el proceso 
#hasta que el usuario ingrese un número negativo, utilizando estructuras de control.

def es_par(numero):
    return numero % 2 == 0

while True:
    numero = int(input("Ingrese un número (ingrese un número negativo para salir): "))
    
    if numero < 0:
        print("Saliendo del programa...")
        break
    
    if es_par(numero):
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")