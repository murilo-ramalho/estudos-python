from random import randrange
from time import sleep
a = randrange(5)
print ('~~'*55)
print ('{}o jogo é acertar o número que o computador escolher!, tente acertar!'.format (' '*10))
print ('~~'*55)
print ()
# primeira chance do jogador
b = int ( input (' digite um valor entre 0 e 5: ')) 
if b>5: 
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
    print (' Parabens voçê acertou!!' if b==a  else ' tente novamente voçê errou!!')
    print ()
    print ('-='*33)
print ()
print ('1 para sim e 2 para não')
o = int (input('tentar novamente?: '))
print ()
if o == 1:
    a = randrange(5)
    # segunda chance do jogador
    b = int ( input (' digite um valor entre 0 e 5: ')) 
    if b>5:
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
        print (' Parabens voçê acertou!!' if b==a  else ' tente novamente voçê errou!!')
        print ()
        print ('-='*33)
    print ()
    print ('1 para sim e 2 para não')
    o = int (input('tentar novamente?: ')) 
    print ()
    if o == 1:
        a = randrange(5)
        # terceira chance do jogador
        b = int ( input (' digite um valor entre 0 e 5: ')) 
        if b>5:
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
            print (' Parabens voçê acertou!!' if b==a  else ' tente novamente voçê errou!!')
            print ()
            print ('-='*33)
        print ()
        print ('1 para sim e 2 para não')
        o = int (input('tentar novamente?: '))
        print ()
        if o == 1:
            a = randrange(5)
            # quarta chance do jogador
            b = int ( input (' digite um valor entre 0 e 5: ')) 
            if b>5:
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
                print (' Parabens voçê acertou!!' if b==a  else ' tente novamente voçê errou!!')
                print ()
                print ('-='*33)
                print ()
            print ('1 para sim e 2 para não')
            o = int (input('tentar novamente?: '))
            print ()
            if o == 1:
                a = randrange(5)
                # quinta chance do jogador
                b = int ( input (' digite um valor entre 0 e 5: ')) 
                if b>5:
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
                    print (' Parabens voçê acertou!!' if b==a  else ' tente novamente voçê errou!!')
                    print ()
                    print ('-='*33)
                    print ()
                    input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
elif o == 2: 
    print (''' Obrigado por jogar
    tenha uma boa tarde!!''')
else:
    print ('escolha invalida!!')
    print ()
    print ('1 para sim e 2 para não')
    o = int (input('tentar novamente?: '))
    print ()
    if o == 1:
        a = randrange(5)
        # segunda chance do jogador caso ocorra algum erro 
        b = int ( input (' digite um valor entre 0 e 5: ')) 
        if b>5:
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
            print (' Parabens voçê acertou!!' if b==a  else ' tente novamente voçê errou!!')
            print ()
            print ('-='*33)
        print ()
        print ('1 para sim e 2 para não')
        o = int (input('tentar novamente?: '))
        print ()
        if o == 1:
            a = randrange(5)
            # terceira chance do jogador caso ocorra algum erro 
            b = int ( input (' digite um valor entre 0 e 5: ')) 
            if b>5:
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
                print (' Parabens voçê acertou!!' if b==a  else ' tente novamente voçê errou!!')
                print ()
                print ('-='*33)
            print ()
            print ('1 para sim e 2 para não')
            o = int (input('tentar novamente?: '))
            print ()
            if o == 1:
                a = randrange(5)
                # quarta chance do jogador caso ocorra algum erro 
                b = int ( input (' digite um valor entre 0 e 5: ')) 
                if b>5:
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
                    print (' Parabens voçê acertou!!' if b==a  else ' tente novamente voçê errou!!')
                    print ()
                    print ('-='*33)
sleep (3) #coloquei isso livre para não finalizar quando for rodar (estou usando o notepad++)