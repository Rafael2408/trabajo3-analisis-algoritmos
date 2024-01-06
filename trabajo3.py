import random

def fill_random_list(list):
    for i in range(len(list)):
        list[i] = random.randint(1, 100)

def plus_elements_array(list, i, plus=0):
    if i < 0:
        return plus
    plus += list[i]
    return plus_elements_array(list, i-1, plus)

def exercise1():
    print("\nEjecutando el ejercicio 1...")
    size = int(input("Introduzca el tamaño del arreglo: "))
    list = [0] * size
    fill_random_list(list)
    print("Lista aleatoria: \n", list)
    print(f'La suma de los elementos del arreglo es: {plus_elements_array(list, len(list)-1)}')
    

def get_largest_number(list, i, number):
    if i < 0:
        return number
    if list[i] > number:
        number = list[i]
    return get_largest_number(list, i-1, number)

def exercise2():
    print("\nEjecutando el ejercicio 2...")
    size = int(input("Introduzca el tamaño del arreglo: "))
    list = [0] * size
    fill_random_list(list)
    print("Lista aleatoria: \n", list)
    print(f'El número mayor de la lista es: {get_largest_number(list, len(list)-1, list[-1])}')
    
    
def plus_multiple_digits(A, multiple, i, B = None):
    if B is None:
        B = []
    if(i<0):
        return B
    sum = 0
    for digit in str(A[i]):
        if int(digit) % multiple == 0:
            sum += int(digit)
    B.append(sum)
    return plus_multiple_digits(A, multiple, i-1, B)
    
def exercise3():
    print("\nEjecutando el ejercicio 3...")
    size = int(input("Introduzca el tamaño del arreglo: "))
    list = [0] * size
    fill_random_list(list)
    print("Lista aleatoria: \n", list)
    
    multiple = int(input("Ingrese un número para que sea múltiplo: "))
    list_multiple = plus_multiple_digits(list, multiple, size-1)
    list_multiple.reverse()
    print(f'La suma de los digitos multiplos de {multiple} es: {list_multiple}')
    
    
def print_matrix_recursive(matrix, row):
    if row == -1:
        return
    print(*matrix[len(matrix)-row-1],sep="\t",end="\n\n")
    print_matrix_recursive(matrix, row - 1)

def is_symmetric_matrix(matrix, i, j):
    if j < 0:
        j = len(matrix[0])-1
        i -= 1
    if i < 0:
        return True
    
    if len(matrix) != len(matrix[0]):
        return False
    if matrix[i][j] != matrix[j][i]:
        return False
    
    return is_symmetric_matrix(matrix, i, j-1)

def exercise4():
    print("\nEjecutando el ejercicio 4...")
    matrix = [[1, 2, 3],
              [2, 3, 5],
              [3, 5, 6]]
    print("Matriz:")
    print_matrix_recursive(matrix, len(matrix)-1)
    print(f'La matriz es simétrica: {is_symmetric_matrix(matrix, len(matrix)-1, len(matrix[0])-1)}')
    
    
def fill_random_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = random.randint(1, 100)

def plus_odd_rows(matrix, i, list_plus = []):
    if i < 0 or i == 0:
        return list_plus
    if i % 2 == 0:
        i-=1 

    list_plus.append(sum(matrix[i]))
    return plus_odd_rows(matrix, i-2, list_plus)

def exercise5():
    print("\nEjecutando el ejercicio 5...")
    rows = int(input("Ingrese las filas: "))
    col = int(input("Ingrese las columnas: "))
    matrix = [[0 for _ in range(col)] for _ in range(rows)]
    fill_random_matrix(matrix)
    print("Matriz generada aleatoriamente: ")
    print_matrix_recursive(matrix, rows-1)
    print(f'La suma de las filas impares es: {plus_odd_rows(matrix, rows-1)}')
    


def multiply_matrices_recursive(A, B, res, i, j, k, sum=0):
    if i < 0:
        return res
    if j < 0:
        return multiply_matrices_recursive(A, B, res, i-1, len(B[0])-1, len(A[0])-1)
    if k < 0:
        res[i][j] = sum
        return multiply_matrices_recursive(A, B, res, i, j-1, len(A[0])-1, 0)

    sum += A[i][k] * B[k][j]
    return multiply_matrices_recursive(A, B, res, i, j, k-1, sum)


def exercise6():
    print("\nEjecutando el ejercicio 6...")
    rowsA = int(input("Ingrese el número de filas de la matriz A: "))
    colsA = int(input("Ingrese el número de columnas de la matriz A: "))
    colsB = int(input("Ingrese el número de columnas de la matriz B: "))
    
    A = [[0 for _ in range(colsA)] for _ in range(rowsA)]
    B = [[0 for _ in range(colsB)] for _ in range(colsA)]
    
    fill_random_matrix(A)
    fill_random_matrix(B)
    
    print("Matriz A: ")
    print_matrix_recursive(A, rowsA-1)
    print("Matriz B: ")
    print_matrix_recursive(B, colsA-1)
    
    AB = [[0 for _ in range(colsB)] for _ in range(rowsA)]
    multiply_matrices_recursive(A, B, AB, rowsA-1, colsB-1, colsA-1)
    print("Matriz AB: ")
    print_matrix_recursive(AB, rowsA-1)
    

def exercise7():
    print("\nEjecutando el ejercicio 7...")

def exercise8():
    print("\nEjecutando el ejercicio 8...")

def exercise9():
    print("\nEjecutando el ejercicio 9...")

def exercise10():
    print("\nEjecutando el ejercicio 10...")

def menu():
    while True:
        print("\n\nSelecciona un ejercicio:")
        for i in range(1, 11):
            print(f"{i}. Ejercicio {i}")
        print("0. Salir")

        opcion = int(input("Introduce tu opción: "))

        if opcion == 1:
            exercise1()
        elif opcion == 2:
            exercise2()
        elif opcion == 3:
            exercise3()
        elif opcion == 4:
            exercise4()
        elif opcion == 5:
            exercise5()
        elif opcion == 6:
            exercise6()
        elif opcion == 7:
            exercise7()
        elif opcion == 8:
            exercise8()
        elif opcion == 9:
            exercise9()
        elif opcion == 10:
            exercise10()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu()
