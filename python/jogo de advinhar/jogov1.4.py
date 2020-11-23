from random import randrange
from time import sleep
a = randrange(5)
print ('~~'*55)
print ('{}o jogo é acertar o número que o computador escolher!, tente acertar!'.format (' '*10))
print ()
print ('{}Você terá 5 chançes'.format (' '*10))
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
# primeira chance do jogador
print ()
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print ('1 para sim e 2 para não')
o = int (input('tentar novamente?: '))
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# segunda chance do jogador
    print ()
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print ('1 para sim e 2 para não')
    o = int (input('tentar novamente?: ')) 
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# terceira chance do jogador
        print ()
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        print ('1 para sim e 2 para não')
        o = int (input('tentar novamente?: '))
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# quarta chance do jogador
            print ()
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
            print ('1 para sim e 2 para não')
            o = int (input('tentar novamente?: '))
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            print ()
            if o == 1:
                a = randrange(5)
# quinta chance do jogador
                b = int ( input (' digite um valor entre 0 e 5: ')) 
                if b>5:
                    print ()
                    print (' Número escolido é ivalido no jogo!!!')
                    print ()
                elif b<=5:
                    print ()
                    print ('{}carregando...'.format (' '*5))
                    sleep(2)
                    print ()
                    print ('{}Resultado{}'.format ('-='*10, '-='*18))
                    print ()
                    print (' Parabens voçê acertou!!' if b==a  else ' tente novamente voçê errou!!')
                    print ()
                    print ('-='*33)
# quinta e ultima chance do jogador
                print ()
# fim--------------------------------------------------------------------------------------------
                print ('suas chançes acabaram;')
                o = int (input('digite 2 para sair'))
                print ()
                if o == 2: 
                    print (''' Obrigado por jogar
                    tenha uma boa tarde!!''') 
# fim--------------------------------------------------------------------------------------------
# fim--------------------------------------------------------------------------------------------
elif o == 2:
    print (''' Obrigado por jogar
    tenha uma boa tarde!!''') 
# fim--------------------------------------------------------------------------------------------
elif o != 2 or o != 1:
    print ('escolha invalida!!')
    print ()
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print ('1 para sim e 2 para não')
    o = int (input('tentar novamente?: '))
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        print ('1 para sim e 2 para não')
        o = int (input('tentar novamente?: '))
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            print ('1 para sim e 2 para não')
            o = int (input('tentar novamente?: '))
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
                print ()
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                print ('1 para sim e 2 para não')
                o = int (input('tentar novamente?: '))
# saida/nova tentativa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                print ()
                if o == 1:
                    a = randrange(5)
# quinta e ultima chance do jogador caso ocorra algum erro 
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
# fim--------------------------------------------------------------------------------------------
                    print ('suas chançes acabaram;')
                    o = int (input('digite 2 para sair'))
                    print ()
                    if o == 2: 
                        print (''' Obrigado por jogar
                        tenha uma boa tarde!!''') 
# fim--------------------------------------------------------------------------------------------
sleep (3) 
#coloquei isso livre para não finalizar quando for rodar (estou usando o notepad++)