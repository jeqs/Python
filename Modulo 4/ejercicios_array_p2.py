import numpy as np

ale = np.random.randint(1, 101, size=(15))
# print(ale)

multi = 1
for numero in ale:
    multi = multi * numero

# print (multi)

multi_numpy = np.prod(ale)
# print (multi_numpy)

ale_bin = np.random.random(15)
# print (ale_bin)

a = np.random.randint(1, 101, size=(3))
b =  np.random.randint(1, 101, size=(3))
# print (a)
# print (b)

suma = a + b      
# print (suma)

suma = np.add(a,b)
# print (suma)

resta = a - b      
# print (resta)

resta = np.subtract(a,b)
# print (resta)

multi = np.multiply(a,b)
# print (multi)

# print ("mayor", np.max(multi))
# print ("media", np.mean(multi))
# print ("mediana", np.median(multi))
# print ("desviacion", np.std(multi))

cant = int(input("Insertar cantidad: "))

unos = np.ones(cant)
print(unos)

cant_filas = int(input("Insertar cantidad filas: "))
cant_columnas = int(input("Insertar cantidad columnas: "))

if cant_filas * cant_columnas == cant:
    arra_unos = unos.reshape((cant_filas,cant_columnas))
    print(arra_unos)
else:
    print ("Cantidad filas o columnas incorrecto")