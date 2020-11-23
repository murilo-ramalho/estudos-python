from time import sleep
print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se o valor digitado é negativo ou positivo')
print ()
print ('-='*35)
print ()
a = int (input(' Digite um valor: '))
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a > 0:
    print (' O número {} é positivo'.format (a))
else:
    print (' O número {} é negativo'.format (a))
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeria
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)