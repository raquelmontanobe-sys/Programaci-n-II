import math
def promedio(a, b, c, d, e, f, g, h, i, j):
    return (a + b + c + d + e + f + g + h + i + j) / 10
def desviacion(a, b, c, d, e, f, g, h, i, j):
    media = promedio(a, b, c, d, e, f, g, h, i, j)
    suma = ((a - media) ** 2 +(b - media) ** 2 +(c - media) ** 2 +(d - media) ** 2 +(e - media) ** 2 +(f - media) ** 2 +(g - media) ** 2 +(h - media) ** 2 +(i - media) ** 2 +(j - media) ** 2)
    return math.sqrt(suma / 9)
a=float(input("Ingrese a: "))
b=float(input("Ingrese b: "))
c=float(input("Ingrese c: "))
d=float(input("Ingrese d: "))
e=float(input("Ingrese e: "))
f=float(input("Ingrese f: "))
g=float(input("Ingrese g: "))
h=float(input("Ingrese h: "))
i=float(input("Ingrese i: "))
j=float(input("Ingrese j: "))
print("El promedio es", promedio(a, b, c, d, e, f, g, h, i, j))
print("La desviación estandard es",desviacion(a, b, c, d, e, f, g, h, i, j))