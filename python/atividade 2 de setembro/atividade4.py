from time import sleep
print ('{}exercicio 4{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se a letra digitada é uma vogal ou consoante')
print ()
print ('-='*35)
print ()
a = str (input(' Digite um letra: '))
print ()
print (' processando...')  
sleep (2)
print ()
a = a.upper()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a == 'A' or 'E' or 'I' or 'O' or 'U':
	print (' A letra digitada é uma vogal')
else:
	print (' A letra digitada é uma consoante')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeria
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)