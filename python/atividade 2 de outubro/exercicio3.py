from time import sleep
print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para informar qual produto você deve comprar')
print ()
print ('-='*35)
print ()
a = float (input(' Digite o preço do primeiro item: R$ '))
b = float (input(' Digite o preço do segundo item: R$ '))
c = float (input(' Digite o preço do terceiro item: R$ '))
print ()
print (' processando...')  
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a < b and a < c:
    print (' O item a ser compra é o primeiro item digitado, que custa R${:.2f}'.format (a))
elif a < b and a == c:
    print (' O item a ser compra é o terceiro item digitado, que custa R${:.2f}'.format (a))
elif a < c and a == b:
    print (' O item a ser compra é o terceiro item digitado, que custa R${:.2f}'.format (a))
elif b < a and b < c:
    print (' O item a ser compra é o segundo item digitado, que custa R${:.2f}'.format (b))
elif b < a and b == c:
    print (' O item a ser compra é o terceiro item digitado, que custa R${:.2f}'.format (b))
elif b < c and b == a:
    print (' O item a ser compra é o terceiro item digitado, que custa R${:.2f}'.format (b))
elif c < a and c < b:
    print (' O item a ser compra é o terceiro item digitado, que custa R${:.2f}'.format (c))
elif c < a and c == b:
    print (' O item a ser compra é o terceiro item digitado, que custa R${:.2f}'.format (c))
elif c < b and c == a:
    print (' O item a ser compra é o terceiro item digitado, que custa R${:.2f}'.format (c))
else:
    print (' Os valores são iguais')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')