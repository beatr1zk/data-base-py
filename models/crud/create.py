class Usuario:
    def __init__(self, nome, email, senha_hash):
        self.id = None
        self.nome = nome
        self.email = email
        self._senha_hash = senha_hash