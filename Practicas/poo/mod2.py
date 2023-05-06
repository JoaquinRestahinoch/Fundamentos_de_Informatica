class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5
    
    def pila_atomica (self):
        if self.potencia <= 75:
            self.potencia += 25
        else:
            self.potencia = 100

    def escudo (self):
        if self.coraza <= 10:
            self.coraza += 10
        else:
            self.coraza = 20
    
    def potencia (self):
        return self.potencia
    
    def coraza(self):
        return self.coraza
    
    def recibir_ataque(self,puntos):
        if puntos > self.coraza:
            self.potencia -= (puntos-self.coraza)
            self.coraza = 0
        else:
            self.coraza -= puntos
    
    def fortaleza_defensiva(self):
        return (self.coraza + self.potencia)
    
    def necesita_fortalecerse(self):
        return (self.coraza == 0 and self.potencia < 20)
    
    def fortaleza_ofensiva(self):
        if self.potencia < 20:
            return 0
        else:
            return ((self.potencia - 20) / 2)

enterprise = Enterprise()
enterprise.pila_atomica()
enterprise.recibir_ataque(14)
enterprise.escudo()

print(enterprise.coraza)
print(enterprise.potencia)