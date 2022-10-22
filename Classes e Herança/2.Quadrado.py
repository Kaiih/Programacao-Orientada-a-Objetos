################################################
# 2) Classe Quadrado: Crie uma classe que #modele um quadrado:
# Métodos: Mudar valor do Lado, Retornar valor do Lado e #calcular Área;
class Quadrado:
    Tam = None
    area = None
    
    def __init__(self, Tam):
        self.Tam = Tam
    
    def mudarTam(self, NTam):
        self.Tam = NTam
    
    def retornarTam(self):
        print("Tamanho:")
        return self.Tam
    
    def calculeArea(self):
        print("Area: ")
        return (self.Tam * 2)

Q1 = Quadrado(200)
print(Q1.retornarTam())
Q1.mudarTam(100)
print(Q1.retornarTam())
print(Q1.calculeArea())