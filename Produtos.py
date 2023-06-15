class Produto:
    def __init__(self, cod, desc, precoCompra, precoVenda, quant):
        self._cod = cod
        self._desc = desc
        self.precoCompra = precoCompra
        self._precoVenda = precoVenda
        self._quant = quant
        
    @property
    def cod(self):
        return self._cod
        
    @property
    def desc(self):
        return self._desc
        
    @property
    def precoCompra(self):
        return self._precoCompra
        
    @property
    def precoVenda(self):
        return self._precoVenda
        
    @property
    def quant(self):
        return self._quant
    
    
class LimiteInsereProduto:
    def __init__(self):
        print("LimiteInsereProduto")


class LimiteConsultaProduto:
    def __init__(self):
        print("LimiteConsultaProduto")


class CtrlProdutos:
    def __init__(self, controlePrincial):
        self._controlePrincial = controlePrincial
        
    def InsereProduto(self):
        self._limInsere = LimiteInsereProduto()
        
    def ConsultaProduto(self):
        self._limConsulta = LimiteConsultaProduto()
        
    def FatProd(self):
        print("Faturamento por produto")