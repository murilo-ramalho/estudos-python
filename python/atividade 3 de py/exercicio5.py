from time import sleep
print ('{}exercicio 5{}'.format ('-='*15, '-='*15))
print ('Olá, este é um programa para calcular seu salario')
print ()
sht= float (input('digite o seu salario por hora trabalhada: R$'))
qht= int (input('digite a quantidade de horas trabalhadas no mês: '))
sb=sht*qht
ip=(sb*11)/100
inss=(sb*8)/100
sd=(sb*5)/100
sl=sb-(ip+inss+sd)
print ()
print('processando...')
sleep (2)
print ()
print ('{}Resultado;{}'.format ('-='*10, '-='*18)) #quis deixar mais bonito ¯\_(ツ)_/¯
print ()
print ('seu salario é : R${:.2f} devido a os descontos'.format (sl))
print ()
sleep (4)
print ('{}MAS'.format (' '*3))
print ()
sleep (3)
print ('O seu salario bruto é : R${:.2f}'.format (sb))
print ('O desconto de 11% feito para o imposto de renda é: R${:.2f}'.format (ip))
print ('O desconto de 8% feito para o INSS é: R${:.2f}'.format (inss))
print ('O desconto de 5% feito para o sindicato é: R${:.2f}'.format (sd))
print ('O preço total dos descontos é: R${:.2f}'.format (ip+inss+sd))
print ('O seu salario liquido (que irar receber) é: R${:.2f}'.format (sl))
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)