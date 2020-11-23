from time import sleep
print ('{}exercicio 7{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se você vai ou não pagar uma multo pro quilo excedente')
print ()
print ('-='*35)
print ()
a = float (input(' Digite quantos quilos de peixe foi pescado: '))
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a > 50:
    a = a-50
    print (' Você deverá pagar uma multa de R${}'.format (a*4))
else:
    print (' Você não deverá pagar nenhuma multa')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')