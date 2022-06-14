from random import randint
from time import sleep
acertou = False
tent = 0
jogador = 0
computador = randint(0, 10) #processa um valor randômico
print('-=-' * 16)
print('Vou pensar em um número de 0 a 10, tente adivinhar!')
print('-=-' * 16)
jogador = int(input('Qual seu palpite? '.format(computador, jogador)))
while not acertou:
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            jogador = int(input('Mais... Não foi dessa vez! Tente novamente: '.format(computador, jogador)))
        else:
            jogador = int(input('Menos... Não foi dessa vez! Tente novamente: '.format(computador, jogador)))
        tent += 1
print('PROCESSANDO...')
sleep(3)
print('Parabéns! Você conseguiu me vencer! Você precisou de {} tentativas!'.format(tent + 1))
