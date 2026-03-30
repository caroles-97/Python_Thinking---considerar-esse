#Calculadora de tarifas de transporte público - valor a depender do passageiro e distância percorrida
#tarifa = 2.50/km   

print("Calculadora de tarifas de transporte público: Tipos de passageiros")
print ("*********\n")

tarifa = 2.50

#VT = valor total

print ( " 1. Estudante")
print ( " 2. Trabalhador")
print ( " 3. Idoso")
print ( " 4. Comum")

opc = input ("Escolha uma opção: ")
variaveldecontrole = 0  #duplo teste para quando chegar no matchcase case_

match opc:
    case "1":
        print (" 1. Estudante tem 50% de desconto no valor total")

        distancia = float(input("Quantos km serão percorridos: "))

        VT = tarifa * 50/100 * distancia #Calculo do valor total com o desconto estudante

    case "2":
        print(" 2. Trabalhador tem 20% de desconto no valor total")
        distancia = float(input("Quantos km serão percorridos: "))
        VT = tarifa * 80/100 * distancia  # Calculo do valor total com o desconto de trabalhador, pois é 20% de desconto. O valor total será com 80%.
    
    case "3":
        print("3. A passagem de transporte público para idoso é gratuita!")
        VT = tarifa * 0

    case "4":
        print("4. Passageiro comum paga o valor completo")
        distancia = float(input("Quantos km serão percorridos: "))

        VT = tarifa * distancia 

    case _:  #qualquer coisa
        print ("Opção inválida. Até breve.")
        variaveldecontrole = 1  #como é /= 0 , ele checa e não aparece a informação com o ifvariavelcontrole==0

if variaveldecontrole == 0:
    print(f"O valor final da passagem é de R$ {VT}.") 
    #NÃO FOI PASSADO COMO EXIBIR VALOR FINAL COM DUAS CASAS DECIMAIS. 
