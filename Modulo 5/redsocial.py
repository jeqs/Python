red_social = [("Juan", ["Maria", "Pedro","Luis"]), ("Maria", ["Juan", "Pedro","Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]
red_social_unicos = []
for usuario, amigos in red_social:
    amigos_uniucos = list(set(amigos))
    red_social_unicos.append((usuario, amigos_uniucos))

amigos_usuarios = []
for usuario, amigos in red_social_unicos:
    amigos_usuarios.append((amigos, len(amigos)))

lista_usuarios = [amigos[0] for amigos in amigos_usuarios]
nro_usuarios = [amigos[1] for amigos in amigos_usuarios]
indice_amigos = nro_usuarios.index(max(nro_usuarios))

print(lista_usuarios[indice_amigos], nro_usuarios[indice_amigos])
