from time import sleep
print ('{}exercicio 9{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para resolver equações de 2º grau')
print ()
print ('-='*35)
print ()
a = float (input(' Digite o primeiro valor da conta (a): '))
if a == 0:
    print ()
    print (' Essa conta não é de segundo grau')
else:
    b = float (input(' Digite o segundo valor da conta (b): '))
    c = float (input(' Digite o terceiro valor da conta (c): '))
    delta = b**2-4*a*c
    if delta < 0:
        print (' A equação não possui raízes reais')
    elif delta == 0:
        print (' A equação possui apenas uma raiz real')
    else:
        x1 = (-b+delta**(1/2))/2*a
        x2= (-b-delta**(1/2))/2*a
        print (' Os resultados são {} e {}'.format (x1, x2))
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')