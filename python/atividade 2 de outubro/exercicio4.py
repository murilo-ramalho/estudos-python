from time import sleep
print ('{}exercicio 4{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para ordenar os números em ordem decrescente')
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
if a > b > c:
    print (' Valores em ordem decrescente {}, {}, {}'.format (int(a), int(b), int(c)))
elif a > c > b:
    print (' Valores em ordem decrescente {}, {}, {}'.format (int(a), int(c), int(b)))
elif a > b and a == c:
    print (' Valores em ordem decrescente {}, {}'.format (int(a), int(b)))
elif a > c and a == b:
    print (' Valores em ordem decrescente {}, {}'.format (int(a), int(c)))
elif b > a > c:
    print (' Valores em ordem decrescente {}, {}, {}'.format (int(b), int(a), int(c)))
elif b > c > a:
    print (' Valores em ordem decrescente {}, {}, {}'.format (int(b), int(c), int(a)))
elif b > a and b == c:
    print (' Valores em ordem decrescente {}, {}'.format (int(b), int(a)))
elif b > c and b == a:
    print (' Valores em ordem decrescente {}, {}'.format (int(b), int(c)))
elif c > a > b:
    print (' Valores em ordem decrescente {}, {}, {}'.format (int(c), int(a), int(b)))
elif c > b > a:
    print (' Valores em ordem decrescente {}, {}, {}'.format (int(c), int(b), int(a)))
elif c > a and c == b:
    print (' Valores em ordem decrescente {}, {}'.format (int(c), int(b)))
elif c > b and c == a:
    print (' Valores em ordem decrescente {}, {}'.format (int(c), int(b)))
else:
    print ('os valores são iguais')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')