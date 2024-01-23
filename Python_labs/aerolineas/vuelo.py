class Vuelo:
    def __init__(self, numero, origen, destino, capacidad):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []
    
    def agregar_pasajero(self, pasajero):
        if self.valida_disponibilidad() > 0:
            self.pasajeros.append(pasajero)
            print ("Pasajero agregado")
        else:
            print ("No hay asientos disponibles")
    
    def valida_disponibilidad(self):
        return self.capacidad - len(self.pasajeros)

class VueloEspecial(Vuelo):
    def __init__(self, numero, origen, destino, capacidad, motivo):
        super().__init__(numero, origen, destino, capacidad)
        self.motivo = motivo

# vuelo_regular = Vuelo("ABC", "BOG", "MAD", 10)
# print(f"Validando Dispo: {vuelo_regular.valida_disponibilidad()}")
# vuelo_regular.agregar_pasajero("Juan")
# print(f"Validando Dispo: {vuelo_regular.valida_disponibilidad()}")
# vuelo_regular.agregar_pasajero("Juan2")
# print(f"Validando Dispo: {vuelo_regular.valida_disponibilidad()}")
# vuelo_regular.agregar_pasajero("Juan3") 
# print(f"Validando Dispo: {vuelo_regular.valida_disponibilidad()}")

vuelo_especial = VueloEspecial("ABC", "BOG", "MAD", 10, "Motivo")
print(f"Validando Dispo: {vuelo_especial.valida_disponibilidad()}")
vuelo_especial.agregar_pasajero("Juan")
print(f"Validando Dispo: {vuelo_especial.valida_disponibilidad()}")
vuelo_especial.agregar_pasajero("Juan2")
print(f"Validando Dispo: {vuelo_especial.valida_disponibilidad()}")
vuelo_especial.agregar_pasajero("Juan3") 
print(f"Validando Dispo: {vuelo_especial.valida_disponibilidad()}")
