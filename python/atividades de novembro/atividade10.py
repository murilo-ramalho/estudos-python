from time import sleep
from random import randrange
print ('{}exercicio 10{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para motrar quantos números impares e pares')
print ()
print ('-='*35)
a = float (input(''' Digite um número
    : '''))
b = float (input(''' Digite um número
    : '''))
c = float (input(''' Digite um número
    : '''))
d = float (input(''' Digite um número
    : '''))
e = float (input(''' Digite um número
    : '''))
f = float (input(''' Digite um número
    : '''))
g = float (input(''' Digite um número
    : '''))
h = float (input(''' Digite um número
    : '''))
i = float (input(''' Digite um número
    : '''))
j = float (input(''' Digite um número
    : '''))
ctp = 0
cti = 0
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
while True:
    if a % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    if b % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    if c % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    if d % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    if e % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    if f % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    if g % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    if h % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    if i % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    if j % 2 == 0:
        ctp = ctp + 1
    else:
        cti = cti + 1
    print('Total de números pares é: ', ctp)
    print('Total de números impares é: ', cti)
    break
print()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
