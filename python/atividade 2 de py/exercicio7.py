v1= int (input ('digite um valor: '))
v2= int (input ('digite um segundo valor: '))
v3= int (input ('digite um terceiro valor: '))
maior= v1
if v1<v2 and v2>v3:
    maior = v2
if v1<v3 and v2<v3:
    maior = v3
print ('o maior valor é {}'.format (maior))
menor=v1
if v1>v2 and v2<v3:
    menor=v2
if v3<v1 and v3<v2:
    menor=v3
print ('o menor valor é {}'.format (menor))
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
