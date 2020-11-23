from random import randrange
from time import sleep
print ('~~'*55)
print ('{}o jogo é acertar o número que o computador escolher!, tente acertar!'.format (' '*10))
print ()
print ('{}Você terá 5 chançes'.format (' '*10))
print ('~~'*55)
print ()
b = randrange(5)
a = int ( input (''' digite um valor entre 0 e 5;
    : ''')) 
if a > 5 or a < 0: 
    print ()
    print (' Número escolido é ivalido no jogo!!!')
    print ()
else:
    print ()
    print ('{}carregando...'.format (' '*5))
    sleep(2)
    print ()
    print ('{}Resultado{}'.format ('-='*10, '-='*18))
    print ()
    if a == b:
        print (' Parabéns voçê acertou!!')
    else:
        print (' tente novamente voçê errou!!')
print ()
print ('-='*33)
print ()
sleep(2)
print (' 1 para sim e 2 para não')
x = int (input(' tentar novamente?: '))
while x == 1:
    b = randrange(5)
    a = int ( input (''' digite um valor entre 0 e 5;
        : ''')) 
    if a > 5 or a < 0: 
        print ()
        print (' Número escolido é ivalido no jogo!!!')
        print ()
    else:
        print ()
        print ('{}carregando...'.format (' '*5))
        sleep(2)
        print ()
        print ('{}Resultado{}'.format ('-='*10, '-='*18))
        print ()
        if a == b:
            print (' Parabéns voçê acertou!!')
        else:
            print (' tente novamente voçê errou!!')
    print ()
    print ('-='*33)
    print ()
    sleep
    print (' 1 para sim e 2 para não')
    x = int (input(' tentar novamente?: '))
else:
    print(' Obrigado por jogar!')