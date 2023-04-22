class Usuario:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self. telefone = telefone
        self.id = 0
        cadastro = {}

    def exibir_dados(self):
        """
        Exibe dados dos usuário cadastrado como nome, e-mail e telefone
        """
        print("Usuário: {}, E-mail: {}, Telefone: {}".format(self.nome, self.email, self.telefone))

