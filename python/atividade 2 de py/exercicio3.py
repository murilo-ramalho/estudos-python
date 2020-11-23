a= str ( input ('digite seu sexo (use a as letras f/m): '))
a=a.capitalize() #para filtra melhor
if a != 'M' or a != 'F':
    print ('sexo invalido!!')
elif a=='M':
    print ('sexo masculino!!')
else:
    print ('sexo feminino!!')
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)