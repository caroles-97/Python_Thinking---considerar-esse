#  *****FUNÇÃO APPLY*****
import pandas as pd

dicionario = {
    'Pontos A': [10, 20, 30, 40, 50],
    'Pontos B': [100, 200, 300, 400, 500],
    'Pontos C': [1, 2, 3, 4, 5]
    }

df1 = pd.DataFrame(dicionario)

def classificar(a):
    if a >= 30:
        return 'baixo'
    elif a >= 40:
        return 'medio'
    else:
        return 'alto' 
print(df1['Pontos A'].apply(classificar))   #apply conecta o Pontos A com classificar, junto com a estrutura de repetição
#Estrtutura de repetição está dentro do apply