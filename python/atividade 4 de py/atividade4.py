from time import sleep
print ('{}exercicio 4{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se um aluno passou ou não em uma materia!')
print ()
print ('-='*35)
print ()
n1 = float (input (' digite a primeira nota; '))
n2 = float (input (' digite a segunda nota; '))
n3 = float (input (' digite a terceira nota; '))
m = (n1+n2+n3)/3
print ()
print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
sleep (2)
print ()
print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
print ()
if m == 10:
    print (' Parabens!!, aluno aprovado com distinção!')
elif m >= 7:
    print (' Aluno Aprovado!')
else:
    print (' Aluno Reprovado!')
print ('-='*33)
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)