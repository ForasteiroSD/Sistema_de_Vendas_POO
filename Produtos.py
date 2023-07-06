import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class Produto:
    def __init__(self, cod, desc, precoCompra, precoVenda, quant):
        self._codigo = cod
        self._descricao = desc
        self._precoCompra = precoCompra
        self._precoVenda = precoVenda
        self._quantidade = quant
        
    @property
    def codigo(self):
        return self._codigo
        
    @property
    def descricao(self):
        return self._descricao
        
    @property
    def precoCompra(self):
        return self._precoCompra
        
    @property
    def precoVenda(self):
        return self._precoVenda
        
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade
    
    
class LimiteInsereProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('360x225')
        self.title("Produto")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameDesc = tk.Frame(self)
        self.framePrecoC = tk.Frame(self)
        self.framePrecoV = tk.Frame(self)
        self.frameQuantidade = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameInfo = tk.Frame(self)
        self.frameCod.pack(pady=7)
        self.frameDesc.pack()
        self.framePrecoC.pack(pady=7)
        self.framePrecoV.pack()
        self.frameQuantidade.pack(pady=7)
        self.frameButton.pack()        
        self.frameInfo.pack(pady=7)

        self.labelCod = tk.Label(self.frameCod,text="Código do produto: ", width=22)
        self.labelCod.pack(side="left")
        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")

        self.labelDesc = tk.Label(self.frameDesc,text="Descrição do produto: ", width=22)
        self.labelDesc.pack(side="left")
        self.inputDesc = tk.Entry(self.frameDesc, width=20)
        self.inputDesc.pack(side="left")

        self.labelPrecoC = tk.Label(self.framePrecoC,text="Preço de compra do produto: ", width=22)
        self.labelPrecoC.pack(side="left")
        self.inputPrecoC = tk.Entry(self.framePrecoC, width=20)
        self.inputPrecoC.pack(side="left")

        self.labelPrecoV = tk.Label(self.framePrecoV,text="Preço de venda do produto: ", width=22)
        self.labelPrecoV.pack(side="left")
        self.inputPrecoV = tk.Entry(self.framePrecoV, width=20)
        self.inputPrecoV.pack(side="left")

        self.labelQuantidade = tk.Label(self.frameQuantidade,text="Quantidade de produtos: ", width=22)
        self.labelQuantidade.pack(side="left")
        self.inputQuantidade = tk.Entry(self.frameQuantidade, width=20)
        self.inputQuantidade.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Produto")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.InserirProduto)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Limpar")           
        self.buttonLimpa.pack(side="left", padx=4)
        self.buttonLimpa.bind("<Button>", controle.LimparInsere)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirInsere)

        self.labelInfo = tk.Label(self.frameInfo,text="Obs.: Para produtos já cadastrados digite apenas os campos:\n \
        código e quantidade")
        self.labelInfo.pack(side="top")


class LimiteConsultaProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('330x70')
        self.title("Produto")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack(pady=7)
        self.frameButton.pack()        

        self.labelCod = tk.Label(self.frameCod,text="Informe o código do produto: ", width=25)
        self.labelCod.pack(side="left")
        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Consultar Produto")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.MostrarProduto)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Limpar")           
        self.buttonLimpa.pack(side="left", padx=4)
        self.buttonLimpa.bind("<Button>", controle.LimparMostra)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirMostra)

class LimiteMensagem():
    def __init__(self, titulo, string):
        messagebox.showinfo(titulo, string)


class CtrlProdutos:
    def __init__(self, controlePrincial):
        self._controlePrincial = controlePrincial

        if os.path.isfile('Produtos.pickle'):
            with open('Produtos.pickle', 'rb') as arq:
                self.listaProdutos = pickle.load(arq)
        else:
            self.listaProdutos = []

    def SalvaProdutos(self):
        if(len(self.listaProdutos) > 0):
            with open('Produtos.pickle', 'wb') as arq:
                pickle.dump(self.listaProdutos, arq)
        
    def InsereProduto(self):
        self._limInsere = LimiteInsereProduto(self)

    def InserirProduto(self, event):
        try:
            codigo = int(self._limInsere.inputCod.get())
        except ValueError:
            LimiteMensagem('Erro', 'O código deve ser um número.')
            return
        
        try:
            quantidade = int(self._limInsere.inputQuantidade.get())
        except ValueError:
            LimiteMensagem('Erro', 'A quantidade deve ser um número.')
            return

        for produto in self.listaProdutos:
            if(codigo == produto.codigo):
                produto.quantidade = produto.quantidade + quantidade
                LimiteMensagem('Sucesso', 'Quantidade do produto alterada')
                self.LimparInsere(event)
                return
        
        desc = self._limInsere.inputDesc.get()
        try:
            precoV = float(self._limInsere.inputPrecoV.get())
            precoC = float(self._limInsere.inputPrecoC.get())
        except ValueError:
            LimiteMensagem('Erro', 'O preço de venda e de compra devem ser numéricos.')  
            return

        produto = Produto(codigo, desc, precoC, precoV, quantidade)
        self.listaProdutos.append(produto)
        LimiteMensagem('Sucesso', 'Produto inserido com sucesso')
        self.LimparInsere(event)

    def LimparInsere(self, event):
        self._limInsere.inputCod.delete(0, len(self._limInsere.inputCod.get()))
        self._limInsere.inputDesc.delete(0, len(self._limInsere.inputDesc.get()))
        self._limInsere.inputPrecoC.delete(0, len(self._limInsere.inputPrecoC.get()))
        self._limInsere.inputPrecoV.delete(0, len(self._limInsere.inputPrecoV.get()))
        self._limInsere.inputQuantidade.delete(0, len(self._limInsere.inputQuantidade.get()))

    def ConcluirInsere(self, event):
        self._limInsere.destroy()

    def ConsultaProduto(self):
        self._limConsulta = LimiteConsultaProduto(self)

    def MostrarProduto(self, event):
        try:
            codigo = int(self._limConsulta.inputCod.get())
        except ValueError:
            LimiteMensagem('Erro', 'O código deve ser um número.')
            return
        
        string = 'Estoque -- Descrição -- Preço de Venda\n'
        for produto in self.listaProdutos:
            if(codigo == produto.codigo):
                string += f'{produto.quantidade} -- {produto.descricao} -- R${produto.precoVenda:,.2f}\n'
                LimiteMensagem('Dados do produto ' + str(codigo), string)
                self.LimparMostra(event)
                return
            
        LimiteMensagem('Erro', 'Produto com código ' + str(codigo) + ' não cadastrado.')


    def LimparMostra(self, event):
        self._limConsulta.inputCod.delete(0, len(self._limConsulta.inputCod.get()))

    def ConcluirMostra(self, event):
        self._limConsulta.destroy()
        
    def FatProd(self):
        print("Faturamento por produto")

    def ProdutosCadastrados(self):
        return self.listaProdutos