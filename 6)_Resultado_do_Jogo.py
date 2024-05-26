time1 = input('Digite o nome do primeiro time: ')
time2 = input('Digite o nome do segundo time: ')
tempo1 = int(input('Digite os gols do primeiro time no primeiro tempo: '))
tempo2 = int(input('Digite os gols do primeiro time no segundo tempo: '))
tempo3 = int(input('Digite os gols do segundo time no primeiro tempo: '))
tempo4 = int(input('Digite os gols do segundo time no segundo tempo: '))

total_time1 = tempo1 + tempo2
total_time2 = tempo3 + tempo4

if total_time1 > total_time2:
    print('O time', time1, 'ganhou de', total_time1, 'a', total_time2)
elif total_time1 == total_time2:
    print('Houve um empate entre os times!')
else:
    print('O time', time2, 'ganhou de', total_time2, 'a', total_time1)