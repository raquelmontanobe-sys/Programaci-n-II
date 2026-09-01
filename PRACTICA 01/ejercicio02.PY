class Ecuacion:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def tieneSolucion(self):
        return(self.__a*self.__d-self.__b*self.__c != 0)
    def getX(self):
        return (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
    def getY(self):
            return (self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))
d=float(input("Ingrese el valor de d: "))
e=float(input("Ingrese el valor de e: "))
f=float(input("Ingrese el valor de f: "))
ecuacion=Ecuacion(a,b,c,d,e,f)
if ecuacion.tieneSolucion():
    print("La ecuación tiene solución")
    print("El valor de x es:",ecuacion.getX())
    print("El valor de y es:",ecuacion.getY())
else:
    print("La ecuación no tiene solución")