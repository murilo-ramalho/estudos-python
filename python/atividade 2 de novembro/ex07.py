from time import sleep
print ('-='*35)
print ('{}exercicio 7{}'.format ('-='*15, '-='*15))
print()
print(' Esse programa foi feito para saber a media aritimetica')
print()
print('-='*35)
print()
p = int (input(''' Digite a quantidade de pessoas
    : '''))
sleep(2)
ax = 0
for c in range(1, p+1):
    i = int (input(''' Digite sua idade
        : '''))
    print()
    ax += i
m = ax/p
sleep(2)
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print (' A media das idades é {:.0f}'.format(m), end=' ')
if m > 0 and m < 25:
    print('que faz parte da 1º idade')
elif m > 25 and m < 60:
    print('que faz parte da 2º idade')
else:
    print('que faz parte da 3º idade')
    print('-codigo com copyright na nota-'*4) # é zoeira