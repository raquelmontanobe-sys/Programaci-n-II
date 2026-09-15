import math
class MiPunto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanciaP(self, punto):
        return math.sqrt((punto.getX() - self.x)**2 +(punto.getY() - self.y)**2)
    def distanciaC(self, x, y):
        return math.sqrt((x - self.x)**2 +(y - self.y)**2)
p1 = MiPunto()
p2 = MiPunto(10, 30.5)
print("Punto 1:", p1.getX(), p1.getY())
print("Punto 2:", p2.getX(), p2.getY())
print("Distancia usando un punto:", p1.distanciaP(p2))
print("Distancia usando coordenadas:", p1.distanciaC(10, 30.5))