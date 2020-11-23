from time import sleep
print ('-='*35)
print (' aqui é onde estão todos os exercicios')
print (' apenas digite o número do exercicio para testalo')
print ('-='*35)
print ()
a = int (input (' Digite aqui o número do exercicio: '))
print ()
if a == 1: 
    from time import sleep
    print ('{}exercicio 1{}'.format ('-='*15, '-='*15))
    print (''' Esse programa foi feito para saber 
    qual dos números digitado é maior.''')
    print ()
    print ('-='*35)
    print ()
    a = float (input(' Digite um valor: '))
    b = float (input(' Digite um outro valor: '))
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if a > b :
        print (' O maior valor digitado é {:.0f}'.format (a))
    else:
        print (' O maior valor digitado é {:.0f}'.format (b))
    print ()
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
    input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
elif a == 2:
    from time import sleep
    print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber se o valor digitado é negativo ou positivo')
    print ()
    print ('-='*35)
    print ()
    a = int (input(' Digite um valor: '))
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if a > 0:
        print (' O número {} é positivo'.format (a))
    else:
        print (' O número {} é negativo'.format (a))
    print ()
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
    input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
elif a == 3:
    from time import sleep
    print ('{}exercicio 3{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para informar o seu sexo')
    print ()
    print ('-='*35)
    print ()
    a = str (input(' Digite somente a primeira letra do seu sexo: '))
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    a = a.upper()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if a == 'F':
        print (' Sexo feminino')
    elif a == 'M':
        print (' Sexo masculino')
    else:
        print (' Sexo invalido')
    print ()
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
    input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
elif a == 4:
    from time import sleep
    print ('{}exercicio 4{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber se a letra digitada é uma vogal ou consoante')
    print ()
    print ('-='*35)
    print ()
    a = str (input(' Digite um letra: '))
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    a = a.upper()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if a == 'A' or 'E' or 'I' or 'O' or 'U':
        print (' A letra digitada é uma vogal')
    else:
        print (' A letra digitada é uma consoante')
    print ()
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeria
    input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
elif a == 5:
    from time import sleep
    print ('{}exercicio 5{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber se o aluno foi aprovado ou não')
    print ()
    print ('-='*35)
    print ()
    a = int (input(' Digite a primeira nota: '))
    b = int (input(' Digite a segunda nota: '))
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    c = ( a + b ) / 2
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if c == 10:
        print (' Aprovado  com  Distinção')
    elif c >= 7:
        print (' Aprovado')
    else:
        print (' Reprovado')
    print ()
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeria
    input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
else:
    print (' Número digitado invalido')
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeria
    input ()#coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)