from time import sleep
print ('-='*35)
print (' Aqui é onde estão todos os exercicios')
print (' Apenas digite o número do exercicio para avalialo')
print ('-='*35)
print ()
b = int (input (' Digite aqui o número do exercicio: '))
print ()
if b == 1: 
    print ('{}exercicio 1{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber os dias da semana')
    print ()
    print ('-='*35)
    print ()
    print (' Digite um número de 1 a 7')
    a = int (input(' Digite um número: '))
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if a == 1:
        print (' O número {} é Segunda-feira'.format (a))
    elif a == 2:
        print (' O número {} é Terça-feira'.format (a))
    elif a == 3:
        print (' O número {} é Quarta-feira'.format (a))
    elif a == 4:
        print (' O número {} é Quinta-feira'.format (a))
    elif a== 5:
        print (' O número {} é Sexta-feira'.format (a))
    elif a == 6:
        print (' O número {} é Sabado'.format (a))
    elif a == 7:
        print (' O número {} é Domingo'.format (a))
    else:
        print (' O número {} é invalido'.format (a))
    print ()
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
elif b == 2:
    print ('{}exercicio 2{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber se um ano é bissexto ou não')
    print ()
    print ('-='*35)
    print ()
    a = int (input  (' digite um ano: '))
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print (' o ano {} é bissexto!'.format (a))
    else:
        print (' o ano {} não é bissexto!'.format (a))
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira 
elif b == 3:
    print ('{}exercicio 3{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber se a data digitada está correta!')
    print ()
    print ('-='*35)
    print ()
    d = int ( input(' Digite o dia: '))
    m = int ( input(' Digite o mes: '))
    a = int (input (' Digite o ano: '))
    v = False
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if d<=31:
            v = True
    elif m==4 or m==6 or m==9 or m==11:
        if d<=30:
            v = True
    elif m==2:
        if a%4==0 and a%400!=0 or a%400==0:
            if d<=29:
                v = True
        elif d<=28:
            v = True

    if v == True:
        print(' Data válida')
    else:
        print(' Data inválida')
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
elif b == 4:
    print ('{}exercicio 4{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber se um aluno passou ou não em uma materia!')
    print ()
    print ('-='*35)
    print ()
    n1 = float (input (' Digite a primeira nota: '))
    n2 = float (input (' Digite a segunda nota: '))
    n3 = float (input (' Digite a terceira nota: '))
    m = (n1+n2+n3)/3
    print ()
    print (' processando...')
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if m == 10:
        print (' Parabens!!, aluno aprovado com distinção!')
    elif m >= 7:
        print (' Aluno Aprovado!')
    else:
        print (' Aluno Reprovado!')
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
elif b == 5:
    print ('{}exercicio 5{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber se um número é par ou impar!')
    print ()
    print ('-='*35)
    print ()
    a= int (input (' Digite um valor: '))
    a = a%2
    print ()
    print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if a == 0:
        print (' o número é par!')
    else:
        print (' o número é impar!')
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
elif b == 6:
    print ('{}exercicio 6{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber se um valor é inteiro ou decimal!')
    print ()
    print ('-='*35)
    print ()
    a = float (input(' Digite um valor: '))
    print ()
    print (' processando...')  
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if a // 1 == a: 
        print(' O número {} inteiro!'.format (a)) # 2º q fiz diferente do que vocês pediram '-'
    else:
        print(' O número {} é decimal!'.format (a))
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
elif b == 7:
    print ('{}exercicio 7{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para saber o conceito de um aluno!')
    print ()
    print ('-='*35)
    print ()
    n1 = float (input(' Digite a primeira nota: '))
    n2 = float (input(' Digite a segunda nota: '))
    m = (n1+n2)/2
    print ()
    print (' processando...')  #quis deixar mais bonito ¯\_(ツ)_/¯
    sleep (2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if m >= 9.0:
        print (''' Com as notas {} e {}, e a media {} 
         O aluno tem o conceito A 
         Aprovado!'''.format (n1, n1, m))    
    elif m >= 7.5 and m < 9.0:
        print (''' Com as notas {} e {}, e a media {} 
         O aluno tem o conceito B 
         Aprovado!'''.format (n1, n1, m)) 
    elif m >= 6.0 and m < 7.5:
        print (''' Com as notas {} e {}, e a media {} 
         o aluno tem o conceito C
         Aprovado!'''.format (n1, n1, m))
    elif m >= 4.0 and m < 6.0:
        print (''' Com as notas {} e {}, e a media {} 
         o aluno tem o conceito D
         Reprovado!'''.format (n1, n1, m))
    else:
        print (''' Com as notas {} e {}, e a media {} 
         O aluno tem o conceito E
         Reprovado!'''.format (n1, n1, m))
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
elif b == 8:
    print ('{}exercicio 8{}'.format ('-='*15, '-='*15))
    print (' Esse programa foi feito para em contrar um possivel assasino.')
    print ('-='*35)
    print ()
    print (' Por favor, escrever com acentuação!')
    p1 = str (input(' Telefonou para a vítima?: '))
    p2 = str (input(' Esteve no local do crime?: '))
    p3 = str (input(' Devia para a vítima?: '))
    p4 = str (input(' Telefonou para a vítima?: '))
    p5 = str (input(' Já trabalhou com a vítima?: '))
    p1 = p1.upper()
    p2 = p2.upper()
    p3 = p3.upper()
    p4 = p4.upper()
    p5 = p5.upper()
    print ()
    print (' processando...')  
    sleep(2)
    print ()
    print ('{}Esses são os dados;{}'.format ('-='*10, '-='*14))
    print ()
    if p1 == 'SIM' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'SIM' :
        print (' O interrogado é o assasino!')
    elif p1 == 'SIM' and p2 == 'SIM' and p3 == 'NÃO' and p4 == 'NÃO' and p5 == 'NÃO' \
    or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'NÃO' \
    or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'NÃO' and p4 == 'SIM' and p5 == 'NÃO' \
    or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'NÃO' and p4 == 'NÃO' and p5 == 'SIM' \
    or p1 == 'NÃO' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'NÃO' \
    or p1 == 'NÃO' and p2 == 'SIM' and p3 == 'NÃO' and p4 == 'SIM' and p5 == 'NÃO' \
    or p1 == 'NÃO' and p2 == 'SIM' and p3 == 'NÃO' and p4 == 'NÃO' and p5 == 'SIM' \
    or p1 == 'NÃO' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'NÃO' \
    or p1 == 'NÃO' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'SIM' \
    or p1 == 'NÃO' and p2 == 'NÃO' and p3 == 'NÃO' and p4 == 'SIM' and p5 == 'SIM' : 
        print (' O interrogado é suspeito')# 2º fazendo esse, ficou mais fácil
    elif p1 == 'SIM' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'NÃO' \
    or p1 == 'SIM' and p2 == 'SIM' and p3 == 'NÃO' and p4 == 'SIM' and p5 == 'NÃO' \
    or p1 == 'SIM' and p2 == 'SIM' and p3 == 'NÃO' and p4 == 'NÃO' and p5 == 'SIM' \
    or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'NÃO' \
    or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'SIM' \
    or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'NÃO' and p4 == 'SIM' and p5 == 'SIM' \
    or p1 == 'NÃO' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'NÃO' \
    or p1 == 'NÃO' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'SIM' \
    or p1 == 'NÃO' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'SIM' \
    or p1 == 'NÃO' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'SIM' \
    or p1 == 'SIM' and p2 == 'NÃO' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'SIM' \
    or p1 == 'SIM' and p2 == 'SIM' and p3 == 'NÃO' and p4 == 'SIM' and p5 == 'SIM' \
    or p1 == 'SIM' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'NÃO' and p5 == 'SIM' \
    or p1 == 'SIM' and p2 == 'SIM' and p3 == 'SIM' and p4 == 'SIM' and p5 == 'NÃO':
        print (' O interrogado é cúmplice')
    else:
        print (' O interrogado é inocente')
    print ('{}feito por Murilo Ramalho com direito a copyright na nota'.format ('-='*29)) # é zoeira
else:
    print (' Número invalido')
input () #coloquei esse input livre para não finalizar quando for rodar (estou usando o notepad++)
