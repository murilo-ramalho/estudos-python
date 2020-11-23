from time import sleep
print ('{}exercicio 9{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para mostra a tabuada do número digitado')
print ()
print ('-='*35)
a = int (input(''' Digite o número desejado
    : '''))
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
for b in range(0, 11):
    print(a,' x ',b,' = ', a*b)
print()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
