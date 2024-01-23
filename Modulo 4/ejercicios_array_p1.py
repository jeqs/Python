import numpy as np

a = np.zeros(8)
a[:] = 2
# print(a)

b = np.arange(2, 11, 2)
# print(b)

c = np.arange(2, 11, 2)
# print(c)
d = c[::-1]
# print(d)

uno = np.arange(2, 11, 2)
dos = np.arange(2, 20, 2)
dos_revert = dos[::-1]
uno_dos_inter = np.intersect1d(uno,dos)
dos_dosI_inter = np.intersect1d(dos,dos_revert)

# print(uno)
# print(dos)
# print(dos_revert)
# print(uno_dos_inter)
# print(dos_dosI_inter)

cant = int(input("Insertar cantidad: "))
unos = np.ones(cant)
print(unos)