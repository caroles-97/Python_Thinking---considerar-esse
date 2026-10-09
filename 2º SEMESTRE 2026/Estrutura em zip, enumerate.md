Exemplos de estruturas com zip

# Ex.1

nomes = ['ana', 'bruno', 'carla']
notas = [19, 22, 21]

for nome, idade in zip(nomes, notas):
    print(nome, idade)
##################################

# Ex.2
produtos = ['arroz', 'feijão', 'macarrão', 'leite']
precos = [25.90, 8.50, 6.90, 5.20]

for produto, preco in zip(produtos, precos):
    print(f'{produto}: R${preco:2f}')

##################################

# Ex.3
produtos = ['notebook', 'mouse', 'teclado', 'monitor']
precos = [3500, 80, 150, 900]
quantidades = [3, 15, 8, 5]

faturamento_total = 0 + 10500 + 1200 + 1200 + 4500

for produto, preco, qtd in zip(produtos, precos, quantidades):
    faturamento = preco * qtd
    faturamento_total += faturamento
    
    print(f'{produto} R$ {faturamento:.2f}')

print(f"Faturamento total - {faturamento_total}")

# Ex.4
nomes = ['ana', 'bruno', 'carla']
notas = [9, 5, 3]

for aluno, nota in zip(nomes, notas):
    
    if nota >= 7:
        situacao = 'Aprovado'
    elif nota >=5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'
    
    print(aluno, nota, situacao)
    
# Ex.5
cidades = ['SP', 'AM', 'CE', 'RJ']
temperaturas = [28, 35, 36, 38]

dados = dict(zip(cidades, temperaturas))

for cidade, temperatura in dados.items():
    if temperatura >= 30:
        print("Alerta de calor", cidade)
        
# Ex.6
equipamentos = ['motor', 'transformador', 'gerador']
temperaturas = [75, 92, 81]

for indice, (equipamento, temp) in enumerate(
        zip(equipamentos, temperaturas), start=1):
    print(f"{indice} - {equipamento}: {temp}ºC")

# Exercício

1. Utilizando as listas meses, vendas_2025 e vendas_2026. Calcule/Mostre: 

a) Mostre as 2 informações para cada mês.
b) Calcule a soma das vendas por mês.
c) Mostre o valor total.
d) A variação mensal das vendas.

meses = ['janeiro', 'fevereiro', 'março', 'abril']
vendas_2025 = [10000, 12000, 15000, 13000]
vendas_2026 = [12000, 11000, 18000, 16000]

(atual - anterior / anterior) * 100

*Resolução dos itens a, b e c*

meses = ['janeiro', 'fevereiro', 'março', 'abril']
vendas_2025 = [10000, 12000, 15000, 13000]
vendas_2026 = [12000, 11000, 18000, 16000]

faturamento_total = 0

for meses, vendas2025, vendas2026 in zip(meses,vendas_2025, vendas_2026):
    print(f'{meses} - {vendas2025} e {vendas2026}')
    
    faturamento = vendas2025 + vendas2026
    faturamento_total += faturamento
    print(f'{meses} com faturamento de R${faturamento:.2f}')
    
print (f'Valor total será de {faturamento_total}')
    