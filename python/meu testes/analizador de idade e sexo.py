#variaveis q fazem o scrt funcionar
m = 0
nhv = ""
imv = 0
imn = 0
imm = 0
print ('{}esse programa foi feito para saber alguns dados sobre idade e sexo{}'.format('='*3, '='*3))
#verifica a quantidade de pessoas
qp = int(input('digite a quantidade de pessoas: '))
for p in range(1, qp+1):
  print("{}º pessoa".format (p))
  n = str(input('nome: '))
  i = int(input('idade: '))
  s = str(input('sexo [F/M]: ')).upper()
  m += i
  #verifica e recolhe o nome e a idade do homem mais velho
  if p==1:
    if s == 'M':
      imv = i
      nhv = n
  else:
    if i>imv and s=='M':
      imv = i
      nhv = n
  #verifica e recolhe quanta mulheres tem 
  if s=='F':
    if i<20:
      imn += 1
    else:
      imm += 1
m /= qp
#mostra os resultados
print('A media da idade das pessoas é de {:.1f} anos'.format(m))
if imv>0:
  print('O homem mais velho se chama {} e tem {} anos'.format(nhv, imv))
if imn>0:
  if imn>1:
    print('no grupo tem {} mulheres menor de 20 anos'.format(imn))
  else:
    print('no grupo tem {} mulher menor de 20 anos'.format(imn))
if imm>0:
  if imm>1:
    print('no grupo tem {} mulheres maior de 20 anos'.format(imm))
  else:
    print('no grupo tem {} mulher maior de 20 anos'.format(imm))
print('fim')