import math
class AlgebraVectorial:
    def __init__(self, x, y, z=0):
        self.__x = x
        self.__y = y
        self.__z = z
    def __add__(self, o):
        return AlgebraVectorial(self.__x + o.__x,self.__y + o.__y,self.__z + o.__z)
    def __sub__(self, o):
        return AlgebraVectorial(self.__x - o.__x,self.__y - o.__y,self.__z - o.__z)
    def __mul__(self, o):
        if isinstance(o, AlgebraVectorial):
            return (self.__x * o.__x +self.__y * o.__y +self.__z * o.__z)
        else:
            return AlgebraVectorial(self.__x * o,self.__y * o,self.__z * o)
    def __rmul__(self, o):
        return self.__mul__(o)
    def __str__(self):
        return f"({self.__x}, {self.__y}, {self.__z})"
    def magnitud(self):
        return math.sqrt(self.__x**2 +self.__y**2 +self.__z**2)
    def producto_cruz(self, o):
        return AlgebraVectorial(self.__y * o.__z - self.__z * o.__y,self.__z * o.__x - self.__x * o.__z,self.__x * o.__y - self.__y * o.__x)
    def perpendicular_a(self, b):
        return abs((self + b).magnitud() -(self - b).magnitud()) < 1e-6
    def perpendicular_b(self, b):
        return abs((self - b).magnitud()-(b - self).magnitud()) < 1e-6
    def perpendicular_c(self, b):
        return abs(self * b) < 1e-6
    def perpendicular_d(self, b):
        izq = (self + b).magnitud() ** 2
        der = self.magnitud()**2 + b.magnitud()**2
        return abs(izq - der) < 1e-6
    def paralela_e(self, b, r):
        esperado = b * r
        return (abs(self.__x - esperado.__x) < 1e-6 and abs(self.__y - esperado.__y) < 1e-6 and abs(self.__z - esperado.__z) < 1e-6)
    def paralela_f(self, b):
        return self.producto_cruz(b).magnitud() < 1e-6
    def proyeccion_de_a_sobre_b(self, b):
        if b.magnitud() == 0:
            return None
        factor = (self * b) / (b.magnitud() ** 2)
        return b * factor
    def componente_de_a_en_b(self, b):
        if b.magnitud() == 0:
            return None
        return (self * b) / b.magnitud()
if __name__ == "__main__":
    a = AlgebraVectorial(1, 0, 0)
    b = AlgebraVectorial(0, 1, 0)
    c = AlgebraVectorial(2, 0, 0)
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print()
    print("a perpendicular a b? (c):", a.perpendicular_c(b))
    print("a paralelo a c? (f):", a.paralela_f(c))
    print()
    print("Proyeccion de a sobre c:", 
        a.proyeccion_de_a_sobre_b(c))
    print("Componente de a en c:", 
        a.componente_de_a_en_b(c))