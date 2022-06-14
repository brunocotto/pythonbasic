print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
total = tot1000 = menor = count = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    p = float(input('Preço: R$'))
    count += 1
    total += p
    if p >= 1000:
        tot1000 += 1
    if count == 1 or p < menor:
        menor = p
        barato = nome
    print('-' * 20)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi de R${} reais.'.format(total))
print('Temos {} produto custando mais de R$1000 reais.'.format(tot1000))
print('O produto mais barato foi {} e custa R${} reais.'.format(barato, menor))


