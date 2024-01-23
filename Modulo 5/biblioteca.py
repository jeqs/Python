biblioteca = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Garbriel Garcia Márquez'), ('La ciudad y los perros', 'Mario Vargas Llosa')]

for libro, autor in biblioteca:
    apellido = autor.split()[-1]
    print(libro, autor, apellido)
