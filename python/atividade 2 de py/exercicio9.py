a= int ( input('digite o valor do primeiro item: '))
b= int ( input('digite o valor do segundo item: '))
c= int ( input ('digite o valor do terceiro item: '))
p=a
if a>b and c>b:
    p=b
if c<a and c<b:
    p=c
s=a
if a>b and c<b or a<b and b>c:
    s=b
if c<a and c>b or c>a and b>c:
    s=c
t=a
if a<b and b>c:
    t=b
if c>a and c>b:
    t=c
print ('o menor valor foi {}, o valor intermadiario foi {}, e o maior foi {}.'.format (p, s, t))
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
