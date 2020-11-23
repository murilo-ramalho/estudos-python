from time import sleep
print ('{}exercicio 5{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se um número é par ou impar!')
print ()
print ('-='*35)
print ()
a= int (input (' Digite um valor: '))
a = a%2
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a == 0:
    print (' o número é par!')
else:
    print (' o número é impar!')
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)