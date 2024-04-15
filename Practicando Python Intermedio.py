for numero in range (2,21,2):
    print(numero)

# Inicializar variables
numero = 1
suma_impares = 0

# Calcular la suma de números impares del 1 al 50
while numero <= 50:
    suma_impares += numero
    numero += 2  # Incrementar en 2 para obtener el próximo número impar

# Imprimir el resultado
print(f"La suma de los números impares del 1 al 50 es: {suma_impares}")

#Funciones

cadena=input("Ingrese una cadena:")
longitud=len(cadena)
print(f"La longitud de la cadena es:")

lista=[1,3,6,9,16,20,25,30]
numero_mas_alto = max(lista)

numero_mas_bajo = min(lista)

print(numero_mas_bajo)

#Definiendo calculadora
def calculadora(num1, num2, operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:  # Evitar la división por cero
            resultado = num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Error: Operador no válido"

    return resultado

# Ejemplos de uso:
resultado_suma = calculadora(5, 3, '+')
print(f"Suma: {resultado_suma}")

resultado_multiplicacion = calculadora(4, 6, '*')
print(f"Multiplicación: {resultado_multiplicacion}")

resultado_division = calculadora(8, 2, '/')
print(f"División: {resultado_division}")

#Definiendo promedio

def calcular_promedio
    if def calcular_promedio(lista_numeros):
    if not lista_numeros:
        return "Error: La lista está vacía"

    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros)
    return promedio

# Ejemplo de uso:
numeros = [2, 4, 6, 8, 10]
promedio_resultado = calcular_promedio(numeros)
print(f"El promedio de la lista es: {promedio_resultado}")

#Funciones lambda
# Lista de palabras
palabras = ["manzana", "pera", "banana", "kiwi", "uva"]

# Ordenar las palabras por longitud usando una función lambda
palabras_ordenadas = sorted(palabras, key=lambda x: len(x))

# Imprimir la lista ordenada
print(palabras_ordenadas)


