#########################
#13) Classe Funcionário: Implemente a classe Funcionário. Um
#empregado tem um nome (um string) e um salário(umdouble). Escrevaum construtor
# com dois parâmetros (nome e salário) e métodos para devolver
#nome e salário. Método aumentarSalario (porcentualDeAumento) queaumente o salário
# do funcionário em uma certa porcentagem. Exemplo de uso:
# harry=funcionário("Harry",25000)
# harry.aumentarSalario(10)

class funcionario:
    nome = None
    salario = None
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def getnome(self):
        print("Funcionário(a):")
        return self.nome
    
    def getsalario(self):
        print("Último salário:")
        return self.salario
    
    def aumentarsalario(self, nsalario):
        self.salario = self.salario + ((self.salario * nsalario) /100)

#####
Ana = funcionario("Ana", 1500)
print(Ana.getnome())
print(Ana.getsalario())
Ana.aumentarsalario(50)
print(Ana.getsalario())