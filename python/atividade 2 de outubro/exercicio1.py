from time import sleep
print ('{}exercicio 1{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber qual é o maior número digitado')
print ()
print ('-='*35)
print ()
a = float (input(' Digite o primeiro valor: '))
b = float (input(' Digite o segundo valor: '))
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a > b:
    print (' O valor {} é o maior'.format (int(a)))
elif a == b:
    print (' Os valores são iguais')
else:
 print (' O valor {} é o maior'.format (int(b)))
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')