# Función Operación Matemática
#Implementa la función calcular_operacion que acepte dos números 
#y una cadena que representa la operación matemática (por ejemplo, "suma", "resta", "multiplicación", "división").
#La función debe verificar si la operación es válida y realizar la operación correspondiente.
#En caso de recibir una operación no válida o un error en los cálculos (como división por cero),
#la función debe manejar estos casos adecuadamente.
#Prueba la función con varios ejemplos para asegurar su correcto funcionamiento.

def calcular_operacion(num1, num2, operacion):
    try:
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicación":
            resultado = num1 * num2
        elif operacion == "división":
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            resultado = num1 / num2
        else:
            raise ValueError("Operación no válida")
        return resultado
    except ZeroDivisionError as e:
        return str(e)
    except ValueError as e:
        return str(e)

# Pruebas
print(calcular_operacion(5, 3, "suma"))  # Resultado esperado: 8
print(calcular_operacion(10, 4, "resta"))  # Resultado esperado: 6
print(calcular_operacion(6, 2, "multiplicación"))  # Resultado esperado: 12
print(calcular_operacion(8, 0, "división"))  # Resultado esperado: "No se puede dividir por cero"
print(calcular_operacion(8, 2, "potencia"))  # Resultado esperado: "Operación no válida"