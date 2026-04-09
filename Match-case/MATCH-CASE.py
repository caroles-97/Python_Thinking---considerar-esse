
print ( "SISTEMA DE NOTAS")
print ("*********\n")

print ( " 1. Verificar nota")
print ( " 2. Editar nota")
print ( " 3. Inserir nota")
print ( " 4. Excluir nota")
print ( " 5. Sair")

opc = input ("Escolha uma opção:")


match opc: #Verifique essa variável opção
    case " 1":
        print ("Você escolheu a opção de verificar a nota")
    case " 2":
        print (" Você escolheu a opção de Editar a nota")
    case " 3":
        print ("Você escolheu a opção de inserir a nota")
    case " 4":
        print ("Você escolheu a opção de excluir nota")
    case " 5":
        print ("Saída. Obrigada e volte sempre")

    case _:  # _ qualquer coisa
        print ("Opção inválida")


