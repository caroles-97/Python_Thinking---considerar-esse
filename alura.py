print ("""
██╗██╗░░██╗░█████╗░░██████╗  ░██████╗░█████╗░██████╗░░█████╗░██████╗░██████╗░
██║██║░██╔╝██╔══██╗██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║█████═╝░███████║╚█████╗░  ╚█████╗░███████║██████╦╝██║░░██║██████╔╝██████╔╝
██║██╔═██╗░██╔══██║░╚═══██╗  ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚██╗██║░░██║██████╔╝  ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""") #https://fsymbols.com/es/letras/ para gerar letras bonitas
print('1. Cadastrar restaurante')  #alt shift 
print('2. Listar restaurantes')
print('3. Avaliar restaurante')
print('4. Sair')

option = input('Escolha uma opção: ')
# option = int('Escolha uma opção :') #se quiser transformar a opção em número inteiro, mas nesse caso não é necessário, pois o input já gera string, e as opções estão em string. Se fosse para comparar com números, aí sim seria necessário transformar a opção em número inteiro.
print(f'Voce escolheu a opção {option}')

if option == '1' :   #se a opção for igual a 1, faça isso
    print ('Cadastrar restaurante')
elif option == '2': 
    print ('Listar restaurantes')
elif option == '3':
    print ('Avaliar restaurante')
else:
    print ('Encerrando o programa')

