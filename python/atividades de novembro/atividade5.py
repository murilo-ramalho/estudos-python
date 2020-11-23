from time import sleep
print ('{}exercicio 5{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para mostra a media do números digitado')
print ()
print ('-='*35)
a = float (input(''' Digite um número
    : '''))
b = float (input(''' Digite um número
    : '''))
c = float (input(''' Digite um número
    : '''))
d = float (input(''' Digite um número
    : '''))
e = float (input(''' Digite um número
    : '''))
print ()
print (' processando...')  
sleep (2)
print ()
f = (a+b+c+d+e)//5
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print(' O valor da media é {:.1f}'.format (f))
print()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
