#Checkpoint é CP - M1 é a média do 1º semestre
# Spring é SP
# MF vou considerar 6 pois é o mínimo que precisa para passar de ano -> 6.
"""
Veja a expressão aritmética abaixo:

M1 = ((CP1 + CP2) / 2) * 0.2 + (SP1+SP2) * 0.1 + GS1 * 0.6
M2 = ((CP1 + CP2) / 2) * 0.2 + (SP1+SP2) * 0.1 + GS2 * 0.6
MF = M1 * 0.4 + M2 * 0.6

Agora, vamos montar um algoritmo em Python para saber o quanto o aluno precisa tirar para passar de ano.
input ("Informe a nota do CP1:")
input ("Informe a nota do CP2:")

Mas precisamos guardar a nota no sistema, então atribuiremos uma variável.

CP1 = float (input ("Informe a nota do CP1:"))  #Todo dado que entrar via input, gera string
CP2 = float (input ("Informe a nota do CP2:"))
SP1 = float (input ("Informe a nota do SP1:"))  #Todo dado que entrar via input, gera string
SP2 = float (input ("Informe a nota do SP2:"))
GS1 = float (input ("Informe a nota do GS1:"))

M1 = (CP1+CP2) * 0.1 + (SP1+SP2) * 0.1 + GS1 * 0.6

print ("Sua média é " , M1)
"""
