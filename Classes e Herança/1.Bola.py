################################################
#1) Classe Bola: Crie uma classe que modele uma bola: Atributos: Cor, circunferência,
#material Métodos: trocaCor e mostraCor.
class Bola:
    cor = None
    circ = None
    material = None
    
    def __init__(self, cor, circ, material):
        self.cor = cor
        self.circ = circ
        self.material = material
    
    def mostracor(self):
        return self.cor
    
    def trocacor(self,Ncor):
        self.cor=Ncor

##
B1 = Bola("Branca", 30, "couro")
print(B1.mostracor())
B1.trocacor("azul")
print(B1.mostracor())
