from time import sleep
print ('{}exercicio 5{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se o periodo que você estuda')
print ()
print ('-='*35)
print ()
print (' M-matutino, V-Vespertino, N-Noturno')
a = str (input(' Digite o periodo em que você estuda: '))
print ()
print (' processando...')  
sleep (2)
a = a.upper()
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a == 'M':
    print (' Bom dia!')
elif a == 'V':
    print (' Boa tarde!')
elif a == 'N':
    print (' Boa noite!')
else:
    print (' Digito invalido')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')