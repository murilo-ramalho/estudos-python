from time import sleep
print ('{}exercicio 5{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para em contrar um possivel assasino.')
print ('-='*35)
print ()
p1 = str (input('Telefonou para a vítima?: '))
p2 = str (input('Esteve no local do crime?: '))
p3 = str (input('Devia para a vítima?: '))
p4 = str (input('Telefonou para a vítima?: '))
p5 = str (input('Já trabalhou com a vítima?: '))
p1 = p1.upper()
p2 = p2.upper()
p3 = p3.upper()
p4 = p4.upper()
p5 = p5.upper()
print ()
if p1 == 'SIM' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'NÃO' \
or p1 == 'SIM' and p2 == 'SIM' and p3 == 'NÃO' and p4 == 'SIM' and p5 == 'NÃO' \
or p1 == 'SIM' and p2 == 'SIM' and p3 == 'NÃO' and p4 == 'NÃO' and p5 == 'SIM' \
or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'NÃO' \
or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'SIM' \
or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'NÃO' and p4 == 'SIM' and p5 == 'SIM' \
or p1 == 'NÃO' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'NÃO' \
or p1 == 'NÃO' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'SIM' \
or p1 == 'NÃO' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'SIM' :
    print ('a')
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)