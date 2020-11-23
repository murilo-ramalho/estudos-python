from time import sleep
print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se um ano é bissexto ou não')
print ()
print ('-='*35)
print ()
a = int (input (' digite um ano; '))
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if ano % 4 == 0 and % 100 != 0 or a % 400 == 0:
    print (' o ano {} é bissexto!'.format (a))
else:
    print (' o ano {} não é bissexto!'.format (a))
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)