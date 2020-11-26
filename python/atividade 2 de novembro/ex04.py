from time import sleep
print ('-='*35)
print ('{}exercicio 4{}'.format ('-='*15, '-='*15))
print()
print(' Esse programa foi feito para informações sobre um conjunto de números')
print()
print('-='*35)
print()
q = int (input(''' Digite a quantidade de valores
    : '''))
sleep(2)
t = 0
m=0
mn=0
for a in range(1, q+1):
    print()
    n = float(input(''' Digite o {}º valor
        : '''.format(a)))
    t += n
    if a == 1:
        m = n
        mn = n
    else:
        if n > m:
            m=n
        if n < mn:
            mn=n
    sleep(2)
print()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print(' O maior valor é {:.0f} e o menor valor é {:.0f}'.format (m, mn), end='')
print(' A soma dos valores é ',t)
print('-codigo com copyright na nota-'*4) # é zoeira