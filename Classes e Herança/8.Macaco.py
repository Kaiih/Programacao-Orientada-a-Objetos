################################################
#8) Classe Macaco: Desenvolva uma classe Macaco,que possua os
#atributos nome e estomago e pelo menos os métodos
#comer(), verBarriga() e digerir().
#Faça um programa ou teste interativamente, criando pelo menos
#dois macacos, alimentando-os com pelo menos 3
#alimentos diferentes e verificando se está alimentado (se tem
#barriga) a cada refeição.

class macaco:
    
    def __init__(self, nome):
        self.barriga = False
        self.nome = nome
    
    def comer(self):
        print("\nTABELA: \nB - Banana \nU - Uva \nH - Hambúrguer\nP - Pizza\n")
        comida = input("Digite o que o macaco vai comer: ")
        while comida != "B" and comida != "b" and comida != "U" and comida != "u" and comida != "H" and comida != "h" and comida != "P" and comida != "p":
            comida = input("Digite o que o macaco vai comer('fim'para sair): ")
            if comida =="fim":
                print("\n\t\tSaindo!\n")
                break
            if comida == "B" or comida == "b":
                self.barriga = False
            if comida == "U" or comida == "u":
                self.barriga = False
            if comida == "H" or comida == "h":
                self.barriga = True
            if comida == "P" or comida == "p":
                self.barriga = True
    
    def verbarriga(self):
        return print("Barriga:",self.barriga)
    
    def vernome(self):
        return print("\nNome:",self.nome)
    
    def digerir(self):
        print("Digerindo...")
        self.barriga = False

###########
M1 = macaco("Boris")
M1.vernome()
M1.comer()
M1.verbarriga()
M2 = macaco("Oliver")
M2.vernome()
M1.verbarriga()
M1.comer()
M1.verbarriga()
M1.digerir()
M1.verbarriga()