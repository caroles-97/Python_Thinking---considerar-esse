# Pedir 3 notas (válidas) de CPs entre 0 a 10 - CP1, CP2, CP3
# Determinar as 2 maiores notas. Apresentar a média dos CPs (1 casa decimal).

# print ("Notas FIAP\n1.CP1\n2.CP2\n3.CP3\n")

# CP1 = float(input("Digita a nota da CP1: "))
#     while CP1 < 0 or CP1 > 10:
    
# CP2 = float(input("Digita a nota da CP2: "))
#     while CP2 < 0 or CP2 > 10:

# CP3 = float(input("Digita a nota da CP3: "))
#     while CP3 < 0 or CP3 > 10:
    




# Pedir 10 idades para as pessoas e imprimir quantos são maiores de idade: 
# 1. PRECISO  GUARDAR AS IDADES? SIM, fazer lista. NÃO, usar o WHILE.

# WHILE idade > 18 , vamos contabilizar

respostas = 1 
maioresDeIdade = 0
# esse seria o cont

while respostas < 10:
    idade = int(input(f"Digite a {respostas}ª idade: "))
    if idade >= 18 :
        maioresDeIdade += 1
    
    respostas += 1
    # Incremento - ELE PARA O LOOPING.  neste caso, indica qtas respostas foram dadas. 

print (f"Existem {maioresDeIdade } pessoas maiores de idade.")





