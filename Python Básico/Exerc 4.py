#1) Entrar com um número e imprimi-lo caso seja maior que 20.
print("\n1-")

num1 = int(input("Digite um número: "))
if num1 > 20:
    print("O número digitado foi ",num1)


#2) Construir um programa que leia dois valores numéricos inteiros
#e efetue a adição, caso o resultado seja maior que 10,
#apresentá-lo.
print("\n2-")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2
if soma > 10:
    print("A soma dos dois números digitados foi: ", soma)


#3) Construir um programa que leia dois números e efetue a adição.
#Caso o valor somado seja maior que 20, este deverá
#ser apresentado somando se a ele mais 8; caso o valor somado seja
#menor ou igual a 20, este deverá ser apresentado subtraindo se 5.
print("\n3-")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2
if soma > 20:
    print("A soma dos dois números digitados + 8 é de: ", soma+8)
if soma <= 20:
    print("A soma dos dois números digitados - 5 foi de: ", soma - 5)


#4) Entrar com um número e imprimir a raiz quadrada do número caso
#ele seja positivo e o quadrado do número caso ele seja negativo.
print("\n4-")

num1 = int(input("Digite um número: "))
if num1 >=0:
    raiz = num1 ** 2
    print("A raiz quadrada do número é: ", raiz)
if num1 < 0:
    quadrado = num1 * num1
    print("O quadrado do número é: ", quadrado)


#5) Escreva um programa que pergunte a distância que um passageiro
#deseja percorrer em km. Calcule o preço da
#passagem, cobrando RS 0,50 por km para viagens de até 200 km, e
#RS 0,45 para viagens mais longas. (Obs: valores em Reais)
print("\n5-")

distancia = float(input("Digite a distância que deseja percorrer em km: "))
if distancia <= 200:
    valor = distancia * 0.50
    print ("O valor da passagem é de ", valor)
if distancia > 200:
    valor2 = distancia * 0.45
    print("O valor da passagem é de ", valor2)


#6) Entrar com um número e informar se ele é ou não divisível por 5
print("\n6-")

num1 = int(input("Digite um número: "))
if num1 % 5 == 0:
    print("O número ",num1," é divisível por 5")
if num1 % 5 != 0:
    print("O número ",num1," não é divisível por 5")


#7) Entrar com um número e informar se ele é divisível por 3 e por 7
print("\n7-")

num1 = int(input("Digite um número: "))
if num1 % 3 == 0:
    print("O número ",num1," é divisível por 3")
else:
    print ("O número ",num1," não é divisível por 3")
if num1 % 7 == 0:
    print("O número ", num1, " é divisível por 7")
else:
    print("O número ", num1, " não é divisível por 7")


#8) A prefeitura do Rio de Janeiro abriu uma linha de crédito para
#os funcionários estatutários. O valor máximo da
#prestação não poderá ultrapassar 30% do salário bruto. Fazer um
#programa que permita entrar com o salário bruto e o
#valor da prestação e informar se o empréstimo pode ou não ser concedido.
print("\n8-")

salario_bruto = float(input("Digite o seu salário bruto: "))
valor_prestacao = float(input("Digite o valor da prestação: "))
limite = salario_bruto + (salario_bruto * 0.3)
if valor_prestacao <= limite:
    print ("O empréstipo pode ser concedido")
else:
    print("O empréstipo não pode ser concedido")


#9) Ler um número inteiro de 3 dígitos, e imprimir se o algarismo
#da casa das centenas é par ou ímpar.
print("\n9-")

num1 = int(input("Digigte um número com 3 dígitos: "))
centena = num1 // 100
if centena % 2 == 0:
    print("O número da casa das centenas é o", centena)
    print("Esse número é par")
else:
    print("O número da casa das centenas é o", centena)
    print("Esse número é ímpar")


#10) Escreva um programa que leia dois números e que pergunte qual
#operação o usuário deseja realizar. Deve-se poder
#calcular a soma (+), subtração (-), multiplicação (*) e divisão
#(/). Exiba o resultado da operação solicitada.
print("\n10-")

num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))
print( "\n\tTABELA \n S = Soma\n D = divisão \n M = multiplicação \n SB = Subtração")
realizar = input("\nDigite a operação que deseja realizar: ")
if realizar == "S":
    soma = num1 + num2
    print (soma)
if realizar == "M":
    multiplicacao = num1 * num2
    print (multiplicacao)
if realizar == "D":
    divisao = num1 / num2
    print (divisao)
if realizar == "SB":
    subtracao = num1 - num2
    print (subtracao)