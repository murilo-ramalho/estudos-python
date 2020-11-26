from time import sleep
print ('-='*35)
print ('{}exercicio 6{}'.format ('-='*15, '-='*15))
print()
print(' Esse programa foi feito para saber a media arritimetica')
print()
print('-='*35)
print()
ax = int (input(''' Digite quantas notas são
    : '''))
ax2 = 0
for c in range(0, ax):
    n = float (input(''' Digite o valor da nota
        : '''))
    ax2 += n 
t = ax2/2
print (' a media das notas é ',t)