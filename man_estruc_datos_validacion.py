#Manipulación de Estructuras de Datos con Validaciones
#1)Implementa la función realizar_operaciones_con_lista que acepte una lista de números
#y realice operaciones como calcular el máximo, mínimo, y promedio.
#2) Asegúrate de validar los datos ingresados por el usuario. Si no son números válidos,
#   pide al usuario que los reingrese.
#3) La función debe manejar casos especiales, como listas vacías, y proporcionar mensajes de error claros.
#4) Después de ingresar los números, llama a la función y muestra los resultados de las operaciones.

def realizar_operaciones_con_lista(lista):
    if not lista:
        print("La lista está vacía. No se pueden realizar operaciones.")
        return

    numeros = []
    for item in lista:
        while True:
            try:
                numero = float(item)
                numeros.append(numero)
                break
            except ValueError:
                print(f"El valor '{item}' no es un número válido. Inténtalo de nuevo.")
                item = input("Ingrese un número válido: ")

    if not numeros:
        print("No se ingresaron números válidos. No se pueden realizar operaciones.")
        return

    maximo = max(numeros)
    minimo = min(numeros)
    promedio = sum(numeros) / len(numeros)

    print("Operaciones realizadas con éxito:")
    print(f"Valor máximo: {maximo}")
    print(f"Valor mínimo: {minimo}")
    print(f"Promedio: {promedio}")


# Ejemplo de uso:
lista_numeros = input("Ingrese una lista de números separados por espacios: ").split()
realizar_operaciones_con_lista(lista_numeros)