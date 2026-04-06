print ("CALCULADORA DE TARIFAS\n")
print ("1. Estudante\n 2. Trabalhador\n 3. Idoso\n 4. Comum\n ")

tarifa = 2.5
erro = "Opção inválida!"

opc = int (input("Escolha uma opção: "))
km = float(input("Informe a distância percorrida: "))

match opc:
    case 1 : 
        total = km * tarifa /2
    case 2 : 
        total = km * tarifa * 0.8
    case 3 : 
        total = 0
    case 4 : 
        total = km * tarifa
    case _: 
        print(erro)
    #    Para opção inválida, imprimimos a variável 'erro'.  

# Só vou imprimir o total se o opc tiver entre 1 e 4. Qualquer coisa fora disso, não será impresso.

print (f"Sua passagem custa R$ {total:.2f}")

