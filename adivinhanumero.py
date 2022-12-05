import random
from random import randint




loop = True

while loop:
    escolha_computador = randint(1,10)
    escolha_humano = None
    print(escolha_computador)
    print("""
          Estou Pensando em um Número...
          de 1 a 10!
          Consegue adivinhar?""")
    escolha_numero = int(input('escolha: '))
    if escolha_numero == 1:
        if escolha_computador == 1:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    elif escolha_numero == 2:
        if escolha_computador == 2:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    elif escolha_numero == 3:
        if escolha_computador == 3:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    elif escolha_numero == 4:
        if escolha_computador == 4:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    elif escolha_numero == 5:
        if escolha_computador == 5:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    elif escolha_numero == 6:
        if escolha_computador == 6:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    elif escolha_numero == 7:
        if escolha_computador == 7:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    elif escolha_numero == 8:
        if escolha_computador == 8:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    elif escolha_numero == 9:
        if escolha_computador == 9:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    elif escolha_numero == 10:
        if escolha_computador == 10:
            print('voce adivinhou')
            loop = False
        else:
            print('vocÊ não adivinhou o número.')
    else:
        print('opção invalida.')
