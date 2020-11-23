from time import sleep
from math import pi
print ('{}exercicio 5{}'.format ('-='*15, '-='*15))
print (' Esse program foi feito para saber a área de um circulo;')
print ()
print ('-='*35)
print ()
r = float (input(' Digite raio do circulo: '))
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print (' O com o raio {} tem como {:.1f} de área;'.format (r, r**2*pi))
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)