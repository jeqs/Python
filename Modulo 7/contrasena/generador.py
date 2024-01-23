import random
import string

def generarContrasena(longitud, incluirMay = True, incluirMin = True, incluirNum = True, incluirEsp = True):
    contrasena = ""
    chart = ""

    if incluirMay:
        chart += string.ascii_uppercase
    
    if incluirMin:
        chart += string.ascii_lowercase
    
    if incluirNum:
        chart += string.digits

    if incluirEsp:
        chart += string.punctuation

    contrasena = "".join(random.choice(chart) for i in range(longitud))
    
    return contrasena