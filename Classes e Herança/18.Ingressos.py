# 18. Crie uma classe chamada Ingresso que possui um valor em reais e um métodoimprimeValor().
# a) crie uma classe VIP, que herda Ingresso e possui um valor adicional.
# Crie um método que retorne o valor do ingresso VIP (com o adicional incluído).
# b) crie uma classe Normal, que herda Ingresso e possui um método que imprime: "Ingresso Normal".
# c) crie uma classe CamaroteInferior (que possui a localização do ingresso e
#métodos para acessar e imprimir esta localização) e uma classe CamaroteSuperior,
# que é mais cara (possui valor adicional).
# Esta última possui um método para retornar o valor do ingresso. Ambas as classes herdam a classe VIP.
# Tarefa: Com base no exemplo acima, escrever um programa que solicite ao usuário a quantidade de ingressos que deseja e
# imprimir o valor a ser pago, considerando os valores de ingressos acima e as classes criadas.

class ingresso:
    valor = None

    def __init__(self, valor):
        self.valor = valor

    def imprimevalor(self):
        return self.valor


class vip(ingresso):
    valorAdicionalVip = None

    def __init__(self, valor, valorAd):
        super().__init__(valor)
        self.valorAdicionalVip = valorAd

    def getingressovip(self):
        return self.valor + self.valorAdicionalVip

class normal(ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def getingressonormal(self):
        return self.valor


class camaroteinferior(vip):
    localizacao = None
    valoradicionalcamaroteinf = None

    def __init__(self, valor, valorAd, localizacao, valoradicionalcamaroteinf):
        super().__init__(valor, valorAd)
        self.localizacao = localizacao
        self.valoradicionalcamaroteinf = valoradicionalcamaroteinf

    def getvalorcamaroteinferior(self):
        return self.valoradicionalcamaroteinf + self.valorAdicionalVip + self.valor

    def getlocalizacao(self):
        return self.localizacao

    def setlocalizacao(self, localizacao):
        self.localizacao = localizacao


class camarotesuperior(vip):
    valoradicionalcamarotesup = None

    def __init__(self, valor, valorad, valoradicionalcamarotesup):
        super().__init__(valor, valorad)
        self.valoradicionalcamarotesup = valoradicionalcamarotesup

    def getvalorcamarotesuperior(self):
        return self.valoradicionalcamarotesup + self.valorAdicionalVip + self.valor


####
ingressonormal = normal(15)
ingressovip = vip(15, 5)
ingressocamaroteinferior = camaroteinferior(15, 5, "Área Sul", 5)
ingressocamarotesuperior = camarotesuperior(15, 5, 10)
print("1 - Ingresso normal - R$", ingressonormal.getingressonormal())
print("2 - Ingresso vip - R$", ingressovip.getingressovip())
print("3 - Ingresso camarote inferior - R$", ingressocamaroteinferior.getvalorcamaroteinferior(), "- Local: ", ingressocamaroteinferior.getlocalizacao())
print("4 - Ingresso camarote superior - R$", ingressocamarotesuperior.getvalorcamarotesuperior())
a = 0
b = 0
c = 0
d = 0

while True:
    qntd = int(input("\nAdicione os ingressos no carrinho (5 - Finalizar/SAIR): "))
    if qntd == 1:
        print("+1 Ingresso normal")
        a += 1
    if qntd == 2:
        print("+1 Ingresso Vip")
        b += 1
    if qntd == 3:
        print("+1 Camarote inferior")
        c += 1
    if qntd == 4:
        print("+1 Camarote superior")
        d += 1
    if qntd == 5:
        print("Saindo...\n")
        break
    if qntd != 1 and qntd != 2 and qntd != 3 and qntd != 4 and qntd != 5:
        print("Opção inválida, tente novamente!")

total_normal = ingressonormal.getingressonormal() * a
total_vip = ingressovip.getingressovip() * b
total_camaroteinf = ingressocamaroteinferior.getvalorcamaroteinferior() * c
total_camarotesup = ingressocamarotesuperior.getvalorcamarotesuperior() * d
tt = total_normal + total_vip + total_camaroteinf + total_camarotesup
print("Quantidade: ", a + b + c + d, "itens.")
print("Valor total = R$", tt)

#######################