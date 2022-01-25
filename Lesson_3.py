# Declaração de uma lista:
nomes = ['A','B','C','D','E','F']

#Listar um único elemento:
print(nomes[2].title())
#Para pegar o último elemento
print(nomes[-1])

#Para pegar o penúltimo elemento
print(nomes[-2])

#Para adicionar a lista:
nomes.append('G')
print(nomes)
#Inserir novos elementos na lista em posição determinada:
novos_nomes=['H','I','J']
nomes.insert(1,'K')
print(nomes)

#Apagar um elemento da linha:
del(nomes[0])
print(nomes)

#Definindo um vetor misto:
Vec=[1,2,3,4,5,'A','B','C','D','E']
print(Vec)
Vec2 = [1,2,3,4,5]
Vec[0]=Vec2[0]+Vec[0]
print(Vec[0])

#Ordenar elementos
Vec3=[3,2,4,5,3,1,1,1,3,4,6,7,9,10,11,13,3]
Vec3.sort()
print(Vec3)
#Ordenar elementos sem alterar a listagem original
Vec4=[3,2,4,5,3,1,1,1,3,4,6,7,9,10,11,13,3]
print(sorted(Vec4))
#Ordem reversa - Vec4.reverse()
#print(Vec4.reverse())
#Tamanho da lista
print('Tamanho da lista: ',len(Vec4))

#Matriz:
A=[[1,2,3],[4,5,6],[7,8,9]]


#Criando listas numéricas - range()
numero=1
while numero <= 5:
    print(numero)
    numero=numero+1
print('---------')
numero=1
while numero <=5:
    print(numero)
    numero+=1 #Mesma funcionalidade de contador

