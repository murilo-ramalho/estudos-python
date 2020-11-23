from time import sleep
print ('{}exercicio 6{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber o peso ideal')
print ()
print ('-='*35)
print ()
a = str (input(' Digite seu sexo: '))
print (' digite em metros')
b = float (input(' Digite sua altura: '))
print ()
print (' processando...')  
sleep (2)
a = a.upper()
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a == 'M':
    print (' Seu peso ideal é {:.1f}'.format ((72.7*b) - 58))
elif a == 'F':
    print (' Seu peso ideal é {:.1f}'.format ((62.1*b) - 44.7))
else:
    print ('digito invalido')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')
