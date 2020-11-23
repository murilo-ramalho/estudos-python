from time import sleep
print ('{}exercicio 1{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para qual é o dia da semana!')
print ()
print (' digite um número de 1 a 7 para saber o dia da semana; ')
print ('-='*35)
print ()
d = int (input (' digite um número; ')) 
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if d == 1:
    print (' O número 1 representa Domingo!') 
elif d == 2:
    print (' O número 2 representa Segunda-feira!')
elif d == 3:
    print (' O número 3 representa Terça-feira!')
elif d == 4:
    print (' O número 4 representa Quarta-feira!')
elif d == 5:
    print (' O número 5 representa Quinta-feira!')
elif d == 6:
    print (' O número 6 representa Sexta-feira!')
elif d == 7:
    print (' O número 7 representa Sabado!')
else:
    print ('Valor digitado é invalido!!')
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)