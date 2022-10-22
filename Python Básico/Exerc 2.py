#1-Faça um programa que leia quatro números informados pelo usuário e que depois imprima a
#média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.

num1 = int(input("\n1-\nDigite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
media = (num1*1 + num2*2 + num3*3 + num4*4)/(1+2+3+4)
print("A média ponderada desses valores é ", media)

#2-Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas
#oferecendo desconto. Faça um programa que possa receber um valor de um produto e um
#valor de desconto. Calcule e imprima o novo valor do produto

valor = float(input("\n2-\nDigite o valor de um produto: "))
desconto = float(input("Digite o valor do desconto: "))
valorfinal = valor - desconto
print("O valor com o desconto é de ", valorfinal)

#3-Uma pessoa resolveu fazer uma aplicação em uma poupança programada. Para calcular seu
#rendimento, ela deverá fornecer o valor constante da aplicação mensal, a taxa e o número de meses.
#Use a fórmula ao lado, sabendo-se que: i = taxa, P = aplicação mensal e n= número de meses.

valor = float(input("\n3-\nForneça o valor da aplicação mensal: "))
taxa = float(input("Qual é o valor da taxa? "))
meses = int(input("De quantos meses é essa aplicação? "))
rendimento = ((1+taxa**meses-1)/taxa)*valor
print("O seu rendimento é de %f"%rendimento)

#4-Faça um programa que calcule o valor em Reais, correspondente aos dólares que um turista
#possui no cofre do hotel. O programa deve solicitar os seguintes dados: Quantidade de dólares
#guardados no cofre e cotação do dólar naquele dia.

valordol = float(input("\n4-\nQuantos dólares você tem no cofre? "))
cotacao = float(input("Qual a cotação do dólar no dia de hoje? "))
valorreal = valordol * cotacao
print ("O valor em reais que tem no cofre é de: ", valorreal)

#5-A Loja Magazine Litoral está vendendo seus produtos em diversas prestações sem juros. Faça um programa que receba
#um valor de uma compra, o número de prestações e mostre o valor de cada prestações.

valortt = float(input("\n5-\nDigite o valor do produto: "))
num_prest = int(input("Digite em quantas prestações você pagará: "))
valor_prest = valortt / num_prest
print("O valor de cada prestação será de R$", valor_prest)