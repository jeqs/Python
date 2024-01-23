nombre = input("Introduzca letra: ")
print (f"Letra hasta menos de 10 Unicode {ord(nombre)}")

if ord(nombre) >= 65 and ord(nombre) <=90:
    print ("Mayuscula")
elif ord(nombre) >= 97 and ord(nombre) <=122:
    print ("Minuscula")
else:
    print ("Otra")
