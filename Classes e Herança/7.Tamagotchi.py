# 7) Classe Animal de Estimação Virtual: crie uma classe que modele um Tamagotchi (Bichinho Eletrônico):
# - Atributos: Nome, Fome, Saúde e Idade
# - Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# *Obs: Existe mais uma informação que devemos levar em consideração, o Humor do tamagotchi, que é uma combinação entre
# os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação
# por que ela pode ser calculada a qualquer momento.

class Bichinho:
    nome = None

    def __init__(self, nome, idade=0, fome=50, saude=50):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude

    def envelhecer(self):
        if self.saude > 10:
            print("\n1 Ano depois...")
            self.idade = self.idade + 1
            self.saude = self.saude - 10
        else:
            print("\nTamagotchi está morrendo, tente medicá-lo!")

    def alimentar(self):
        if self.fome < 100:
            print("\nNhac, nhac...")
            self.fome = self.fome + 10
        else:
            print("\nEstou cheia(o)!")

    def medicar(self):
        if self.saude < 100:
            print("\n...")
            self.saude = self.saude + 10
        else:
            print("\nEstou saudável!")

    def retornaridade(self):
        return print(self.nome, "tem", self.idade, "anos.")

    def retornarfome(self):
        if self.saude > 50:
            if self.fome > 50:
                print("O humor está ótimo")
        print("O nível da fome está em", self.fome, "%.")

    def retornarsaude(self):
        if self.saude > 50:
            if self.fome > 50:
                print("O humor está ótimo")
        return print("O nível de saúde está em", self.saude, "%.")

    def retornarnome(self):
        return print("O nome do seu Tamagotchi é", self.nome)


p1 = Bichinho("Bili")
p1.retornarnome()
p1.retornarsaude()
p1.retornaridade()
p1.retornarfome()
p1.envelhecer()
p1.retornarsaude()
p1.medicar()
p1.alimentar()
p1.retornarsaude()
p1.retornaridade()
p1.retornarfome()