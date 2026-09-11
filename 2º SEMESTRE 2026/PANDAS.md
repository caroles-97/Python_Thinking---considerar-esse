**PANDAS**

~~~VARIÁVEL = NOME_DO_DATAFRAME ['_COLUNA_']



import pandas as pd     #pandas como pd - usaremos na função como pd
import matplotlib.pyplot as plt     #matplotlib - biblioteca gráfica    

dados = pd.read_excel('C:/Users/labsfiap/Downloads/pythopn/dataset_falhas_maquinas.xlsx')


#Filtro por máquinas do tipo M

df1 = dados[dados["Tipo"].isin(["M"])]
#dados fora= df inteiro
#dados Tipo = dentro do dataset filtre pela coluna Tipo 
#isin = dentro de "M"


x = df1 ["UDI"]
y = df1['Temperatura Processo [K]']

plt.plot(x,y)
plt.show()

##############################
1- Crie filtro para trazer apenas máquinas do tipo L, depois M, depois do tipo H. 
2 - Plote os 3 gráficos da temperatura do processo, considerando cada tipo de máquina. 
3 - QUais falhas estão presentes em máquinas do tipo L, M e H? 
4 - Qual a curva de velocidade de rotação e torque quando o tipo de falha é apenas power failure? 
5 - Quando selecionar apenas as falhas do tipo power failure, quais são os tipos de máquinas existentes? 
