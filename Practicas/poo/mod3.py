class Persona:
    def __init__(self, energia):
        self.energia = energia
        self.feliz = False
    
    def comer (self):
        self.energia += 10
    
    def energia_ahora (self):
        return self.energia
    
    def dormir (self, horas):
        if horas >= 8:
             self.energia = 100
        else:
            self.energia += (horas*12.5)
    
    def ejercicio (self,minutos):
        self.energia -= (25*(minutos/30))
    
    def estado_animo(self):
        return self.feliz

class Estudiante(Persona):
    def estudiar (self,hora):
        self.energia -= (20*hora)
    def aprobar (self):
        return (not self.estado_animo())

estudiante = Estudiante(100)
estudiante.ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_ahora())