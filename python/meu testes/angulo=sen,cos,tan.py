import math
a= float ( input ('digite um ângulo:'))
cos= math.cos (math.radians (a))
sen= math.sin (math.radians (a))
tan= math.tan (math.radians (a))
print ('-'*10)
print ('O sen de {0} graus é {1:.2f}:\n O cosseno de {2} graus é {3:.2f}:\n O tangente de {4} graus é {5:.2f}:'.format (int (a), sen, int(a), cos, int(a), tan))
print ('-'*10)
input ()
