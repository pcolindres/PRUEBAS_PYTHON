#Programación Funcional en Python

#1) Implementa la funcion_principal aplicando principios de programación funcional
#como funciones puras e inmutabilidad.

#2) Implementa validaciones y maneja posibles errores en los datos.
#3) Utiliza funciones de orden superior como map, filter, y reduce.
#4) Realiza pruebas para asegurar que la función maneja diferentes casos correctamente.

def validar_edad(edad):
    if edad >= 18:
        return True
    else:
        raise ValueError("La edad debe ser mayor o igual a 18")

def validar_nombre(nombre):
    if nombre.isalpha():
        return True
    else:
        raise ValueError("El nombre solo puede contener letras")

def procesar_usuario(usuario):
    try:
        nombre_valido = validar_nombre(usuario['nombre'])
        edad_valida = validar_edad(usuario['edad'])
        return {'nombre': usuario['nombre'], 'edad': usuario['edad']}
    except ValueError as e:
        print(f"Error: {e}")
        return None

def funcion_principal(lista_usuarios):
    usuarios_validos = filter(lambda usuario: procesar_usuario(usuario) is not None, lista_usuarios)
    usuarios_procesados = map(procesar_usuario, usuarios_validos)
    return list(usuarios_procesados)

# Ejemplo de lista de usuarios
lista_usuarios = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'María', 'edad': 30},
    {'nombre': 'Pedro', 'edad': 15},
    {'nombre': 'Ana', 'edad': 20},
    {'nombre': '123', 'edad': 18}  # Usuario con nombre no válido
]

# Ejecutar la función principal
usuarios_procesados = funcion_principal(lista_usuarios)
print(usuarios_procesados)