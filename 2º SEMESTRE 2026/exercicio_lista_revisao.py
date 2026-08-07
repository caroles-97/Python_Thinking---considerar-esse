lista = [[], [], [], [], []]   
contador = 0 

while contador <=3:    
    print (f"\n Dados do seu (contador +  1)º carro:")

    marca = input ("Digite a marca do seu carro:")
    versao = int (input("Digite a versão do carro:"))
    ano = int(input("Digite o ano do carro:"))
    cor = input ("Digite a cor do carro:")
    ipva = input ("IPVA foi pago? (S/N):")

    lista[0].append(marca) 
    lista[1].append(versao) 
    lista[2].append(ano)
    lista[3].append(cor)  
    lista[4].append(ipva)  
    contador += 1

print(lista)

# **Abordagem 2 - com esse cód a resposta fica numa única sublista - gostei mais**
lista = [[], [], [], [], []]    -- crio 5 sublistas para as informações
contador = 0 

while contador < 4:     -- contando o 0 como nº inicial, vou ir até o número 3
    print (f"\n Dados do seu (contador +  1)º carro:")

    marca = input ("Digite a marca do seu carro:")
    versao = int (input("Digite a versão do carro:"))
    ano = int (input("Digite o ano do carro:"))
    cor = input ("Digite a cor do carro:")
    ipva = input ("IPVA foi pago? (S/N):")
    
    dados = [marca, versao, ano, cor, ipva]
    lista.append(dados)
    contador += 1

print(lista)


# LIÇÃO DE CASA FAZER O EXERCÍCIO USANDO FOR - USAR A BASE DO EXERCÍCIO DE REVISÃO