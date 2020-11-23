from time import sleep
print ('{}exercicio 4{}'.format ('-='*15, '-='*15))
print ('Olá, digite o peso de sua pesca e veja o valor da multa (se tiver)')
print ()
pp= float (input('digite o peso de peixeis pescados: '))
print ()
print ('procesando...')
sleep (2)
print ()
print ('{}Resultado;{}'.format ('-='*10, '-='*18)) #quis deixar mais bonito ¯\_(ツ)_/¯
print ()
if pp<=50:
    print ('Hoje não saiu do peso permitido')
else:
    e=pp-50
    print ('    Com {:.3f}kg'.format (pp))
    print ('    Você exedeu {:.3f}kg'.format (e))
    print ('    E agora você deve pagar ua multa de {:.2f} reais'.format (e*4))
print ('-='*33)
sleep (15) #coloquei isso livre para não finalizar quando for rodar (estou usando o notepad++)