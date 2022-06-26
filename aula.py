import mysql.connector

conexao = mysql.connector.connect(
    host='localhost', #host do banco de dados
    user='root', #usuario do banco de dados
    password='', #senha do banco de dados
    database='teste', #nome do banco de dados
)

cursor = conexao.cursor() #executa os comandos

#CRUD

"""
#CREATE
nome = 'Juliana'
sobrenome = 'Hernandes'
idade = 28

comando = f"INSERT INTO clientes (nome, sobrenome, idade) VALUES ('{nome}','{sobrenome}',{idade})"
cursor.execute(comando) #executa o comando
conexao.commit() #edita o banco de dados
"""


"""
#READ
comando =f'SELECT * FROM clientes'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)#escreve o resultado na tela
"""

"""
#UPDATE
nome = 'Everson'
nova_idade = 1
comando = f"UPDATE clientes SET idade = {nova_idade} WHERE nome = '{nome}'"
cursor.execute(comando)
conexao.commit()
"""

#DELETE
id = 3
comando = f"DELETE FROM clientes WHERE id = {id}"
cursor.execute(comando)
conexao.commit()


cursor.close()#encerra o comando
conexao.close()#encerra a conexão

