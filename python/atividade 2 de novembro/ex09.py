from time import sleep
print ('-='*35)
print ('{}exercicio 9{}'.format ('-='*15, '-='*15))
print()
print(' Esse programa foi feito para saber a media de alunos por sala')
print()
print('-='*35)
print()
s = int(input(''' Digite a quantidade de salas
    : '''))
ax=0
for c in range(1, s+1):
    a = int(input(''' Digite a quantdade de alunos da {}º sala
    : '''.format(c)))
    if a < 40:
        ax += a
    else:
        print(' A quantidades de alunos não é valida')
        print()
        print('Digite novamente')
        a = int(input(''' Digite a quantdade de alunos da {}º sala
    : '''))
t=ax/s
sleep(2)
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print(' A media de alunos por sala é {:.1f}'.format(t))
print()
print('-codigo com copyright na nota-'*4) # é zoeira
