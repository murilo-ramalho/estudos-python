from time import sleep
print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber o peso ideal')
print ()
print ('-='*35)
print ()
print (' digite em metros')
print ()
a = float (input(' Digite sua altura: '))
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print (' A com {}cm de altura seu peso ideal é {:.1f}kg'.format (a, (72.7*a)-58))
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)