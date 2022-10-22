################################################
#6) Classe TV: Faça um programa que simule um televisor criando-o
#como um objeto. O usuário deve ser capaz de
#informar o número do canal e aumentar ou diminuir o volume.
#Certifique-se de que o número do canal e o nível do volume
#permanecem dentro de faixas válidas.

class TV:
    def __init__(self, numCanal=1, volume=20):
        self.numCanal = numCanal
        self.volume = volume
    
    def aumentarVolume(self):
        if self.volume >=0 and self.volume <40:
            self.volume = self.volume + 1
            print("Vol", self.volume)
        else:
            print("Vol", self.volume)
    
    def diminuirVolume(self):
        if self.volume >0 and self.volume <=40:
            self.volume = self.volume - 1
            print("Vol",self.volume)
        else:
            print("Vol", self.volume)
    
    def mudarCanal(self):
        print("Você está no canal",self.numCanal)
        self.numCanal = int(input("Digite o número do canal que você deseja ir: "))
        
        while self.numCanal < 1 or self.numCanal >25:
            print("CANAL INVÁLIDO!")
            self.numCanal = int(input("\nDigite o número do canal que você deseja ir: "))
            print("Você está no canal", self.numCanal)

#####
TV1 = TV()
TV1.aumentarVolume()
TV1.diminuirVolume()
TV1.mudarCanal()