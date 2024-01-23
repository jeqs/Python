import numpy as np

calificaciones = np.array([
    [5, 4.3, 2],
    [3, 4.5, 2.7],
    [4, 2.1, 1.5]
])

print("calificaciones")
print(calificaciones)

# Tareas 33%, Examenes 34%, Trabajos 33%

final_examen = np.median(calificaciones[0])
print(final_examen)

final_trabajos = np.median(calificaciones[1])
print(final_trabajos)

final_tareas = np.median(calificaciones[2])
print(final_tareas)

total = np.array([
    final_examen,
    final_trabajos,
    final_tareas
])

print(total)
print("nota total", np.median(total))
