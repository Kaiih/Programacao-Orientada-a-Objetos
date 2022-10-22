# 1. Faça um Programa que peça as 4 notas bimestrais e mostre a média simples
# das notas.
print("\n1-\n")
cont = 0
nota1 = float(input("Digite o valor da nota 1: "))
cont = cont + 1
nota2 = float(input("Digite o valor da nota 2: "))
cont = cont + 1
nota3 = float(input("Digite o valor da nota 3: "))
cont = cont + 1
nota4 = float(input("Digite o valor da nota 4: "))
cont = cont + 1
media = (nota1 + nota2 + nota3 + nota4) / cont
print(cont)
print(media)


# 2. Faça um Programa que converta metros para centímetros.
print("\n2-\n")
print("\n\t\t\tCONVERSOR DE METROS EM CENTÍMETROS")
centimetros = float(input("\nDigite quantos metros deseja converter: "))
metros = centimetros * 100
print(metros, " metros")


# 3. Faça um programa para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada. Considere que acobertura
# da tinta é de 1 litro para cada 3 metros quadrados e que a tinta évendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidadede latas
# de tinta a serem compradas e o preço total.
print("\n3-\n")
print("\n\t\tCALCULADORA QUANTIDADE DE TINTAS")
metros = float(input("\nDigite quantos metros você deseja pintar: "))
litros = metros / 3
qntd = litros / 18
valor = qntd * 80
print("Serão necessários %.2i" % litros, "litros de tinta para pintar essa área.")
print("Você precisa comprar %.1f" % qntd, "latas de tinta.")
print("Você irá gastar %.2f" % valor, "reais para pintar essa área.")


# 4. Faça um programa que solicite a média semestral (MS) do aluno ecalcule a
# nota necessária no exame (NE), sabendo-se que a média final (MF) é igual a
# MF = (MS x 6 + NE x 4) / 10.
# Obs: para ser aprovado a MF deve ser >= 5.0
# Nota necessária (NE) = ( 50 - ( MS * 6 ) ) / 4
print("\n4-\n")
MS = float(input("Qual foi a sua média semestral?"))
if MS < 7.0:
    print("\nVocê está em exame!")
    NE = (50 - (MS * 6)) / 4
    print("\nA nota necessária que você precisa tirar no exame é de", NE)
if MS >= 7.0:
    print("\nParabéns, você foi aprovado!")


# 5.Faça um programa que solicite uma distância percorrida por um carro(em
# Km), o consumo de combustível (em litros) da viagem realizada e a distância da
# próxima viagem a ser realizada.
# Com base nestas informações, imprimir:
# a) a média de consumo (km/l) da primeira viagem
# b) a quantidade de combustível que será necessária para realizar a
# próxima viagem.
# c) o total de Km percorridos nas 2 viagens.
# d) o total de combustível gasto nas 2 viagens.
# b) a quantidade de combustível que será necessária para realizar a
# próxima viagem.
# d) o total de combustível gasto nas 2 viagens.
print("\n5-\n")
distancia = float(input("Digite a distância percorrida em km: "))
consumo = float(input("O consumo de combustível em litros foi de: "))
distancia_prox = float(input("Digite a distância que será percorrida na próxima viagem em km: "))
totalkm = distancia + distancia_prox
media = distancia / consumo
qtde_combustivel = distancia_prox / media
Total_combustivel = consumo + qtde_combustivel
print("\na) A media de consumo na primeira viagem foi de ", media, "km/l")
print("b) A quantidade de combustível que será necessária para realizar a próxima viagem é de", qtde_combustivel, "km")
print("c) O total de Km a percorrer nas 2 viagens é de", totalkm, "km")
print("Total de combustível gasto nas 2 viagens: ", Total_combustivel,"litros")


# 6. Faça um Programa que solicite dois números e imprima o maior deles.
print("\n6-\n")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    print("O maior número que você digitou foi o ", num1)
elif num2 > num1:
    print("O maior número que você digitou foi o ", num2)
else:
    print("Os números digitados são iguais ")


# 7) Faça um Programa que solicite um valor e mostre na tela # se o valor
#é positivo ou negativo
print("\n7-\n")
num = int(input("Digite um valor: "))
if num > 0:
    print("O número é positivo!")
elif num < 0:
    print("O número é negativo!")
else:
    print("Você digitou 0.")


# 8)Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F – “Feminino”, M – “Masculino” ou “Sexo
#indeterminado”
print("\n8-\n")
sexo = input("Digite o código do sexo:\nCÓDIGO\tSEXO\nF - Feminino\nM - Masculino  ")
if sexo == "F":
    print("\nFeminino!")
elif sexo == "M":
    print("\nMasculino!")
else:
    print("\nSexo indefinido!")


# 9) Faça um programa para a leitura de duas notas parciais de #um aluno.
#O programa deve calcular a média alcançada por
# aluno e apresentar: A mensagem "Aprovado", se a média #alcançada for
#maior ou igual a sete; A mensagem "Reprovado",
# se a média for menor do que sete; A mensagem "Aprovado com #Distinção", print("\n9-\n")
#se a média for igual a dez
print("\n9-\n")
nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
media = (nota1 + nota2) / 2
print("Média = ", media)
if media == 10:
    print("APROVADO COM DISTINÇÃO!")
if media >= 7 and media < 10:
    print("Aprovado!")
if media < 7:
    print("Reprovado!")


# 10) Faça um Programa que leia três números e mostre o #maior deles
print("\n10-\n")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >= b and a >= c:
    print("O maior número é ", a)
elif b >= a and b >= c:
    print("O maior número é ", b)
elif c >= a and c >= b:
    print("O maior número é ", c)


# 11 - Faça um Programa que leia três números e mostre o #maior e o menor deles.
print("\n11-\n")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if a >= b and a >= c:
    print("O maior número é ", a)
elif b >= a and b >= c:
    print("O maior número é ", b)
elif c >= a and c >= b:
    print("O maior número é ", c)
if a <= b and a <= c:
    print("O menor número é ", a)
elif b <= a and b <= c:
    print("O menor número é ", b)
elif c <= a and c <= b:
    print("O menor número é ", c)


# 12) Faça um programa que pergunte o preço de três produtos e informe qual 
#produto você deve comprar, sabendo que a decisão é sempre pelo mais
#barato.
print("\n12-\n")
p1 = float(input("Valor do primeiro produto: "))
p2 = float(input("Valor do segundo produto: "))
p3 = float(input("Valor do terceiro produto: "))
if p1 <= p2 and p1 <= p3:
    print("Comprar o primeiro produto, custa R$", p1)
elif p2 <= p1 and p2 <= p3:
    print("Comprar o segundo produto, custa R$", p2)
elif p3 <= p1 and p3 <= p2:
    print("Comprar o terceiro produto, custa R$", p3)


# 13) Faça um Programa que leia três números e mostre-os em ordem
#decrescente.
print("\n13-\n")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if a > b and a > c:
    if b > c:
        print('\n', a, b, c)
    else:
        print('\n', a, c, b)
if b > a and b > c:
    if a > c:
        print('\n', b, a, c)
    else:
        print('\n', b, c, a)
if c > a and c > b:
    if a > b:
        print('\n', c, a, b)
    else:
        print('\n', c, b, a)


# 14. Faça um Programa que pergunte em que turno você estuda. Peça para
# digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
#"Bom dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o
#caso.
print("\n14-\n")
turno = input("Qual turno você estuda? \n\tDIGITE:\n M - Matutino\n V - Vespertino\n N - Noturno\n")

if turno != "M" and turno !="m" and turno != "V" and turno != "v" and turno != "N" and turno != "n": 
    print("Valor inválido")
else:
    if turno == "M" or turno =="m":
        print("Bom dia!")
    if turno == "V" or turno =="v":
        print("Boa tarde!")
    if turno == "N" or turno =="n":
        print("Boa noite!")

    


# 15. As Organizações Tabajara resolveram dar um aumento de salário aosseus
# colaboradores e lhe contrataram para desenvolver o programa quecalculará os
# reajustes. Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento
print("\n15-\n")
salario = float(input("Digite o seu salário: "))
print("O seu salário antes do reajuste era: ", salario)
if salario <= 280:
    aumento20 = ((salario * 20) / 100)
    valor20 = aumento20 + salario
    print("O percentual de aumento aplicado é de: ", 20, "%.")
    print("O valor do ajuste é de: ", aumento20)
    print("O seu salario após reajusto é de", valor20)
if salario > 280 and salario <= 700:
    aumento15 = ((salario * 15) / 100)
    valor15 = aumento15 + salario
    print("O percentual de aumento aplicado é de: ", 15, "%.")
    print("O valor do ajuste é de: ", aumento15)
    print("O seu salario após reajusto é de", valor15)
if salario > 700 and salario <= 1500:
    aumento10 = ((salario * 10) / 100)
    valor10 = aumento10 + salario
    print("O percentual de aumento aplicado é de: ", 10, "%.")
    print("O valor do ajuste é de: ", aumento10)
    print("O seu salario após reajusto é de", valor10)
if salario > 1500:
    aumento5 = ((salario * 5) / 100)
    valor5 = aumento5 + salario
    print("O percentual de aumento aplicado é de: ", 5, "%.")
    print("O valor do ajuste é de: ", aumento5)
    print ("O seu salario após reajusto é de",valor5)