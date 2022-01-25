#Lista com 5 nomes digitados pelo usuário. Depois exibir os nomes que estão cadastrados.

nomes=[]
i=0

while i<=4:
    nomes.append(input("digite o nome"))
    i=i+1

print(nomes)

print('-----------------')
nomes2=[]
resposta= 's'
while resposta == 's':
    nomes2.append(input('Digite o nome: '))
    resposta = input('Deseja continuar?')

print(nomes2)