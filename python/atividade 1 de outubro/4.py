from time import sleep
print ('{}exercicio 4{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para saber se um aluno passou ou não em uma materia!')
print ()
print ('-='*35)
print ()
n1 = float (input (' Digite a primeira nota: '))
n2 = float (input (' Digite a segunda nota: '))
n3 = float (input (' Digite a terceira nota: '))
m = (n1+n2+n3)/3
print ()
print (' processando...')
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
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)