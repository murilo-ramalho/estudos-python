from time import sleep
print ('-='*35)
print ('{}exercicio 10{}'.format ('-='*15, '-='*15))
print()
print(' Esse programa foi feito para saber a quantidade media gasta em coleções')
print()
print('-='*35)
print()
cl = int(input(''' Digite a quantidade de coleções
    : '''))
sleep(1)
t=0
for c in range(1, cl+1):
    i = float(input(''' Digite o valor da {}º  coleção
    : '''.format (c)))
    t+=i
sleep(2)
m=t/cl
print()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print(' A media dos investimentos em coleções é R${:.2f}'.format (m))
print()
print('-codigo com copyright na nota-'*4) # é zoeira
