import math
class Estadistica:
    def __init__(self,a,b,c,d,e,f,g,h,i,j):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
        self.__g=g
        self.__h=h
        self.__i=i
        self.__j=j
    def promedio(self):
        return (self.__a+self.__b+self.__c+self.__d+self.__e+self.__f+self.__g+self.__h+self.__i+self.__j)/10
    def desviacion(self):
        media = self.promedio()
        suma = ((self.__a - media) ** 2 +(self.__b - media) ** 2 +(self.__c - media) ** 2 +(self.__d - media) ** 2 +(self.__e - media) ** 2 +(self.__f - media) ** 2 +(self.__g - media) ** 2 +(self.__h - media) ** 2 +(self.__i - media) ** 2 +(self.__j - media) ** 2)
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
estadistica=Estadistica(a,b,c,d,e,f,g,h,i,j)
print("El promedio es: ", estadistica.promedio())
print("La desviación es: ", estadistica.desviacion())