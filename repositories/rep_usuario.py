from banco.db import conectar
from models.crud.create import Usuario

def tabela_usuario():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute ("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_usuario VARCHAR(150) NOT NULL,
            email_usuario VARCHAR(254) NOT NULL UNIQUE,
            senha_hash VARCHAR(254) NOT NULL
            )
    """
    )
    conexao.commit()
    conexao.close()


def criar_usuario(usuario):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO usuarios(nome_usuario, email_usuario, senha_hash)
        VALUES (%s, %s, %s)
    """, (usuario.nome, usuario.email, usuario._senha_hash)
    )
    conexao.commit()
    id_gerado = cursor.lastrowid
    conexao.close()

    usuario.id = id_gerado
    return id_gerado

def buscar_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT nome, email, senha_hash FROM usuario 
    WHERE email = %s
    """, (email))

    usuario = cursor.fetchall()
    conexao.close()

    if usuario is None:
        return None
    else:   
        id_usuario, nome, email, senha_hash = usuario
        usuario = Usuario(nome, email, senha_hash)
        usuario.id = id_usuario
        return usuario
        