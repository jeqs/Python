'''
Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
de los otros dos.
 '''

numero_1 = int(input("Ingresar Numero 1: "))
numero_2 = int(input("Ingresar Numero 2: "))
numero_3 = int(input("Ingresar Numero 3: "))

print(numero_1 == (numero_2 + numero_3) or numero_2 == (numero_1 + numero_3) or numero_3 == (numero_1 + numero_2))

# if numero_1 == (numero_2 + numero_3) or numero_2 == (numero_1 + numero_3) or numero_3 == (numero_1 + numero_2):
#     print ("Si") 
# else:
#     print("No")
