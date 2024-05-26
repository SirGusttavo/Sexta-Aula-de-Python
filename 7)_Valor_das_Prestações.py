compra = float(input('Digite o valor da compra: '))
prestacao = int(input('Digite o número de prestações: '))
if prestacao > 0:
    valor = compra / prestacao
    print('O valor da prestação é:','%.2f'% valor, 'sem juros')
else:
    print('Número de prestações inválido. Por favor, insira um número maior que zero.')
