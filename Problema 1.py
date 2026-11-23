# Estudiante: Maryluz Herrera Gómez
# Curso: Fundamentos de Programación - Fase 5
# Problema 1: Evaluación de compromiso de clientes
# Programa: Ing. en Inteligencia Artificial y Ciencia de Datos
# Grupo: 213022_279


# Función que evalúa la duración y los clics para devolver el nivel de compromiso
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


# Procedimiento para recorrer la matriz e imprimir el informe final
def mostrar_informe(matriz_sesiones):
    print("--- INFORME DE COMPROMISO DE CLIENTES ---")
    for fila in matriz_sesiones:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]

        nivel = clasificar_compromiso(duracion, clics)
        print(f"Cliente: {id_cliente} | Compromiso: {nivel}")


# Matriz de sesiones: [ID del Cliente, Duración (segundos), Número de clics]
sesiones = [
    ["C001", 210, 10],
    ["C002", 40, 4],
    ["C003", 130, 2],
    ["C004", 150, 5],
    ["C005", 180, 8],
    ["C006", 290, 14],
]

# Ejecución del programa
mostrar_informe(sesiones)