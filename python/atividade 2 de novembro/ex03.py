from time import sleep
print ('-='*35)
print ('{}exercicio 3{}'.format ('-='*15, '-='*15))
print()
print(' Esse programa foi feito para mostra o fatorial de um número')
print()
print('-='*35)
print()
n = int (input(''' Digite um valor
    : '''))
sleep(2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print (n,'! ', end='')
ax = 1
for a in range(n, 0, -1):
    print('*{}'.format(a), end='')
    ax *= a
print('= ', ax)
print('-codigo com copyright na nota-'*4) # é zoeira