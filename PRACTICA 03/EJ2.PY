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
    def generaNumero(self):
        return random.randint(0, 10)
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    def juega(self):
        self.reiniciarPartida()
        self.numeroAAdivinar = self.generaNumero()        
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
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not super().validaNumero(numero):
            return False
        if numero % 2 != 0:
            print("Error: debes ingresar un numero par.")
            return False
        return True
    def generaNumero(self):
        return random.choice([0, 2, 4, 6, 8, 10])
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not super().validaNumero(numero):
            return False
        if numero % 2 == 0:
            print("Error: debes ingresar un numero impar.")
            return False
        return True
    def generaNumero(self):
        return random.choice([1, 3, 5, 7, 9])
class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)
        print("JUEGO DE ADIVINAR NUMERO")
        juego1.juega()
        print("JUEGO DE ADIVINAR NUMERO PAR")
        juego2.juega()
        print("JUEGO DE ADIVINAR NUMERO IMPAR")
        juego3.juega()
if __name__ == "__main__":
    Aplicacion.main()