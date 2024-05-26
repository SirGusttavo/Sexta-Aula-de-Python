print('====Classificação de nadadores por idade====')
idade = int(input('Digite sua idade: '))
if idade >=5 and idade <=7:
    print('Você está classificado na categoria Infantil A!')
elif idade >=8 and idade <=11:
    print('Você está classificado na categoria Infantil B!')
elif idade >=12 and idade <=13:
    print('Você está classificado na categoria Juvenil A!')
elif idade >=14 and idade <=17:
    print('Você está classificado na categoria Juvenil B!')
else:
    print('Você está classificado na categoria Adulto!') 