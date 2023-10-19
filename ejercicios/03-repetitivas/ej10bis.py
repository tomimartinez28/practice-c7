letra = input('Ingrese una letra: ')

letra = letra.lower()

print(letra)


if letra in 'aeiou':
    print('La letra ingresada es una vocal')
else:
    print('La letra es una consonante')