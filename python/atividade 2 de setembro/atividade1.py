from time import sleep
print ('{}exercicio 1{}'.format ('-='*15, '-='*15))
print (''' Esse programa foi feito para saber 
    qual dos números digitado é maior.''')
print ()
print ('-='*35)
print ()
a = float (input(' Digite um valor: '))
b = float (input(' Digite um outro valor: '))
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a > b :
    print (' O maior valor digitado é {:.0f}'.format (a))
else:
    print (' O maior valor digitado é {:.0f}'.format (b))
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeria
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)