"""
4-Escribe un programa que imprima los números pares del 1 al 100.

"""

for i in range(101):
    if i % 2 == 0:
        print(i, 'es par.')


for i in range(0, 101, 2):
    print(i)