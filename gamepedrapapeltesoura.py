print('==========LOJAS OTTO=========')
preco = float(input('Insira o preço do produto: R$'))
print('-=-'* 11)
print('[1] Á vista no dinheiro ou cheque')
print('[2] Á vista no cartão')
print('[3] Em até 2 vezes no cartão')
print('[4] Em 3 vezes ou mais no cartão')
print('-=-'* 11)
desc1 = preco - preco * (10 / 100)
desc2 = preco - preco * (5 / 100)
pgta = int(input('Escolha a forma de pagamento: '))
if pgta == 1:
    print('Você tem 10% de desconto! O preço era R${:.2f} e ficou R${:.2f}.'.format(preco, desc1))
if pgta == 2:
    print('Você tem 5% de desconto! O preço era R${:.2f} e ficou R${:.2f}.'.format(preco, desc2))
if pgta == 3:
    print('O preço fica inalterado! Sem juros! O preço fica R${:.2f}.'.format(preco))
if pgta == 4:
    print('Nesta opção você pagará 20% de juros. O preço fica R${:.2f}.'.format(preco*1.20))