from time import sleep
print ('-='*35)
print()
print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
print()
print(' Esse programa foi feito para mostra como funciona a série de Fibonacci')
print()
print('-='*35)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
sleep(2)
n1 = 1
n2 = 1
print(n1,' + ',n2,' = ', n2)
while n2 < 500:
    print(n1,' + ',n2,' = ', n1+n2)
    n3 = n2
    n2 += n1
    n1 = n3
print()
print('-codigo com copyright na nota-') # é zoeira