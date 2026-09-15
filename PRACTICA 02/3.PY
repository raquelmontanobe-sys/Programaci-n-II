import math
class Vector:
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, otro):
        return(Vector(self.x+otro.x,self.y+otro.y,self.z+otro.z))
    def __sub__(self, otro):
        return(Vector(self.x-otro.x,self.y-otro.y,self.z-otro.z))
    def __mul__(self, r):
        return(Vector(r*self.x,r*self.y,r*self.z))
    def longitud(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    def normal(self):
        s=self.longitud()
        return(Vector(self.x/s,self.y/s,self.z/s))
    def __matmul__(self, otro):
        return(self.x*otro.x+self.y*otro.y+self.z*otro.z)
    def __xor__(self, otro):
        return(Vector(self.y*otro.z-self.z*otro.y,-(self.z*otro.x-self.x*otro.z),self.x*otro.y-self.y*otro.x))
    def perpendicular(self, otro):
            return (self@otro)==0
    def paralelo(self, otro):
        producto=self^otro
        return (producto.x==0 and producto.y==0 and producto.z==0)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
a=Vector(2, -1, 3)
b=Vector(-3, 2, 5)
print("Vector a:", a)
print("Vector b:", b)
print("Suma:")
print(a+b)
print("Resta:")
print(a-b)
print("Multiplicación por escalar:")
print(a*2)
print("Longitud de a:")
print(a.longitud())
print("Normal de a:")
print(a.normal())
print("Producto escalar:")
print(a@b)
print("Producto vectorial:")
print(a^b)
print("¿Son perpendiculares?")
print(a.perpendicular(b))
print("¿Son paralelos?")
print(a.paralelo(b))