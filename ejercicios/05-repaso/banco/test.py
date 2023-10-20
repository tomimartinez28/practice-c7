DATOS_USUARIOS = [ {'username' : 'tomimartinez28', 'password' : 'heladito123', 'saldo' : 0},
                    {'username' : 'zoe28', 'password' : 'heladito456', 'saldo' : 1000},
                    {'username' : 'lea28', 'password' : 'heladito789', 'saldo' : 0},
                ]


# LIST COMPREHENSION

lista_de_usernames = [usuario['username'] for usuario in DATOS_USUARIOS]

print(lista_de_usernames)














""" for usuario in DATOS_USUARIOS:
    lista_de_usernames.append(usuario['username'])

print(lista_de_usernames)

 """