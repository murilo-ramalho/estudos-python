from time import sleep
print ('{}exercicio 7{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para mostra os números interiros entres dois valores selecionados')
print ()
print ('-='*35)
print
n1 = int(input(' Digite um valor: '))
n2 = int(input(' Digite um valor: '))
if n2 > n1:
    ax = n1
    n1 = n2
    n2 = ax
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
for x in range(n2+1, n1):
    print(x)
print()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira