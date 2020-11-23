from random import choice
a1=str (input ('digite o nome do primeiro aluno:'))
a2=str(input('digite o nome do segundo aluno:'))
a3=str(input('digite o nome do terceiro aluno:'))
a4=str(input('digite o nome do quarto aluno:'))
l= [a1, a2, a3, a4]
print ('-_'*10)
print ('o aluno sorteado foi: {}'.format (choice (l)))
print ('-_'*10)
input ()