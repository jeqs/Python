class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario, bono_anual):
        super().__init__(nombre, apellido, salario)
        self.bono_anual = bono_anual
    
    def calcular_salario(self):
        return (self.salario + self.bono_anual)

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario, horas_trabajadas):
        super().__init__(nombre, apellido, salario)
        self.horas_trabajadas = horas_trabajadas
    
    def calcular_salario(self):
        return (self.salario + self.horas_trabajadas * 1.5*4*12)
    
empleadoTC = EmpleadoTiempoCompleto("Jose", "Quispe", 5000, 1000)
print (f"{empleadoTC.calcular_salario()}")

empleadoTP = EmpleadoTiempoParcial("Jose", "Quispe", 5000, 10)
print (f"{empleadoTP.calcular_salario()}")