#Importa biblioteca regex (expressões regulares)
import re
phrase = 'O rato roeu a roupa do rei de Roma'

if 'rato' in phrase:
    print('Palavra encontrada.')
# contador da palavra rato
    print('ocorrência: ',phrase.count('rato'))
else:
    print('Palavra não encontrada.')