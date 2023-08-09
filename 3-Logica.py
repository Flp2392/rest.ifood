from funções import *


conexao = sqlite3.connect('ifood.db')
cursor = conexao.cursor()
         
while True:
        print("\n--- Menu ---")
        print("1. Clientes")
        print("2. Motoqueiro")
        print("3. Restaurante")
        print("4. Pagamento")
        print("5. Pedidos")
        print("6. Encerrar atendimento")
        option = input("Escolha a opção desejada: ")

        if option == '1':
            cadastro_cliente()
        elif option == '2':
            inserir2()
        elif option == '3':
            inserir3()
        elif option == '4':
            inserir4()
        elif option == '5':
            inserir5()
        elif option == '6':
            conexao.close()
            break
            
        else:
            print("Opção inválida.")

























'''
#apresentação

cadastro_cliente (
    if nome in clientes:
        print('cliente já cadastrado')
        pedidos()
    else:
        insert into.....

)


#clicou em cadastro:
cadastro_cliente()

'''





