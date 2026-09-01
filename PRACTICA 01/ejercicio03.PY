import math
class Ecuacioncuadratica:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def discriminante(self):
        return self.__b**2-4*self.__a*self.__c
    def getRaiz1(self):
        return (-self.__b+math.sqrt(self.__b**2-4*self.__a*self.__c))/(2*self.__a)
    def getRaiz2(self):
            return (-self.__b-math.sqrt(self.__b**2-4*self.__a*self.__c))/(2*self.__a)
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))
ecuacion=Ecuacioncuadratica(a,b,c)
if ecuacion.discriminante()>0:
    print("Tiene dos raices")
    print("Raiz 1: ",ecuacion.getRaiz1())
    print("Raiz 2: ",ecuacion.getRaiz2())
elif ecuacion.discriminante()==0:
    print("Tiene una raíz")
    print("Raiz 1: ",ecuacion.getRaiz1())
else:
    print("No tiene raíz")