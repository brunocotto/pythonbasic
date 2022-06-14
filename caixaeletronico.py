print('='*30)
print('{:^30}'.format('BANCO NUBANK'))
print('='*30)
saque = int(input('Qual valor você deseja sacar? '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced += 1
    else:
        if totced > 0:
            print('Total de {} cédulas de R${} reais'.format(totced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Obrigado! O Nubank agradece a preferência...')
