# Criando uma função que exibe mensagem de boas-vindas

# Vamos colocar primeiro o 'import' que é para importar a biblioteca, depois as funções, variáveis e a main (sistema/ lógica).

def exibir_msg():
    # Vamos colocar o que ela deve fazer ao ser chamada
    print("Sejam Bem-Vindos!")

#Main - aqui vamos chamar a função 
#exibir_msg()
#OU
#para repetir, vamos usar o for
for i in range (10):
    exibir_msg()


# Criando função para verificar se o número é par ou ímpar

# Definindo o nome da nossa função: par_ou_impar
def par_ou_impar(numero):
    if numero % 2 == 0:
        # se esse numero que recebi, dividido por 2 for igual a 0 será:
        print('Par')
    else:
        print('Ímpar')
#Main
Numero = int(input('Informe o número: '))
# Continuando a MAIN. Aqui chamamos a função para fazer as verificações:
par_ou_impar(Numero)



# Função que dobra o número informado
def dobrar(numero):
    numero = numero *2
    print (numero)
#Main
N = int(input('Informe o número: '))
dobrar (N)
print(N)


# Função para calcular a área de um triângulo
def calcular_area(base, altura):
    area = (base * altura)/2
    print (f'Área do triângulo: {area}')
#Main
base = float (input('Informe a base:'))
altura = float (input('Informe a altura: '))
calcular_area (base,altura)


# Função para calcular a área de um triângulo
def calcular_area(base, altura):
    area = (base * altura)/2
    # Vai devolver o resultado para o usuário/ para a MAIN. Para devolver ao usuário, precisa guardar.
    return area
#Main
base = float (input('Informe a base:'))
altura = float (input('Informe a altura: '))

# Guardando o return
A = calcular_area (base,altura)

#Mostrando ao usuário o valor de A:
print (f'Área do triângulo: {A}')

#OU 
print (f'Área do triângulo: {calcular_area (base,altura)}')



#EXERCÍCIOS: FUNÇÕES

#Programa que solicita 2 notas de provas. Faça uma função que receba as notas por parâmetro e exibe a mensagem "Você foi aprovado!" ou "Você foi reprovado!". Considere 6.0 a média mínima para aprovação. 

def validar_nota(nota):
    # Teremos vários ifs
    while nota < 0 or nota >10:
        nota = float(input('Informe uma nota válida (entre 0 e 10): '))
        #neste caso, precisamos que a nota válida retorne ao usuário
    return nota 

def media (nota1 , nota2):
    media = (N1 + N2) / 2
    if media >= 6:
        print (f' Aprovado ! \n Sua média é {media}')
    else:
        print (f' Reprovado ! \n Sua média é {media}')

#Main: onde vai iniciar o sistema quando rodar
N1 = float(input('Informe a primeira nota: '))

# Aqui armazena a nota1:
N1 = validar_nota(N1)

# Para a nota 2:
N2 = float(input('Informe a segunda nota: '))
N2 = validar_nota(N2) 

media (N1, N2)



