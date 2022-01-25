#O que são variáveis?
#São espaços criados na memória ram para serem utilizados na execução do programa.

"""
Nomes de variáveis podem conter apenas: letras, números e underscores
Nome (correto)
nome do aluno (incorreto) - Não pode utilizar espaço
1Bim (incorreto) - Não pode começar com número
"""

saudacao="Olá senhor"
nome="diogo" #Mesmo colocando o nome com letra minúscula, o nome.title() vai iniciar ele com letra maiúscula.
idade=31
nota1=9.7
nota2=9.3
nota3=8.9

print(saudacao, type(saudacao))
print(nome)
print(idade, type(idade))
print(nota1, type(nota1))

nota_final=(nota1+nota2+nota3)/3
print("A nota final do aluno " + nome.title()+ " foi de",nota_final,"pontos",sep=' ')