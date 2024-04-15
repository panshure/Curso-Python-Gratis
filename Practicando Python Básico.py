#Variables simples

nombre="Fabricio"
edad=22
ciudad="Lima"
print(f"Mi nombre es {nombre}, tengo {edad}años y mi ciudad es {ciudad}")

#Datos compuestos

lista=["blanco","amarillo","verde"]
print("Lista:", lista)

tupla=("Star Wars", "Avengers","Gato con botas")
print("Tupla:",tupla)

#Operadores aritméticos

a=20
b=5

suma=a+b
print(suma)

resta=a-b
print(resta)

multi=a*b
print(multi)

div=a/b
print(div)

#Solicitar al usuario ingresar dos números

a=float(input("Ingrese el primer número:"))
b=float(input("Ingrese el segundo número:"))

#Plantear las operaciones

suma=a+b
resta=a-b
multi=a*b

#División

if b!=0:
    div=a/b
    print(f"División: {div}")
else:
    print("No se puede dividir por cero.")

#Imprimir resultados

print(f"Suma:{suma}")
print(f"Resta:{resta}")
print(f"multi:{multi}")

#Operadores de comparación


a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

if a == b:
    print("Los números son iguales.")
elif a != b:
    print("Los números son diferentes.")
    
    if a > b:
        print(f"{a} es mayor que {b}.")
    else:
        print(f"{a} es menor que {b}.")
else:
    print("Algo salió mal. Ingresa los números de nuevo.")
    
#Condicionales

a = float(input("Ingrese el primer número: "))

if a % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#Operadores lógicos

numero= float(input("Ingrese un número: "))

if numero>0 and numero%2==0:
    print(f"{numero} es positivo y par")
else:
    print(f"{numero} no cumple con el requisito de ser positivo y par")
    
#Métodos de cadenas

nombre_completo = "Fabricio Flores Quispe"

# Obtener el nombre en mayúsculas
nombre_en_mayusculas = nombre_completo.split()[0].upper()

# Obtener los apellidos en minúsculas
apellidos_en_minusculas = ' '.join(nombre_completo.split()[1:]).lower()

# Imprimir los resultados
print(f"Nombre en mayúsculas: {nombre_en_mayusculas}")
print(f"Apellidos en minúsculas: {apellidos_en_minusculas}")

#Métodos de listas

ciudades=["Lima","Buenos Aires","Caracas","Santiago","Quito"]
print(ciudades)

#agregando un elemento a la lista
ciudades.append("Asunción")
print(ciudades)

#removiendo un elemento de la lista por su valor
ciudades.remove("Caracas")
print(ciudades)

#Métodos de diccionarios

canción_favorita={
    "nombre":"En la ciudad de la furia","artista":"Soda Stereo","año":1988
}
for clave, valor in canción_favorita.items():
    print(f"{clave}: {valor}")

nombre = input("Ingrese su nombre: ")
edad_str= input("Ingrese su edad:")

# Convertir la edad a un número entero
edad = int(edad_str)
#mostrando el dato
print(f"Mi  nombre es {nombre} y mi edad es {edad}")  

