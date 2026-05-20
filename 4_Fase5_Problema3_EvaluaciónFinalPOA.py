'''
UNAD:       Universidad Nacional Abierta y a Distancia
ECBTI:      Escuela de Ciencias Básicas Tecnología e Ingeniería
Curso:      Fundamentos de Programación
Grupo:      213022_804
Programa:   Ingeniería de Sistemas


Actividad Fase 5 - Problema No. 3 - Evaluación Final POA
Autor: Luís Ángel Padilla Soto
Versión: 1.0
Fecha de Actualización: 20 de mayo de 2026
'''


# ------------------------------------------------------------------------------------------------------------------------------------------
# PROGRAMA:     Sistema de auditaría de inventario y toma de decisiones sobre qué artículos necesitan ser reabastecidos.
#
# DESCRIPCIÓN:  Este programa permite conocer y administrar el inventario de una tienda de equipos de cómputo y periféricos, utilizando 
#               estructuras de datos como matrices (listas) y funciones para calcular la cantidad a pedir, junto con estructuras de control
#               cíclicas y condicionales.
# ------------------------------------------------------------------------------------------------------------------------------------------


# Se declara la matriz [inventario] para listar los equipos y periféricos del inventario, donde cada fila representa un artículo con: código, nombre, stock actual y stock mínimo:
inventario = [
    [1, "Teclado", 100, 170],
    [2, "Mouse", 200, 450],
    [3, "Monitor", 50, 90],
    [4, "Impresora", 25, 25],
    [5, "Laptop", 250, 530],
    [6, "Desktop", 150, 350],
    [7, "Tablet", 30, 60],
    [8, "Disco Duro Externo", 75, 75]
]

# Se define la función [calcular_pedido()], para calcular la cantidad a pedir mediante una operación de resta entre el stock mínimo y el stock actual, y devuelve la cantidad a pedir o cero si el stock es suficiente:
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Se imprime la lista de pedidos para reabastecimiento, recorriendo la matriz [inventario] con un ciclo for, y utilizando la función [calcular_pedido()] para determinar la cantidad a pedir para cada artículo:
print("LISTA DE PEDIDOS PARA REABASTECIMIENTO\n")

# Se recorre la matriz [inventario] con un ciclo for, y se extraen los datos de cada artículo para calcular la cantidad a solicitar utilizando la función [calcular_pedido()], y se imprime el resultado:
for articulo in inventario:
    codigo = articulo[0] # Se extrae el código del artículo
    nombre = articulo[1] # Se extrae el nombre del artículo
    stock_actual = articulo[2] # Se extrae el stock actual del artículo
    stock_minimo = articulo[3] # Se extrae el stock mínimo del artículog

    # Se calcula la cantidad a solicitar utilizando la función [calcular_pedido()], entre el stock actual y el stock mínimo como argumentos, y se almacena el resultado en la variable [cantidad_solicitar]:
    cantidad_solicitar = calcular_pedido(stock_actual, stock_minimo) 

    print(f"Artículo: {nombre}")
    print(f"Código: {codigo}")
    print(f"Cantidad a solicitar: {cantidad_solicitar}")
    print("------------------------------")


"""
RESUMEN:
1. Se crea una matriz con 8 artículos disponibles, llamada [inventario].
2. La función [calcular_pedido()] determina cuánto se debe solicitar.
3. Si el stock actual es menor al mínimo, calcula la diferencia.
4. Si el stock es suficiente, devuelve cero [Ej.: el artículo "Impresora" y "Disco Duro Externo"].
5. Finalmente, se imprime la lista de reabastecimiento.
"""