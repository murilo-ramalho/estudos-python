from time import sleep
print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
print (' Esse programa foi feito para logar sua conta')
print ()
print ('-='*35)
print(' Cadastrar')
print('-'*30)
n = str (input(''' Digite seu nome
    : '''))
nk = str (input(''' Digite seu nick
    : '''))
s = int (input(''' Digite sua senha
    : '''))
print()
sleep(2)
print('-'*30)
print(' login')
for a in range(999999999999):
    print()
    n2 = str (input(''' Digite seu nome
        : '''))
    s2 = int (input(''' Digite sua senha
        : '''))
    print()
    sleep(2)
    if n != n2 and s != s2 or n != n2 and s == s2 or n == n2 and s != s2:
        print('  Erro, nome ou senha invalidos')
        sleep(2)
    else:
        print(' Aproveite!')
        break
print()
print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira