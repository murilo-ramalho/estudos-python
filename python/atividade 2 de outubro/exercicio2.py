from time import sleep
print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber o maior e o menor número digitado')
print ()
print ('-='*35)
print ()
a = float (input(' Digite o primeiro valor: '))
b = float (input(' Digite o segundo valor: '))
c = float (input(' Digite o terceiro valor: '))
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a > b > c and a > c > b:
    print (' O maior valor é {}, e o menor valor é {}'.format (int(a), int(c)))
elif a > b and a == c:
    print (' O maior valor é {}, e o menor valor é {}'.format (int(a), int(b)))
elif a > c and a == b:
    print (' O maior valor é {}, e o menor valor é {}'.format (int(a), int(c)))
elif b > a > c and b > c > a:
    print (' O maior valor é {}, e o menor valor é {}'.format (int(b), int(c)))
elif b > a and b == c:
    print (' O maior valor é {}, e o menor valor é {}'.format (int(b), int(a)))
elif b < c and b == a:
    print (' O maior valor é {}, e o menor valor é {}'.format (int(b), int(c)))
elif c > a > b and c > b > a:
    print (' O maior valor é {}, e o menor valor é {}'.format (int(c), int(a)))
elif c > a and c == b:
    print (' O maior valor é {}, e o menor valor é {}'.format (int(c), int(a)))
elif c < b and c == a:
    print (' O maior valor é {}, e o menor valor é {}'.format (int(c), int(b)))
else:
    print (' Os valores são iguais')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')