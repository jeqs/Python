import numpy as np

pelis = np.array([
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 123, 1985, 8],
    ['Peli 3', 'Drama', 110, 1998, 7.5],
    ['Peli 4', 'Terror', 130, 1978, 6.5],
    ['Peli 5', 'Terror', 142, 2000, 9]
])

generos, conteo = np.unique(pelis[:,1], return_counts = True)
conteo_desc = np.argsort(conteo)[::-1] #Devuelve indice de los arreglos de mayor a menor
popular = generos[conteo_desc[0]]      #Buscar genero x el Indice
print(popular)

decadas = np.unique(pelis[:,3].astype(int) // 10 * 10)
print(decadas)

conteo_decadas= []
for decada in decadas:
    conteo = np.count_nonzero((pelis[:,3].astype(int) >= decada) & (pelis[:,3].astype(int) < decada + 10))
    conteo_decadas.append(conteo)
    print (f"decada {decada} conteo_decadas {conteo}")

                                        