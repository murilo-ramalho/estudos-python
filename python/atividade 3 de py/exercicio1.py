from time import sleep
print ('exercicio 1')
n1= int( input ('digite um valor: '))
n2= int ( input ('digite um segundo valor: '))
n3= float ( input ('digite um terceiro valor: '))
produto=(n1*2)*(n2/2)
soma=n1*3+n3
cubo=n3**3
print ('processando...') #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}resultado;{}'.format ('-='*10, '-='*18))
print ()
print ('o produto do dobro do primeiro valor com metade do segundo valor é: {}'.format (produto))
print ('a soma do triplo do primeiro valor com o terceiro valor é: {}'.format (float (soma)))
print ('o terceiro valor elevado ao cubo é: {}'.format (float (cubo))) 
print ('-='*33)
sleep (15) #coloquei isso livre para não finalizar quando for rodar (estou usando o notepad++)
 
