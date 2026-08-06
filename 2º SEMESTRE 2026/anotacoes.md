For - estrutura de repetição 

1º SEMESTRE 2026 : FOR, LISTAS [], APPEND. 

lista_nomes = []  - criando variavel lista "nomes" para armazenar cada variável. Criado lista para armazenar.
lista_idades = []
lista_sexo = []


Estrutura de repetição para solicitar esses dados 2x:

for i in range (2):    - REPETIÇÃO
    print(f"\nDados da {i+1}ª pessoa:")   ---SAÍDA
    nome = input("Digite o nome: ")   -------- ENTRADA (INPUT)
    lista_nomes.append(nome) ----- por meio do append. o NOME vai ser enviado para a lista NOMES

    IDADE = int(input("Digite sua idade: "))   -------- ENTRADA (INPUT)
    lista_idades.append(idade)

    sexo = input("Digite M para masculino e F para feminino: ")   -------- ENTRADA (INPUT)
    lista_sexo.append(sexo)  ---------- append. ARMAZENA NA LISTA    
print(lista_nomes)
print(lista_idades)
print(lista_sexo)

LISTA COM SUBLISTA COM TODAS AS INFORMAÇÕES DO USUÁRIO: 

print (Meu nome é {nome}, tenho {idade} e sou do sexo {sexo})

