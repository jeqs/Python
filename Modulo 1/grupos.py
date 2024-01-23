'''
En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la
M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y
R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por
pantalla el grupo que le corresponde a ese alumno.
'''

nombre_chica = input("Ingresar su nombre chica: ")
lista_grupo_a = "ABCDEFGHIJKLM"
lista_grupo_b = "NOPQRSTUVWYZY"

''' A..M '''
if nombre_chica[0].upper() in lista_grupo_a:
    print ("Perteneces al Grupo A")

''' N..Z '''
if nombre_chica[0].upper() in lista_grupo_b:
    print ("Perteneces al Grupo B")


nombre_chico = input("Ingresar su nombre chico: ")
lista_grupo_a = "ABCDEFGHIJKLMN"
lista_grupo_b = "RSTUVWYZY"

''' A..H '''
if nombre_chico[0].upper() in lista_grupo_a:
    print ("Perteneces al Grupo A")

''' R..Z '''
if nombre_chico[0].upper() in lista_grupo_b:
    print ("Perteneces al Grupo B")