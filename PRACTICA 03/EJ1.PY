import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.numeroDeVidasIn = numeroDeVidas
        self.record=0
    def reiniciarPartida(self):
        self.numeroDeVidas = self.numeroDeVidasIn
    def actualizarRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
    def quitaVida(self):
        self.numeroDeVidas= self.numeroDeVidas - 1
        return self.numeroDeVidas > 0
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
    def juega(self):
        self.reiniciarPartida()
        self.numeroAAdivinar=random.randint(0, 10)
        while True:
            print("Adivina un numero entre 0 y 10:")
            numero = int(input())
            if numero==self.numeroAAdivinar:
                print("Acertaste!")
                self.actualizarRecord()
                print("Record:", self.record)
                return
            if not self.quitaVida():
                print("Te quedaste sin vidas.")
                print("El numero era:", self.numeroAAdivinar)
                return
            if numero < self.numeroAAdivinar:
                print("El numero a adivinar es mayor.")
            else:
                print("El numero a adivinar es menor.")
            print("Vidas restantes:", self.numeroDeVidas)
class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(5)
        juego.juega()
if __name__ == "__main__":
    Aplicacion.main()