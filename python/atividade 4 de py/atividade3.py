from time import sleep
print ('{}exercicio 3{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se a data digitada está correta!')
print ()
print ('-='*35)
print ()
d = int ( input(' Digite o dia; '))
m = int ( input(' Digite o mes; '))
a = int (input (' Digite o ano; '))
v = False
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    if d<=31:
        v = True
elif m==4 or m==6 or m==9 or m==11:
    if d<=30:
        v = True
elif m==2:
    if a%4==0 and a%400!=0 or a%400==0:
        if d<=29:
            v = True
    elif d<=28:
        v = True

if v == True:
    print(' Data válida')
else:
    print(' Data inválida')
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
