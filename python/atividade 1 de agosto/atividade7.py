from time import sleep
print ('{}exercicio 7{}'.format ('-='*15, '-='*15))
print (' Esse program foi feito para saber o salario;')
print ()
print ('-='*35)
print ()
s = float (input(' Digite o valor recebido por hora: '))
h = float (input(' Digite a quantidade de horas trabalhadas no mês: '))
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print (' O salario será de {:.2f}R$;'.format (s*h))
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)