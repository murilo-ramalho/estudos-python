p1= float ( input('digite o valor do primeiro item: '))
p2= float ( input('digite o valor do segundo item: '))
p3= float ( input ('digite o valor do terceiro item: '))
menor_preço=p1
if p1>p2 and p2<p3:
    menor_preço=p2
if p3<p1 and p3<p2:
    menor_preço=p3
print ('o item a se comprar, é item o com valor {}'.format (menor_preço))
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
