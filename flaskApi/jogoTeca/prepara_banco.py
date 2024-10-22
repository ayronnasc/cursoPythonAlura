import mysql.connector
from mysql.connector import errorcode

print("conectando...")

try:
    print(" Tentando Conectar ... ")
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password=''
    )
except mysql.connector.Error as err:
    print('\n Aba de Excecoes :')
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuario ou senha')
    else:
        print(err,' ------ erro econtrado')

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS 'jogoteca';")
cursor.execute("CREATE DATABASE 'jogoteca'; ")
cursor.execute("USE 'jogoteca'; ")

# criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
                    CREATE TABLE `jogos` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `none` varchar(50) NOT NULL,
                    `categoria` varchar(40) NOT NULL,
                    `categoria` varchar(40) NOT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
                        ''')

TABLES['Usuarios'] = ('''
                        CREATE TABLE `usuarios` (
                            `nome` varchar(20) NOT NULL,
                            `nickname` varchar(8) NOT NULL,
                             `senha` varchar(100) NOT NULL,
                            PRIMARY KEY (`nickname`)
                        )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
                        
                        ''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já Existe')
        else:
            print(err.msg)
    else:
        print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ("Ayron Nascimento", "Yrin10k", 'fani'),
    ("Igor sardanself", "Monty345", 'nay'),
    ("Ryan Araldo", "Rysu", 'persona'),

]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('SELECT * FROM jogoteca.usuarios')
print(' -------------- Usuarios: ---------------')
for user in cursor.fetchall():
    print(user[1])

    #inserindo Jogos
jogos_sql = 'INSERT INTO jogos(nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
    ('God of War', 'Action', 'PS2'),
    ('Pokemon Emerald', 'RPG TURN', 'Game Boy Advanced'),
    ('Dark Souls Remastered', 'DARK FANTASY', 'PS4'),
]

cursor.executemany(jogos_sql, jogos)

cursor.execute('SELECT * FROM jogoteca.jogos')
print('------------- JOGOS --------------')
for jogo in cursor.fetchall():
    print(jogo[1])

