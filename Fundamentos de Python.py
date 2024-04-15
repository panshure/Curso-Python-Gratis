hola=(1+1)*8
print(hola)

hola1=25/5
print(hola1)

hola2=25//6
print(hola2)

hola3=(5**2)-16
print(hola3)

hola4=12>7
print(hola4)

a=6
b=5

c=a+b==13
print(c)

lista=["soy popular", False, 3, 4.71, ["Jon Bon Jovi","Pedro Suárez Vertiz"]]
print(lista)

cursos = ["Historia", "Economia", "Antropologia", "RSP", "Derecho"]

#número de cursos

numerocursos=len(cursos)
print(numerocursos)

#Tu respuesta
cursos = ["Historia", "Economia", "Antropologia", "RSP", "Derecho"]
cursomas=["Elementos de Ciencia Política"]

cursos+cursomas

comidas=["Causa rellena","Lomo saltado","Rocoto relleno","Ají de gallina"]
comidasmas=["Tacacho con cecina"]

print(comidas+comidasmas)

comidas.append("Pollo a la brasa")
print(comidas)

mas_cursos = ['Lógica', 'Epistemología']
cursos_copy = cursos[:]
cursos_copy.extend(mas_cursos)
cursos_copy

mas_comidas =["Ceviche","Cuy chactado"]
comidas_copy= comidas[:]
comidas_copy.extend(mas_comidas) 
print(comidas_copy)

#Tu respuesta
cursoRSP = cursos[3]
print(cursoRSP)


comidas=["Causa rellena","Lomo saltado","Rocoto relleno","Ají de gallina"]
comidaRocoto=comidas[2]
print(comidaRocoto)


comidas.remove("Lomo saltado")

print(comidas)

comidas.reverse()
print(comidas)

listanumeros=[23,70,14,34,16.5]
listanumeros.sort()
print(listanumeros)
