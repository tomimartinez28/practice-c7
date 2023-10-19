"""
12-Crea una función llamada convertir_temperatura que tome una temperatura
en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
es: Fahrenheit = (Celsius * 9/5) + 32.

"""




def convertir_temperatura(celsius):
    return celsius * 9/5 + 32



temperatura = float(input('Ingrese la temp en grados celius: '))


print(f'{temperatura} grados celius es igual a {convertir_temperatura(temperatura)} ')
