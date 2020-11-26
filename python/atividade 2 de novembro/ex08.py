from time import sleep
print ('-='*35)
print ('{}exercicio 8{}'.format ('-='*15, '-='*15))
print()
print(' Esse programa foi feito para servir como uma urna eletronica')
print()
print('-='*35)
print()
p = int(input(''' Digite a quantidade de pessoas que irão votar
    : '''))
print()
print('[ 1 ] para o primeiro candidato')
print('[ 2 ] para o segundo candidato')
print('[ 3 ] para o terceiro candidato')
print()
sleep(2)
cd1 = 0
cd2 = 0
cd3 = 0
for c in range(1, p+1):
    v = int(input(''' Digite o número de candidato para votar
        : '''))
    if v == 1:
        cd1 += 1
    if v == 2:
        cd2 += 1
    if v == 3:
        cd3 += 1
    print()
sleep(2)
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if cd1 > cd2 and cd1 > cd3:
    print(' Com {} votos o primeiro eleito vençe'.format (cd1))
    print(' O outros eleitores conseguram esses dados, {} para o segundo e {} para o terceiro '.format (cd2, cd3))
elif cd1 < cd2 and cd2 > cd3:
    print(' Com {} votos o segundo eleito vençe'.format (cd2))
    print(' O outros eleitores conseguram esses dados, {} para o primeiro e {} para o terceiro '.format (cd1, cd3))
elif cd3 > cd2 and cd1 < cd3:
    print(' Com {} votos o terceiro eleito vençe'.format (cd3))
    print(' O outros eleitores conseguram esses dados, {} para o primeiro e {} para o segundo '.format (cd1, cd2))
print()
print('-codigo com copyright na nota-'*4) # é zoeira