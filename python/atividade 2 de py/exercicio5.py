n1= int (input('digite o vlor da primeira nota: '))
n2= int (input('digite o valor da segundo nota: '))
m=(n1+n2)/2
if m==10:
    print ('Com a media {}, o aluno foi aprovado com distição!!'.format (m))
else: 
    if m>5:
        print ('Com a media {}, o aluno foi aprovado'.format (m))
    if m<5:
        print ('Com a media {}, o aluno foi reprovado'.format (m))
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)