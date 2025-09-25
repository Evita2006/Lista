def modulo(a, b):
    """Devuelve el resto de la división entera a % b. Lanza ZeroDivisionError si b == 0."""
    a = int(a)
    b = int(b)
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a % b

def potencia(x, y):
    resultado = 1
    for _ in range(y):
        resultado *= x
    return resultado

def raiz_cuadrada_entera(x):
    if x < 0:
        raise ValueError('No existe raíz cuadrada entera para este valor')

    if x == 0 or x == 1:
        return x

    i = 1
    while i * i <= x:
        i += 1


    return i - 1

def sort_array(array):
    
    arr = array[:]  
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # intercambiar
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sum_elem_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

def sumar_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")

    resultado = []
    for i in range(len(a)):
        fila = []
        for j in range(len(a[0])):
            fila.append(a[i][j] + b[i][j])
        resultado.append(fila)

    return resultado

def pedir_recursos(nombre):
    cantidades = list(map(int, input(f"Ingresa las cantidades de {nombre} separadas por espacio: ").split()))
    cantidades.sort()
    total = sum(cantidades)
    return cantidades, total

def aplicar_subvencion(coste, subvencion):
    """Aplica subvención a los costes de construcción."""
    return sumar_matrices(coste, subvencion)

def calcular_coste_total(coste_unitario, cantidad):
    """Calcula el coste total multiplicando la matriz por la cantidad de construcciones."""
    return [[elem * cantidad for elem in fila] for fila in coste_unitario]

def calcular_tiempo_total(cantidades, tiempos, obreros):
    """
    tiempos: diccionario con tiempo (horas) que tarda un obrero en construir 1 estructura.
    cantidades: cuántas estructuras se van a construir.
    obreros: número total de obreros disponibles.
    """
    total_tiempo = 0
    detalle = {}

    for construccion, cantidad in cantidades.items():
        if cantidad == 0:
            continue
        tiempo_unitario = tiempos[construccion]
        tiempo_total_obra = tiempo_unitario * cantidad
        detalle[construccion] = tiempo_total_obra
        total_tiempo += tiempo_total_obra

    return total_tiempo, detalle


def simular_equilibrado(total_tiempo, obreros):
    """Simulación con los obreros repartidos equitativamente."""
    return total_tiempo / obreros


def simular_uno_por_obra(detalle, obreros):
    """Cada obra solo puede tener un obrero a la vez."""
    tiempo_max = 0
    for construccion, tiempo in detalle.items():
        tiempo_construccion = tiempo  # porque solo un obrero trabaja en ella
        if tiempo_construccion > tiempo_max:
            tiempo_max = tiempo_construccion
    return tiempo_max


def simular_en_parejas(detalle, obreros):
    """Los obreros trabajan de 2 en 2 en una construcción.

    Si no hay pares de obreros (obreros < 2), se devuelve el tiempo total sin reducción.
    """
    tiempo_total = 0
    for construccion, tiempo in detalle.items():
        # al ser de dos en dos, se reduce a la mitad el tiempo por estructura
        tiempo_total += tiempo / 2

    pares = max(1, obreros // 2)
    return tiempo_total / pares

