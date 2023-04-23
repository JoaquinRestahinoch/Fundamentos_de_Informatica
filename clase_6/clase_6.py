#no instancio la clase porque no tiene métodos particulares. Solo actúa como una clase abstracta
class AnimalAlado:
    def esta_feliz(self):
      return self.energia >= 500

class Golondrina (AnimalAlado): # le digo a Golondrina que adopte los métodos de AnimalesAlado
  def __init__(self, energia): 
    self.energia = energia

  def esta_debil (self):
        return self.energia<10
  
  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

""" def esta_feliz(self):
    return self.energia >= 50
"""
class Dragon (AnimalAlado): #le permito entender a la clase Dragon si está feliz (porque le añadí la clase AnimalesAlado)     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def esta_debil (self):
    return self.energia<50

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1
    
  def volar(self, kms):
    self.energia -= 10 + kms/10

class Entrenador:
    def __init__(self, equipo_dragones):
        self.equipo_dragones = equipo_dragones
    
    def agregar_dragones_al_equipo(self, dragon):
        for i in dragon:
            self.equipo_dragones.append(i)
        return self.equipo_dragones
    
    def obtener_equipo_dragones(self):
        return self.equipo_dragones

  #metodo para aceptar dragones


""""def entrenarlos(self):
    .volar_en_circulos()
    .comer_peces()"""


""""  def esta_feliz(self):
    return self.energia >= 500"""

"""
vemos que el método volar es compartido por ambos objetos (es EXÁCTAMENTE el mismo código), vamos a unificarlos.

"""
  
pepita = Golondrina(100) #instanciación del objeto. Lo creo y le atribuyo una clase
anastasia = Golondrina(20)
roberta = Dragon(10, 1000)
maria= Golondrina (42)
chimuelo = Dragon (200, 1000)
hipo=Entrenador ([])

  #metodo para aceptar dragones
"""""
Creá a la golondrina maria con 42 puntos de energía inicial
Creá al dragón chimuelo, con 200 dientes y 1000 de energía inicial
Definí el método esta_debil, que nos dice si nuestras "aves" tiene menos de 10 puntos de energía (golondrinas) o menos de 50 puntos de energía (dragones)
Definí el método esta_feliz, que nos dice si nuestras "aves" tiene más de 500 puntos de energía (sin importar de qué clase sean)
Hace a hipo, entrenador de dragones: sabe aceptar a dragones, quienes son sus entrenados y 
hacerlos entrenar todos los dias, haciendoles dar 20 vueltas en circulos y 
luego comer su comida favorita hasta saciarse (3 peces)
Hacé que hipo pueda entrenar a las golondrinas. ¿Qué comportamiento deberían entender las golondrinas ahora?
Definí el método entrenamiento_intensivo, que hace dar vueltas en circulos a sus entrenados hasta que estén débiles."""""