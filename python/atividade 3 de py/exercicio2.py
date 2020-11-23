from time import sleep
print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
print ('digite sua altura para saber seu peso ideal')
print ()
a= float (input('digite sua altura: '))
print ('processando...') #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}resultado;{}'.format ('-='*10, '-='*18))
print ()
print ('seu peso ideal é {:.1f}Kg'.format ((72.7*a) -58))
print ('-='*33)
sleep (15) #coloquei isso livre para não finalizar quando for rodar (estou usando o notepad++)