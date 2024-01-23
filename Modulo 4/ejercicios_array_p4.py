import numpy as np

ventas = np.array([
    [1, 100, 'ropa'],
    [1, 200, 'calzado'],
    [1, 300, 'reloj'],
    [2, 100, 'ropa'],
    [2, 200, 'calzado'],
    [2, 300, 'reloj'],
    [3, 100, 'ropa'],
    [3, 200, 'calzado'],
    [3, 300, 'reloj']
])

venta_mes = np.zeros(12)

suma = 0
for venta in ventas:
    suma = 0
    for mes in range(1,13):
        if venta[0].astype(int) == mes:
            print(f"ventas del mes {mes} es de {venta[1]}")
            suma = suma + venta[1].astype(int)