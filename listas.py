nome = ['Carol' , 'Arthur', 'Victor']
print(nome[2])

# Na LISTA SEMPRE inicia-se o i contando 0, 1, 2 etc
# i === índice === item

# Usando o FOR na LISTA: Aqui o "nome" torna-se uma "lista". 
# Neste caso, 'Carol' é uma lista 
for item in nome [0]:
    print(item)



# Colocar a lista de nº somando os valores : vamos usar FOR
lista = [3,10,7,8,1,9,8,5,8]

total = 0 
# Começamos com 0 pq é soma

for item in lista:
    total += item

print(total)



# Calculando o nº mínimo e o nº máximo: vamos criar variável min

min = lista[0]
# min é a lista índice/ posição zero 
max = lista[0]
for item in lista:
    if min > item:
        min = item
    if max < item: 
        max = item

        # Ele verifica os números e vai atribuindo o valor conforme o que foi descrito.

print (f"O menor item é {min}\n"
       f"o maior item é {max}")