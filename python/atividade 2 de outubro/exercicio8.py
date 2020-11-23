from time import sleep
print ('{}exercicio 8{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se quantas latas de tintas devem ser compradas')
print ()
print ('-='*35)
print ()
print (' Digite em metros')
a = float (input(' Digite o área a ser pintada: '))
print ()
print (' processando...')  
sleep (2)
l = a/3
lt = l/18
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a <= 54 and a > 1:
    print (' Será necessario 1 lata de tinta')
elif a > 54:
    print (' Será necessario {:.0f} latas de tinta'.format (lt))
else:
    print (' Valor insuficiente')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')