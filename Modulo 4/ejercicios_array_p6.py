import numpy as np

datos_clima = np.array([
    [22, 10, 1008, 1],
    [23, 11, 1009, 1],
    [24, 12, 1010, 2],
    [21, 13, 1011, 2],
    [19, 14, 1012, 3],
    [20, 15, 1013, 3],
    [19, 14, 1012, 4],
    [20, 15, 1013, 4],
    [19, 14, 1012, 5],
    [20, 15, 1013, 6],
    [19, 14, 1012, 6],
    [20, 15, 1013, 6],
    [19, 14, 1012, 7],
    [20, 15, 1013, 7],
    [19, 14, 1012, 8],
    [20, 15, 1013, 8],
    [19, 14, 1012, 9],
    [20, 15, 1013, 9],
    [19, 14, 1012, 10],
    [20, 15, 1013, 10],
    [19, 14, 1012, 11],
    [20, 15, 1013, 11],
    [19, 14, 1012, 12],
    [20, 15, 1013, 12],
])

meses = datos_clima[:,3]
temperatura = datos_clima[:,0]
temp_mes = np.zeros(12)

for mes in range(12):
    temp_mes[mes] = np.mean(temperatura[meses == mes + 1]) # todo los elementos donde meses igual al (mes) 
    print(temp_mes[mes])