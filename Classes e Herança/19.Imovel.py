######################
#19. Crie a classe Imovel, que possui um endereço e um preço.
# a) crie uma classe Novo, que herda Imovel e possui um adicional no preço.
#Crie métodos de acesso e impressão deste valor adicional.
# b) crie uma classe Usado, que herda Imovel e possui um desconto no preço.
#Crie métodos de acesso e impressão para este desconto
class imovel:
    endereco = None
    preco = None
    
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco
    
    def getpreco(self):
        return self.preco
    
    def getendereco(self):
        return self.endereco

class novo(imovel):
    adicional = None
    
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco,preco)
        self.adicional = adicional
    
    def setAdicional(self,adicional):
        self.adicional = adicional
    
    def getAdicional(self):
        return self.adicional

class usado(imovel):
    desconto = None
    
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto
    
    def setDesconto(self, desconto):
        self.desconto = desconto
    
    def getDesconto(self):
        return self.desconto

########
casa1 = novo("Progresso", 1500,200)
casa2 = usado("Progresso", 1500, 100)
print("Imovel %s valor R$ %.2f" % (casa1.getendereco(),casa1.getpreco() +casa1.getAdicional()))
print("Imovel %s valor R$ %.2f" % (casa2.getendereco(),casa2.getpreco() +casa2.getDesconto()))