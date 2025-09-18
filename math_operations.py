def modulo(a, b):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    division = a // b
    mult = division * b
    subs = a - mult
    print("The remainder is: ", subs)
    return subs

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
