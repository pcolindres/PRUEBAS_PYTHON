#Revisión de Funciones y Estructuras de Datos

#1)Implementa la función analizar_datos que acepte una lista de datos y realice varias operaciones,
#como clasificación o análisis estadístico.
#2)Asegúrate de validar los datos ingresados. Si no son válidos, maneja estos casos adecuadamente.
#3)La función debe ser capaz de manejar listas vacías o datos no numéricos.
#4)Prueba la función con diferentes conjuntos de datos.

import statistics

def analizar_datos(datos):
    if not datos:
        return "La lista de datos está vacía"

    try:
        datos_numericos = [float(dato) for dato in datos]
    except ValueError:
        return "La lista de datos contiene valores no numéricos"

    cantidad_datos = len(datos_numericos)
    suma = sum(datos_numericos)
    promedio = suma / cantidad_datos
    mediana = statistics.median(datos_numericos)
    maximo = max(datos_numericos)
    minimo = min(datos_numericos)

    return {
        "cantidad_datos": cantidad_datos,
        "suma": suma,
        "promedio": promedio,
        "mediana": mediana,
        "maximo": maximo,
        "minimo": minimo
    }

# Prueba de la función con diferentes conjuntos de datos
datos1 = [1, 2, 3, 4, 5]
print(analizar_datos(datos1))

datos2 = [10, 20, 'a', 30, 40]  # datos no numéricos
print(analizar_datos(datos2))

datos3 = []  # lista vacía
print(analizar_datos(datos3))

datos4 = ['a', 'b', 'c']  # lista vacía
print(analizar_datos(datos4))