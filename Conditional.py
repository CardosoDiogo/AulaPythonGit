#Exercício 5 - Escrever um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor
x=int(input("Digite um número inteiro: "))
print('O antecessor de ',x,' é ',x-1)
print('-------------------------------')
#Exercício 6 - Escreva um algoritmo para ler as dimensões de um retânculo (base e altura),
# calcular e escrever a área do retângulo.
base=float(input('Digite a medida da base (m): '))
altura=float(input('Digite a medida da altura (m): '))
Area=base*altura
print('A área do retângulo é de ',Area,'m².')
print('-------------------------------')
#Exercício 7 - Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
# dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
print('Digite a sua idade em anos, meses e dias')
anos=int(input('Digite a sua idade em anos: '))
meses=int(input('Digite a sua idade em meses: '))
dias=int(input('Digite a sua idade em dias: '))
print('A sua idade em dias é de ',anos*365+meses*30+dias,' dias.')
print('-------------------------------')
#Exercício 8 - Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos,
#nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.
eleitores=int(input('Digite o número total de eleitores: '))
validos=int(input('Digite o número total de votos válidos: '))
brancos=int(input('Digite o numero total de votos brancos: '))
nulos=int(input('Digite o número total de votos nulos: '))
if (eleitores >= 0) and (brancos >= 0) and (brancos >=0) and (nulos >=0) and (validos+brancos+nulos == eleitores):
    print('Percentual de votos válidos: ', (validos / eleitores) * 100)
    print('Percentual de votos brancos: ', (brancos / eleitores) * 100)
    print('Percentual de votos nulos: ', (nulos / eleitores) * 100)
else:
    print('Necessário revisar a entrada de dados.')
print('-------------------------------')
#Exercício 9 - Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
#Calcular e escrever o valor no novo salário.
salario=float(input('Digite o valor do salário mensal: '))
reajuste=float(input('Digite o valor do reajuste em valores percentuais (%): '))
reajuste = reajuste/100

print('O novo salário reajustado será de R$ ',salario*(1+reajuste))
print('-------------------------------')
#Exercício 10 - O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor
# e dos impostos (aplicados ao custo da fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos
# de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final do consumidor.
custo_fab = float(input('Digite o custo de fábrica: '))
perc_dist = 0.28 #28%
impostos = 0.45 #45%
custo = custo_fab * (1+perc_dist+impostos)
print('O custo total do veículo será de R$ ',custo)
#Exercícios 12 - Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
#correspondente em graus Celsius (baseado na fórmula abaixo): C/5 = (F-32)/9
F=float(input('Digite a temperatura em °F: '))
print('A temperatura corresponde a ', 5*(F-32)/9,' °C.')
print('-------------------------------')
#Exercício 13 - Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
# Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:
# Media Final = (n1*2+n2*3+n3*5)/10
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
Media=(nota1*2+nota2*3+nota3*5)/10
print('Média final do aluno: ',Media)

#Exercício 14 - Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário
# escrever NÃO É MAIOR QUE 10!.
num=float(input('Digite um número: '))
if num > 10:
    print('O número é maior que 10.')
else:
    print('O número não é maior que 10')

#Exercício 15 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como postivo):
numm = float(input('Digite um número: '))
if num >= 0:
    print('O número é positivo')
else:
    print('O número é negativo')

#Exercício 16 - As maças custam R$1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas
# pelo menos 12. Escreva um programa que leia o número de maças compradas, calcule e escreva o custo total da compra.
num = int(input('Digite o número de maças compradas: '))
if num >= 12:
    print('Valor total foi de ',num,' Reais.')
else:
    print('Valor total foi de', num*1.3,' Reais.')

#Exercício 17 - Ler a 1ª e 2ª nota de avaliações de um aluno. Calcular a média aritmética simples e escrever uma
# mensagem que diga se o aluno foi ou não aprovado (considerar a nota maior ou igual a 6 o aluno foi aprovado).
# Escrever também a média calculado.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2
if media >= 6:
    print('O aluno foi aprovado com média ',media)
else:
    print('O aluno foi reprovado com média ',media)

#Exercício 19 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.
num1=1
num2=1
while num1 == num2:
    if num1 == num2:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        if num1>num2:
            print('O número ',num1,' é maior que ',num2)
        elif num1<num2:
            print('O número ',num1,' é menor que ',num2)

#Exercício 20 - Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
num1=1
num2=1
while num1 == num2:
    if num1 == num2:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        if num1>num2:
            print('Ordem crescente: ',num2,' , ',num1)
        elif num1<num2:
            print('Ordem crescente: ',num1,' , ',num2)
