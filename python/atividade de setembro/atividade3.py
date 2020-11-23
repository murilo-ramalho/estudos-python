from time import sleep
print ('{}exercicio 3{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber o sálario e os descontosdo sárario')
print ()
print ('-='*35)
print ()
sph = float (input(' Digite o sárario por hora: '))
ht = int (input(' Digite o as horas trabalhadas no mês: '))
print ()
sb = sph * ht
ir = (sb * 11) /100
inss = (sb * 8) /100
sind = (sb * 5) /100
sl = sb-(ir+inss+sind)
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print (' Salário Bruto R${}'.format (sb))
print (' IR R${}'.format (ir))
print (' INSS R${}'.format (inss))
print (' Sindicato R${}'.format (sind))
print (' Salário Liquido R${}'.format (sl))
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
