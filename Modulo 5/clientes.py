base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012")]
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]),("Luis", "Calle 789", ["Libro4"])]

clientes1 = [cliente[0] for cliente in base_datos1]
clientes2 = [cliente[0] for cliente in base_datos2]

comunes = set(clientes1) & set(clientes2)

print(comunes)