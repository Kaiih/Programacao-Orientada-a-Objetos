################################################
# 4) Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    nome = None
    idade = None
    peso = None
    altura = None
    Npeso = None
    
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.05
            self.idade += 1
            print("1 Ano depois...")
    
    def engordar(self):
        Npeso = float(input("Digite quantos KG a pessoa engordou:"))
        self.peso += Npeso
    
    def emagrecer(self):
        Mpeso = float(input("Digite quantos KG a pessoa emagreceu:"))
        self.peso -= Mpeso

    def crescer(self):
        Naltura = float(input("Digite quantos CM a pessoa cresceu:"))
        self.altura += (Naltura / 100)
    
    def mostrarpessoa(self):
        return print("\nNome:", self.nome, "\nIdade:", self.idade,"\nPeso:", self.peso, "\nAltura:", "%.2f" % self.altura, "\n")

###
kailane = Pessoa('Kailane', 19, 45, 1.57)
kailane.mostrarpessoa()
kailane.envelhecer()
kailane.mostrarpessoa()
kailane.engordar()
kailane.mostrarpessoa()
kailane.emagrecer()
kailane.mostrarpessoa()
kailane.crescer()
kailane.mostrarpessoa()
