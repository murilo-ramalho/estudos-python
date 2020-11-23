from time import sleep
print ('{}exercicio 3{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para informar o seu sexo')
print ()
print ('-='*35)
print ()
a = str (input(' Digite somente a primeira letra do seu sexo: '))
print ()
print (' processando...')  
sleep (2)
print ()
a = a.upper()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a == 'F':
    print (' Sexo feminino')
elif a == 'M':
    print (' Sexo masculino')
else:
    print (' Sexo invalido')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeria
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)