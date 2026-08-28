input


print (f"Valor de a: {a}")



**ESTRUTURA DE CONDIÇÃO**

if a > b:       se a > b
    print("A é maior")

elif a==b:  *CONDIÇÕES INTERMEDIÁRIAS, quando não se encaixa no if/ else*
    print("A e B são iguais")

else:       senao...
    print ("B é maior")


**ESTRUTURA DE REPETIÇÃO: FOR/WHILE**   **lista/ tupla**

Para repetir algo. 


for i in range (3):       *Vai repetir 3x*  *i é cada posição*
    nome = input ("Insira seu nome: ")
    print(nome)


lista = []  *Quero guardar as info dentro da lista*
lista =['a', 'b','c']

for i in range (3):       *Vai repetir 3x*
    nome = input ("Insira seu nome: ")
    print(nome)
    *lista.append(nome)*     **Anexando a variável nome na lista**

    OU

tupla = ()  *Estrutura de lista IMUTÁVEL*

tupla = ('a', 'b', 'c') *posição: 0, 1, 2 - sempre inicia do índice 0*

for k in tupla:     *para posição(k) na tupla*
    print(k)
    a
    b
    c

print(tupla[0]) *printa a*
print(tupla[1]) *printa b*
print(tupla[2]) *printa c*

**Transformar a tupla em lista: usamos função list - transforma tudo em lista**
lista_noma = list(tupla)
print(lista_nova)

###      WHILE  ###

1. Pensar na variável que vai iniciar
2. Pensar na variável que vai incrementar
3. Limite

i = 0   *iniciando em 0*

while i <= 3:   *enquanto i for menor ou igual a 3*
    print(i)
    i += 1      *incrementa +1 na contagem*


i = 0   *iniciando em 0*

while i <= 3:   *enquanto i for menor ou igual a 3*
    if i == 2:  *se 2, vai parar de rodar*
        break
    print(i)
    i += 1      *incrementa +1 na contagem. i = i+1*

 ****decrementador -= 1 : i = i-1**


for i in rang (1,6):    *vai rodar de 1 a 5*
    if i == 3:      
        continue    *vai pular o 3. Vai continuar a estrutura de repetição, sem o 3*
    print(i)





def