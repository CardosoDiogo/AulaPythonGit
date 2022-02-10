print('========== Votação ===========')
nmax=3


candidates = list(range(0,nmax))
candidatesnumb = list(range(0,nmax))
for i in candidates:
    candidates[i] = input('Digite o nome do candidato: ')
    candidatesnumb[i] = int(input('Digite o número do candidato: '))

nvotes = int(input('Defina número de eleitores: '))
votes = list(range(0,nvotes))

print('****** Votação ********')
for i in votes:
    votes[i] = int(input('Digite o número do seu candidato: '))

count1 = 0
count2 = 0
count3 = 0
for i in votes:
    if i == candidatesnumb[0]:
        count1 = count1+1
    elif i == candidatesnumb[1]:
        count2=count2+1
    else:
        count3=count3+1

if count1 > count2:
    if count1 > count3:
        if count3 > count2:
            winner = candidates[0]
            second = candidates[2]
            third = candidates[1]
            countw = count1
            counts = count3
            countt = count2
        else:
            winner = candidates[0]
            second = candidates[1]
            third = candidates[2]
            countw = count1
            counts = count2
            countt = count3
    else:
        winner = candidates[2]
        second = candidates[0]
        third = candidates[1]
        countw = count3
        counts = count1
        countt = count2
else:
    if count2 > count3:
       if count3 > count1:
           winner = candidates[1]
           second = candidates[2]
           third = candidates[0]
           countw = count2
           counts = count3
           countt = count1
       else:
           winner = candidates[1]
           second = candidates[0]
           third = candidates[2]
           countw = count2
           counts = count1
           countt = count3
    else:
        winner = candidates[2]
        second = candidates[1]
        third = candidates[0]
        countw = count3
        counts = count2
        countt = count1

print(' Vencedor com ',countw, ' votos foi o candidato ',winner)
print(' Percentual dos votos: ',100*(countw/nvotes),' %')
print(' Segundo colocado com ',counts, ' votos foi o candidato ',second)
print(' Percentual dos votos: ',100*(counts/nvotes),' %')
print(' Terceiro colocado com ',countt, ' votos foi o candidato ',third)
print(' Percentual dos votos: ',100*(countt/nvotes),' %')

