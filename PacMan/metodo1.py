# SEGUNDA OPCIÓN DE RESOLUCIÓN

class PacMan:

    def _init_(self):
        self.vidas = 3
        self.puntos = 0
        
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
        self.puntos += fantasma.puntos_color(color)

class Fantasma:
    def _init_(self):
        self.fantasmas = {"rosa": 8, "verde": 6, "naranja": 4, "rojo": 2}
    
    def puntos_color(self, color):
        return self.fantasmas[color]
    
pacman = PacMan()