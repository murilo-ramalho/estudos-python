from time import sleep
print ('{}exercicio 1{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber os dias da semana')
print ()
print ('-='*35)
print ()
print (' Digite um número de 1 a 7')
a = int (input(' Digite um número: '))
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a == 1:
    print (' O número {} é Segunda-feira'.format (a))
elif a == 2:
    print (' O número {} é Terça-feira'.format (a))
elif a == 3:
    print (' O número {} é Quarta-feira'.format (a))
elif a == 4:
    print (' O número {} é Quinta-feira'.format (a))
elif a== 5:
    print (' O número {} é Sexta-feira'.format (a))
elif a == 6:
    print (' O número {} é Sabado'.format (a))
elif a == 7:
    print (' O número {} é Domingo'.format (a))
else:
    print (' O número {} é invalido'.format (a))
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)