# TERCERA OPCIÓN DE RESOLUCIÓN

class PacMan:
    def _init_(self):
        self.vidas = 3
        self.puntos = 0
        # velocidad opcional

    def comerBolita(self, cantidad):
        self.puntos += (cantidad * 2)

    def velocidad(self):
        return self.puntos 
    
    def perderVida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print ("GAME OVER")

    def comerFantasma(self, fantasma, color):
        fantasma.set_color(color)
        self.puntos += fantasma.puntos_color(color)

class Fantasma:
    def _init_(self):
        self.color = None

    def set_color(self, color):
        self.color = color
    
    def puntos_color(self, color):
        return self.color.puntos()

class Rojo:
    def puntos(self):
        return 2

class Naranja:
    def puntos(self):
        return 4

class Verde:
    def puntos(self):
        return 6

class Rosa:
    def puntos(self):
        return 8

pacman = PacMan()
rojo = Rojo()
rosa = Rosa()
naranja = Naranja()
verde = Verde()
fantasma = Fantasma()

print(pacman.puntos)
pacman.comerBolita(10)
print(pacman.puntos)
pacman.comerFantasma(fantasma, rojo)
print(pacman.puntos)
pacman.comerFantasma(fantasma, verde)
print(pacman.puntos)

# B) A medida que avanza el juego Pac-Man obtiene nuevas habilidades: sí llega a 200 puntos, gana una vida extra. Además, ahora gana más velocidad a medida que suma puntos de la forma: cada punto extra le da un 1% más de velocidad.

class PacManMejorado(PacMan):
    def vidaExtra(self):
        if self.puntos >= 200:
            self.vidas += 1
            self.puntos -= 200
        else:
            print("Faltan", 200 - self.puntos, "puntos para ganar una vida extra")
    
    def velocidad(self):
        return 3 + self.puntos / 100