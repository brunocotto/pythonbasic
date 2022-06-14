maior = 0
homens = 0
m20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-' * 20)
    if idade >= 18:
            maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
            m20 += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('{} pessoas tem mais de 18 anos..'.format(maior))
print('{} homens foram cadastrados..'.format(homens))
print('{} mulheres tem menos de 20 anos..'.format(m20))
