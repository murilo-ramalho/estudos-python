import math
co= float (input ('Digite o valor do cateto oposto:'))
ca= float (input ('Digite o valor do cateto adjacente:'))
h= math.hypot (co, ca)
print ('A hipotenusa {:.2f} do cateto oposto {} e do adjacente {} '.format (h, co, ca))
input ()