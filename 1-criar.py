import sqlite3

conn = sqlite3.connect('ifood.db')

def restaurante():
    conn.execute('''
        CREATE TABLE restaurante(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        telefone TEXT,
        endereço TEXT)
      
        ''')
    

    conn.execute('''
        CREATE TABLE clientes(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        telefone TEXT,
        endereço TEXT)
      
        ''')
    

    conn.execute('''
        CREATE TABLE motoqueiro(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        telefone TEXT)
        
      
        ''')
    

    conn.execute('''
        CREATE TABLE pedidos(
        id INTEGER PRIMARY KEY,
        id_restaurante INTEGER,
        id_clientes INTEGER,
        id_motoqueiro INTEGER,
        data_hora DATE,
        FOREIGN KEY (id_restaurante) REFERENCES restaurante (id)
        FOREIGN KEY (id_clientes) REFERENCES clientes (id)
        FOREIGN KEY (id_motoqueiro) REFERENCES motoqueiro (id))
        ''')
    
    conn.execute('''
        CREATE TABLE pagamento(
        id INTEGER PRIMARY KEY,
        id_clientes INTEGER,
        id_motoqueiro INTEGER,
        id_pedidos INTEGER,
        data_hora DATE,
        valor TEXT,
        FOREIGN KEY (id_pedidos) REFERENCES pedidos (id)
        FOREIGN KEY (id_clientes) REFERENCES clientes (id)
        FOREIGN KEY (id_motoqueiro) REFERENCES motoqueiro (id))
        ''')

restaurante()
conn.commit()
conn.close()