from time import sleep
print ('{}exercicio 5{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se o aluno foi aprovado ou não')
print ()
print ('-='*35)
print ()
a = int (input(' Digite a primeira nota: '))
b = int (input(' Digite a segunda nota: '))
print ()
print (' processando...')  
sleep (2)
print ()
c = ( a + b ) / 2
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if c == 10:
	print (' Aprovado  com  Distinção')
elif c >= 7:
	print (' Aprovado')
else:
	print (' Reprovado')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeria
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)