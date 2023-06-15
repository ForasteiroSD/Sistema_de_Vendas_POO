class Cliente:
    def __init__(self, cpf, nome, endereco, email):
        self._cpf = cpf
        self._nome = nome
        self._endereco = endereco
        self._email = email
        
    @property
    def cpf(self):
        return self._cpf
        
    @property
    def nome(self):
        return self._nome
        
    @property
    def endereco(self):
        return self._endereco
        
    @property
    def email(self):
        return self._email


class LimiteInsereCliente:
    def __init__(self):
        print("LimiteInsereCliente")


class LimiteConsultaCliente:
    def __init__(self):
        print("LimiteConsultaCliente")


class CtrlClientes:
    def __init__(self, controlePrincial):
        self._controlePrincial = controlePrincial
        
    def InsereCliente(self):
        self._limInsere = LimiteInsereCliente()
        
    def ConsultaCliente(self):
        self._limConsulta = LimiteConsultaCliente()
        
    def FatCliente(self):
        print("Faturamento por cliente")