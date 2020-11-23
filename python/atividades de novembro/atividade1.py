from time import sleep
print ('{}exercicio 1{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber o valor da nota')
print ()
print ('-='*35)
for b in range(9999999999999999):
    print ()
    print(' digite o valor entre 0 e 10')
    a = int (input(''' Digite o valor da nota
        : '''))
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if a < 0 or a > 10:
        print(' O valor da nota é invalido')
        sleep(2)
    else:
        print(' O valor da nota é {}'.format (a))
        break
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira