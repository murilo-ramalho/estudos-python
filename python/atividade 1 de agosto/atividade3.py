from time import sleep
print ('{}exercicio 3{}'.format ('-='*15, '-='*15))
print (' Esse program foi feito para saber a madia do aluno;')
print ()
print ('-='*35)
print ()
n1 = float (input(' Digite a primeira nota: '))
n2 = float (input(' Digite a segunda nota: '))
n3 = float (input(' Digite a terceira nota: '))
n4 = float (input(' Digite a quarta nota: '))
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
print (''' O aluno com as notas {:.1f}, {:.1f}, {:.1f} e {:.1f} 
 tem como {:.1f} de media;'''\
.format (n1, n2, n3, n4, (n1+n2+n3+n4)/4))
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)