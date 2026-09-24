class Usuario:
    def __init__(self, nome, email, senha_hash):
        self.id_usuario = None
        self._nome = nome
        self._email = email
        self._senha_hash = senha_hash