from random import randint

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

print('*-----------------------------------------*')
print('|                                         |')
print('|    Bem-vindo ao jogo de batalha naval   |')
print('|    Criador: Diogo Cardoso Lima          |')
print('|    Versão 1.0 - Ano: 2022               |')
print('|                                         |')
print('*-----------------------------------------*')
print('Regras:')
print('1. Cada tabuleiro possui dimensão 3x3 (9 casas).')
print('2. Em cada rodada o computador e o usuário tentam acertar o navio do oponente '
      'selecionando a posição do tabuleiro adversário.')
print('3. Vence a batalha quem afundar primeiro toda a esquadra do adversário.')

# Setup do jogo:
# Número de casas do tabuleiro: 3 x 3
ntable = 3
# Número de navios no tabuleiro: 2
ship = 2
UserAns = False
count =0
while UserAns == False:
    UserAns = str(input('Deseja jogar (s/n)?    '))
    if UserAns == 's':
        # Definição da matriz 8x8 como o tabuleiro (board) zerado.
        board = np.empty((ntable,ntable))
        userboard = np.empty((ntable,ntable))
        # O computador irá inicializar randomicamente a posição dos seus navios (ship = 2 - Ver setup do jogo).
        # Para i de [1;ship[ com passo de 1 em 1, preencha randomicamente ship posições com o número 1.
        while count < ship:
            count = count + 1
            line = randint(0,(ntable-1))
            column = randint(0,(ntable-1))
            if board[line][column] == 1:
                count = count - 1
            else:
                board[line][column] = 1
        # Cheat do jogo: Para ver o tabuleiro do adversário (PC), desabilite o comentário abaixo:
        #plt.imshow(board)
        #plt.colorbar()
        #plt.show()
        count =0
        while count < ship:
            count = count + 1
            line = int(input('Escolha a linha do tabuleiro (0-2): '))
            column = int(input('Escolha a coluna do tabuleiro (0-2): '))
            if (line > (ntable-1)) or (column >(ntable-1)):
                print('A posição deve ser um número de 0 a 2. Repita a seleção, por favor.')
                count = count - 1
            elif userboard[line][column] == 1:
                print('A posição já encontra-se ocupada. Favor, selecione outra posição para o navio.')
                count = count - 1
            else:
                userboard[line][column] = 1
        # Para ver o tabuleiro do usuário:
        #plt.imshow(userboard)
        #plt.suptitle('Tabuleiro do usuário')
        #plt.colorbar()
        #plt.show()
        print('-----------------')
        print(' Início do jogo  ')
        print('-----------------')
        # Inicialização da pontuação:
        userpoint = 0
        cpupoint = 0
        # Enquanto nenhum dos usários chegar a 10 pontos:
        round = 0
        while (userpoint != 2) or (cpupoint !=2):
            print('******************************************')
            print('Placar:')
            print('Usuário:  ', userpoint)
            print('CPU    :  ', cpupoint)
            count = 0
            cpucount=0
            if (cpupoint != 2):
                round = round + 1
                print('*******************************************')
                print('Rodada nº ', round, ' - Escolha do usuário')
                print('-------------------------------------------')
                while count == 0:
                # Rodada inicializada pelo usuário:
                    line = int(input('Escolha a linha para ataque do tabuleiro adversário (0-2):'))
                    column = int(input('Escolha a linha para ataque do tabuleiro adversário (0-2):'))
                    # Se a posição conter o número 2, então a posição já foi selecionada anteriormente.
                    if board[line][column] == 2:
                        print('A posição já foi selecionada. Favor, escolha nova posição.')
                        count=0
                    # Se a posição conter o nímero 1, então a posição contém o navio adversário.
                    # Neste caso, o usuário ganha 1 ponto e a posição recebe o número 2 (ver desc. acima)
                    elif board[line][column] ==1:
                        print('Você acertou o navio adversário e ganhou 1 ponto!')
                        userpoint = userpoint + 1
                        board[line][column] = 2
                        count = count + 1
                    # Se a posição for 0, o usuário não acertou o navio adversário.
                    # Neste caso, a posição recbe o número 2 (ver desc. acima)
                    else:
                        print('Artilharia ao mar! Você não acertou nenhum navio adversário.')
                        board[line][column] = 2
                        count = count+1
            else:
                print('A CPU venceu o jogo !      :/ ')
                print('*******************************************')
                print('*             Fim do Jogo                 *')
                print('*******************************************')
                print('|  Resultado:                             |')
                print('|  Usuário  ', userpoint, '   x   CPU  ', cpupoint, '            |')
                print('------------------------------------------')
                break

            if (userpoint != 2):
                print('- - - - - - - - - * - - - - - - - - - - - -')
                print('Rodada nº ', round, ' - Escolha do adversário')
                while cpucount==0:
                    line = randint(0,(ntable-1))
                    column = randint(0,(ntable-1))
                    # Se a posição conter o número 2, então a cpu sorteou um número já sorteado.
                    # Nenhuma mensagem é exibida.
                    if userboard[line][column] == 2:
                        cpucount = 0
                        # Se a posição conter o nímero 1, então a posição contém o navio adversário.
                    elif userboard[line][column] == 1:
                        print('Boom! O adversário acertou seu navio e ganhou 1 ponto!')
                        cpupoint = cpupoint + 1
                        userboard[line][column] = 2
                        cpucount = cpucount +1
                    # Se a posição for 0, o usuário não acertou o navio adversário.
                    # Neste caso, a posição recbe o número 2 (ver desc. acima)
                    else:
                        print('Passou voando! O adversário não acertou nenhum navio.')
                        userboard[line][column] = 2
                        cpucount = cpucount + 1
            else:
                print(' Você venceu o jogo!      :)')
                print('*******************************************')
                print('*             Fim do Jogo                 *')
                print('*******************************************')
                print('|  Resultado:                             |')
                print('|  Usuário  ', userpoint, '   x   CPU  ',cpupoint,'            |')
                print('------------------------------------------')
                break
        break
    elif UserAns == 'n':
        print('O jogo está encerrado. Obrigado.')
        break
    else:
        print('Resposa inválida.')
        UserAns = False




