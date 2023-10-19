"""
17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
letras pero en distinto orden), o False en caso contrario.

"""

def es_anagrama(cadena1, cadena2):
    cadena1_limpia = cadena1.replace(' ', '').lower()
    cadena2_limpia = cadena2.replace(' ', '').lower()

    return sorted(cadena1_limpia) == sorted(cadena2_limpia)




print(es_anagrama('nido', 'Odin'))


# el todo # eltodo # deloot

# Toledo  # toledo # deloot









