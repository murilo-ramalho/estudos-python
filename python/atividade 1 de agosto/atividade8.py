from time import sleep
print ('{}exercicio 8{}'.format ('-='*15, '-='*15))
print (''' Esse program foi feito para saber a em graus Farenheit
    em garus Celsius;''')
print ()
print ('-='*35)
print ()
f = int (input(' Digite a temperatura em graus Farenheit: '))
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print (' {}fº são {:.0f}gº;'.format (f, 5 * (f-32) / 9))
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)