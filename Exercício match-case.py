''' Escolha uma opção - perguntando a qtde. No final, terá que ter o valor do pedido da pessoa
1.Lanche  -> 1. Cachorro-Quente: R$ 15.00 , 2. Hamburguer: R$20.00
2. bebida  ->  1 . Refrigerante R$6.00 , 2. Suco natural: R$10.00
3. Sobremesa  ->  1. Açaí  R$ 25.00 , 2. Sorvete R$ 18.00
4. Sair   -   Até logo, volte sempre.

# Se a pessoa digitar 1, terá outro submenu'''

print (" *** Kikis food *** ")
print ("***************\n")

print ( " 1. Lanche")
print ( " 2. Bebida")
print ( " 3. Sobremesa")
print ( " 4. Sair")

opc = input ("Escolha uma opção: ")


match opc:
    case "1":
        print (" a. Cachorro-quente - R$ 15.00")
        print (" b. Hamburguer - R$20.00 ")

        opc1 = input ("Escolha seu lanche: ")

        match opc1:
            case "a":
                opc11 = int (input ("Escolha sua quantidade: "))
                VP = 15 * opc11

    case "2":
        print(" a. Refrigerante - R$ 6.00")
        print(" b. Suco Natural - R$10.00 ")

        opc2 = input("Escolha sua bebida: ")

        match opc2:
            case " 2":
                print(" 1. Refrigerante - R$ 6.00")
                print(" 2. Suco Natural - R$10.00 ")

    case " 3":
        print(" 1. Açaí - R$ 25.00")
        print(" 2. Sorvete - R$18.00 ")

        opc3 = input("Escolha sua sobremesa:")

        match opc3:
            case " 2":
                print(" 1. Açaí - R$ 25.00")
                print(" 2. Sorvete - R$18.00 ")

    case " 4":
        print (" Até logo, volte sempre :) !")

print (VP)




