from time import sleep
print ('{}exercicio 9{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se quantas latas de tintas devem ser compradas')
print ()
print ('-='*35)
print ()
print (' Digite em metros')
a = float (input(' Digite o área a ser pintada: '))
print ()
print (' processando...')  
sleep (2)
l = a/6
lt = l/18
g = l/3.6
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if a <= 3.6 and a >= 1:
   print (' Será necessario 1 lata de tinta de 18 litros que custa R$80,00')
   print (' Será necessario 1 lata de tinta de 3,6 litros que custa R$25,00')
   print (' Será necessario 1 lata de tinta de 3,6 litros que custa R$25,00 para economizar')
elif a > 3.6 and a <= 108:
   print (' Será necessario 1 lata de tinta de 18 litros')
   print (' Será necessario {:.0f} latas de tinta de 3,6 litros'.format (g))
   if a <= 104.4:
        print (' Será necessario {:.0f} latas de tinta de 3,6 litros que custa R${:.2f} para economizar'.format (g, g*25.00))
   elif a == 108:
        print (' Será necessario 1 lata de tinta de 18 litros que custa R$80,00 para economizar')
elif a > 3.6:
   print (' Será necessario {:.0f} latas de tinta de 18 litros'.format (lt))
   print (' Será necessario {:.0f} latas de tinta de 3,6 litros'.format (g))
   if a == 3.6 and a <= 104.4:
       print (' Será necessario {:.0f} lata de tinta de 3,6 litros que custa {:.2f} para economizar'.format (g, g*25.00))
   elif a > 104.4 and a <= 108:
       print (' Será necessario {:.0f} lata de tinta de 18 litros que custa {:.2f} para economizar'.format (lt, lt*80.00))
   elif a > 108:
        tg = g-lt
        print (' Será necessario {:.0f} latas de tinta de 18 litros e {:.0f} latas de 3,6 litros que custará {:.2f} para economizar'.format (lt-1, tg,(((lt-1)*80.00)+(tg*25.00))))
else:
    print (' Valor insuficiente')
print ()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
print ()
input ('input livre para não finalizar quando for rodar pq estou usando o notepad++')