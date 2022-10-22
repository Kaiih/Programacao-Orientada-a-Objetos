################################################
#3) Classe Retangulo: Crie uma classe que modele um
#retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base 
#e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados,
#calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao
#usuário que informe as medidades de um local. Depois,
#devecriar um objeto com as medidas e calcular a quantidade
#de pisos e de rodapés necessárias para o local.

class Retangulo:
    comprimento = None
    largura = None
    
    def __init__(self,comprimento,largura):
        self.ladoA = comprimento
        self.ladoB = largura
    
    def retornarlados(self):
        return self.ladoA, self.ladoB
    
    def mudarlados(self, Ncomprimento, Nlargura):
        self.ladoA = Ncomprimento
        self.ladoB = Nlargura
    
    def calcularArea(self):
        return (self.ladoA * self.ladoB)
    
    def calcularperimetro(self):
        return 2 * (self.ladoA + self.ladoB )

####
comp = float(input("Digite o comprimento do local: "))
larg = float(input("Digite a largura do local: "))
local = Retangulo(comp,larg)
print("\nO comprimento e largura do lugar respectivamente é de:",local.retornarlados())
print("Serão necessários %.2f" % local.calcularArea(),"m2 depiso.")
print("Serão necessários %.2f" % local.calcularperimetro(),"m2 derodapé.")
