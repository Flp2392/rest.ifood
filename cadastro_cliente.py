import sqlite3


# Função para criar uma nova conta no sistema
def cadastro_cliente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereço = input("Endereço: ")
    
    #Conecta ao banco de dados
    conn = sqlite3.connect('ifood.db')
    cursor = conn.cursor()

    # Inserir o novo registro na tabela 'contas'
    cursor.execute(f"INSERT INTO clientes (nome, telefone, endereço) VALUES ('{nome}', '{endereço}', '{telefone}')")
    conn.commit()

   
    print("Cadastro criado com sucesso!")

    conn.close()