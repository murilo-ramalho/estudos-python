from time import sleep
print ('{}exercicio 7{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber o conceito de um aluno!')
print ()
print ('-='*35)
print ()
n1 = float (input(' Digite a primeira nota: '))
n2 = float (input(' Digite a segunda nota: '))
m = (n1+n2)/2
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if m >= 9.0:
    print (''' Com as notas {} e {}, e a media {} 
     O aluno tem o conceito A 
     Aprovado!'''.format (n1, n1, m))    
elif m >= 7.5 and m < 9.0:
    print (''' Com as notas {} e {}, e a media {} 
     O aluno tem o conceito B 
     Aprovado!'''.format (n1, n1, m)) 
elif m >= 6.0 and m < 7.5:
    print (''' Com as notas {} e {}, e a media {} 
     o aluno tem o conceito C
     Aprovado!'''.format (n1, n1, m))
elif m >= 4.0 and m < 6.0:
    print (''' Com as notas {} e {}, e a media {} 
     o aluno tem o conceito D
     Reprovado!'''.format (n1, n1, m))
else:
    print (''' Com as notas {} e {}, e a media {} 
     O aluno tem o conceito E
     Reprovado!'''.format (n1, n1, m))
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)