import generador as gn
import validador as val

def solicitar_contra():
    contrasena = input("Ingresar contrasena:")
    valida = val.validarContrasena(contrasena)
    if valida:
        print("Valida")
    else:
        print("No Valida")
        print("Sugerencia", gn.generarContrasena(5))

solicitar_contra()