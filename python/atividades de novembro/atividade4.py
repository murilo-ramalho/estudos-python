from time import sleep
print ('{}exercicio 4{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para mostra qual número é o maior')
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
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a>b and a>c and a>d and a>e:
    print(' O maior número é {}'.format (a))
elif b>a and b>c and b>d and b>e:
    print(' O maior número é {}'.format (b))
elif c>a and c>b and c>d and c>e:
    print(' O maior número é {}'.format (c))
elif d>a and d>b and d>c and d>e:
    print(' O maior número é {}'.format (d))
elif e>a and e>b and e>c and e>d:
    print(' O maior número é {}'.format (e))
print()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira