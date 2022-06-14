from random import randint
win = 0
while True:
    print('-=' * 12)
    print('VAMOS JOGAR PAR OU ÍMPAR!')
    print('-='* 12)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('Você jogou {} e o computador {}. Total de {}... '.format(jogador, computador, total), end = '')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if opcao == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            win += 1
        else:
            print('Você PERDEU!')
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            win += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('GAME OVER... Você venceu {} vezes..'.format(win))














