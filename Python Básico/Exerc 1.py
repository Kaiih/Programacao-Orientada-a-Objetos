#1-Considerando que um círculo tem raio=5, escreva um programa que calcule a área
#deste círculo, lembrando que área = π ⋅ r2
area = float(3.14 * 5**2)

print ("\n1-\nA area do circulo é de ",area)

############
#2-Considerando que um carro percorreu 140 km e consumiu 11 litros de combustível.
#Escreva um programa que calcula o consumo de gasolina deste carro em quilômetros
#por litro, imprimindo a resposta. 

print ("\n2-\n")
consumopkm = 11/140

print("O consumo de gasolina por km é de ",consumopkm)

############
#3-Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas
#oferecendo desconto. Faça um programa que calculo o valor a ser pago por um produto
#considerando o custo inicial de R$ 153,00 e o desconto de 20%. 
print("\n3-\n")
custo = 153
desconto = (custo * 20)/100
valortt = float(custo - desconto)

print("O valor a ser pago pelo produto é de ",valortt)

############
#4-Faça um programa que receba o peso e a altura de uma pessoa e calcule o índice de
#massa corpórea (peso em Kg, dividido pelo quadrado da altura em metros). 

peso = float(input("\n4-\nQual é o seu peso? "))
altura = float(input("Qual é a sua altura ? "))

imc = peso/(altura**2)

print("O seu imc é de ", imc)

############
#5-Faça um programa que receba o custo de um espetáculo teatral e o preço do convite
#esse espetáculo. Esse programa deve calcular e mostrar:
#a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do
#espetáculo seja alcançado.
#b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%. 

custo = float(input("\n5-\nQual o valor de custo do espetáculo teatral? "))
convite = float(input("Qual o valor do convite? "))

quantidade = int(custo/convite)
lucro = (123 * custo)/100
quantlucro = int(lucro/convite)

print("É preciso vender",quantidade,"ingressos para alcançar o custo do espetáculo.")
print ("É preciso vender",quantlucro,"ingressos para alcançar o um lucro de 23%.")

############
#6-Considerando uma eleição de apenas 2 candidatos, elabore um programa que leia do
#teclado o número total de eleitores, o número de votos do primeiro candidato e o
#número de votos do segundo candidato. Em seguida, o programa deverá apresentar o
#percentual de votos de cada um dos candidatos e o percentual de eleitores ausentes.

votostt = int(input("\n6-\nDigite o número total de eleitores:"))
votos1 = int(input("Digite o número de votos do eleitor 1:"))
votos2 = int(input("Digite o número de votos do eleitor 2:"))

porc1 = (votos1/votostt)*100
porc2 = (votos2/votostt)*100

print("A porcentagens de votos do candidato 1 é: ", porc1,"%")
print("A porcentagens de votos do candidato 2 é: ", porc2,"%")


