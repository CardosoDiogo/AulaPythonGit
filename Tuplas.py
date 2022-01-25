#Tuplas são criadas e não podem ser modificadas em tempo de execução:
dimensoes = (200,50,30,58,70)
print(dimensoes[0])
print(dimensoes[1])

print('-----------')
print("Percorrendo elementos da tupla")
for elemento in dimensoes:
    print(elemento)

#Lista
nome = [200,50] # Lista
print(nome[0])
print(nome[1])

#Dictionary - Defined by: {}
Juan = {'Matemática': 10,'História':7.5,'Geografia':6.0,'Biologia':9.0}
for notas in Juan:
    print(notas)