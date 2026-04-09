### EXERCÍCIO DA LANCHONETE
sair = False
valor = 0
print('Lanchonete CARCARÁ, seja bem vindo!\n')
 
while sair == False:
    escolha = input('Faça o seu pedido:\n1. Lanche\n2. Bebida\n3. Sobremesa\nOpção: ')
 
    match escolha:
        case '1':
            lanche = input('\nEscolha seu lanche:\n\n1. Cachorro-Quente: R$15,00\n2. Hambúrguer: R$20,00\nOpção: ')
           
            quantidade = int(input('Insira a quantidade: '))
 
            if quantidade > 0:    
                match lanche:
                    case '1':
                        print(f'\nO valor para {quantidade} de cachorro-quente ficará: R${float(quantidade*15)}\n')
 
                        valor += 15 * quantidade
                    case '2':
                        print(f'\nO valor para {quantidade} de hambúrguer ficará: R${float(quantidade*20)}\n')
 
                        valor += 20 * quantidade
                    case _:
                        print('Insira uma opção válida !\n')
            else:
                print('\nInsira uma quantidade válida !\n')
           
        case '2':
            bebida = input('\nEscolha sua bebida:\n\n1. Refrigerante: R$6,00\n2. Suco natural: R$10,00\nOpção: ')
           
            quantidade = int(input('Insira a quantidade: '))
           
            if quantidade > 0:  
                match bebida:
                    case '1':
                        print(f'\nO valor para {quantidade} de refrigerante ficará: R${float(quantidade*6)}\n')
 
                        valor += 6 * quantidade
                    case '2':
                        print(f'\nO valor para {quantidade} de suco natural ficará: R${float(quantidade*10)}\n')
 
                        valor += 10 * quantidade
                    case _:
                        print('Insira uma opção válida !\n')
            else:
                print('\nInsira uma quantidade válida !\n')
 
        case '3':
            sobremesa = input('\nEscolha sua sobremesa: \n\n1. Açaí: R$25,00 \n2. Sorvete: R$18,00\nOpção: ')
           
            quantidade = int(input('Insira a quantidade: '))
           
            if quantidade > 0:  
                match sobremesa:
                    case '1':
                        print(f'\nO valor para {quantidade} de açaí ficará: R${float(quantidade*25)}\n')
 
                        valor += 25 * quantidade
                    case '2':
                        print(f'\nO valor para {quantidade} de sorvete ficará: R${float(quantidade*18)}\n')
 
                        valor += 18 * quantidade
                    case _:
                        print('Insira uma opção válida !\n')
            else:
                print('\nInsira uma quantidade válida !\n')
 
        case _:
            print('\nInsira uma opção válida (1 à 3)!\n')
 
    resposta = input('Deseja finalizar? (s/n)\n')
    if resposta == 's':
        sair = True
 
if valor > 0:
    print(f'\nO total do seu pedido é de R${float(quantidade*valor)} !')