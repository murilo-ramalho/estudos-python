from time import sleep
print ('{}exercicio 6{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se um valor é inteiro ou decimal!')
print ()
print ('-='*35)
print ()
a = float (input(' Digite um valor; '))
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()

if a // 1 == a: 
    print(' O número {} inteiro!'.format (a)) # fiz diferente do que vocês pediram '-'
else:
    print(' O número {} é decimal!'.format (a))
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)