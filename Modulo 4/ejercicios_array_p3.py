import numpy as np

cant_filas = int(input("Insertar cantidad filas: "))
cant_colum = int(input("Insertar cantidad columnas: "))
a = np.eye(cant_filas, cant_colum)
print(a)

b = np.arange(cant_filas*cant_filas).reshape((cant_filas,cant_filas))
print(b)

print("concatena")
c = np.concatenate((a,b))
print(c)

print("apila h")
d = np.hstack((a,b))
print(d)

print("apila v")
e = np.vstack((a,b))
print(e)