import time
class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = time.time()
    def inicia(self):
        self.__inicia = time.time()
    def detener(self):
        self.__finaliza = time.time()
    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000
    def getInicia(self):
        return self.__inicia
    def getFinaliza(self):
        return self.__finaliza
def seleccion(a):
    for i in range(len(a) - 1):
        menor = i
        for j in range(i + 1, len(a)):
            if a[j] < a[menor]:
                menor = j
        aux = a[i]                 
        a[i] = a[menor]
        a[menor] = aux
a = []
for i in range(10000):
    a.append(10000 - i)
cronometro = Cronometro()
cronometro.inicia()
seleccion(a)
cronometro.detener()
print("Tiempo de ejecución:", cronometro.lapsoDeTiempo(), "milisegundos")