class Titan:
    def __init__(self,salud):
        self.salud = salud
    
    def esta_vivo(self):
        return self.salud > 0
    
    def salud_actual(self):
        return self.salud

    def recibir_ataque(self,daño):
        if self.esta_vivo():
            self.salud -= 1.5*daño
        else:
            print("El titan no puede recibir daño por que ha muerto")
    
    def destruir_casas(self):
        if self.cuantas_casas() > 1:
            if (self.cuantas_casas() % 1) > 0:
                self.salud -= (self.cuantas_casas() // 1) *12.5
            else:
                self.salud -= (self.cuantas_casas() - 1) *12.5
        else:
            print("No puede destruir ninguna casa")
    

    def cuantas_casas(self):
        return self.salud *8 / 100
    
    def grito(self):
        return "¡Aaaarrrg!"
    
    
titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())