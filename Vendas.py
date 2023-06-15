class Venda:
    def __init__(self, cod, data):
        self._cod = cod
        self._data = data
        self._produtos = [] # Lista de produtos: Cada produto deve ser uma sublista com o produto e a quantidade
        self._valorTotal = 0
        
    @property
    def cod(self):
        return self._cod
        
    @property
    def data(self):
        return self._data
        
    @property
    def produtos(self):
        return self._produtos
        
    @property
    def valorTotal(self):
        return self._valorTotal
    
    
class LimiteInsereVenda:
    def __init__(self):
        print("LimiteInsereVenda")


class LimiteConsultaVenda:
    def __init__(self):
        print("LimiteConsultaVenda")


class CtrlVendas:
    def __init__(self, controlePrincial):
        self._controlePrincial = controlePrincial
        
    def InsereVenda(self):
        self._limInsere = LimiteInsereVenda()
        
    def ConsultaVenda(self):
        self._limConsulta = LimiteConsultaVenda()
        
    def FatPeriodo(self):
        print("Faturamento por período")
        
    def LucroLiquido(self):
        print("Lucro Líquido")
        
    def MaisVendidos(self):
        print("10 mais vendidos")