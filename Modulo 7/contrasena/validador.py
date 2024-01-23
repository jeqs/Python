def validarContrasena(contrasena):
    valida = True
    tieneMay = False
    tieneMin = False
    tieneNum = False

    if len(contrasena) <=8: valida = False

    for char in contrasena:
        if char.isupper(): tieneMay = True
        if char.islower(): tieneMin = True
        if char.isdigit(): tieneNum = True

    return valida and tieneMay and tieneMin and tieneNum