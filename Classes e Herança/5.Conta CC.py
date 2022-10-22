################################################
#5) Classe Conta Corrente: Crie uma classe para implementar uma
#conta corrente. A classe deve possuir os seguintes
#atributos: número da conta, nome do correntista e saldo. Os
#métodos são os seguintes: alterarNome, depósito e saque;
#No construtor, saldo é opcional, com valor default zero e os
#demais atributos são obrigatórios.

class conta_corrente:
    numero = None
    nome = None
    saldo = None
    
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self):
        Nnome = input("Digite o nome: ")
        self.nome = Nnome
    
    def deposito(self):
        mais = float(input("Digite o valor que foi depositado: "))
        self.saldo += mais
    
    def saque(self):
        menos = float(input("Digite o valor que foi sacado: "))
        self.saldo -= menos

    def mostrardados(self):
        return print("\nCaro(a)",self.nome,", o número da sua conta é", self.numero, "e o seu saldo atual é de", self.saldo,"reais.")

##
c1 = conta_corrente(151547,"Bruno")
c1.mostrardados()
c1.deposito()
c1.mostrardados()
c1.saque()
c1.mostrardados()
c1.alterarNome()
c1.mostrardados()
