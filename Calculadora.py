#  Calculadora de Promedio de Notas

# Implementa la función calcular_promedio que tome una lista de notas y devuelva su promedio.
# Permite al usuario ingresar notas (pueden ser números flotantes) una por una.
#El usuario deberá indicar cuándo ha terminado de ingresar notas 
#(puede ser ingresando un valor específico, como -1).
#Calcula el promedio de las notas ingresadas utilizando la función calcular_promedio.
#Imprime el promedio calculado.

def calcular_promedio(notas):
    total = sum(notas)
    cantidad = len(notas)
    if cantidad == 0:
        return 0
    else:
        return total / cantidad

def ingresar_notas():
    notas = []
    while True:
        nota_str = input("Ingrese una nota (o ingrese -1 para terminar): ")
        if nota_str == "-1":
            break
        try:
            nota = float(nota_str)
            notas.append(nota)
        except ValueError:
            print("Por favor ingrese un número válido.")

    return notas

def main():
    print("Calculadora de Promedio de Notas")
    print("Ingrese las notas una por una. Ingrese -1 cuando haya terminado.")

    notas = ingresar_notas()

    promedio = calcular_promedio(notas)

    print("El promedio de las notas ingresadas es:", promedio)

if __name__ == "__main__":
    main()



 