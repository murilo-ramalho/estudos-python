from time import sleep
print ('-='*35)
print ('{}exercicio 3{}'.format ('-='*15, '-='*15))
print()
print(' Esse programa foi feito para saber se um número é primo')
print()
print('-='*35)
print()
n = int (input(''' Digite um valor
    : '''))
sleep(2)
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
v = 0
t=(True)
for c in range(1, n+1):
    if n%c==0:
        t=(True)
        v+=1
    else:
        t=(False)
if t == (True) and v==2:
    print(' O número {} é um número primo'.format (n))
else:
    print(' O valor {} não é um número primo'.format (n))
print()
print('-codigo com copyright na nota-'*4) # é zoeira