import tkinter as tk
from tkinter import messagebox
import Produtos as pdt
import Clientes as clt
import Vendas as vnd

class LimitePrincipal():
    def __init__(self, root, controle):
        self.root = root
        self.controle = controle
        self.root.geometry('350x200')
        
        self.menuBar = tk.Menu(self.root)
        self.menuProdutos = tk.Menu(self.menuBar)
        self.menuClientes = tk.Menu(self.menuBar)
        self.menuFaturamento = tk.Menu(self.menuBar)
        self.menuVendas = tk.Menu(self.menuBar)
        self.menuSair = tk.Menu(self.menuBar)
        
        self.menuProdutos.add_command(label='Inserir', command=self.controle.InsereProduto)
        self.menuProdutos.add_command(label='Consultar', command=self.controle.ConsultaProduto)
        self.menuBar.add_cascade(label="Produtos", menu=self.menuProdutos)

        
        self.menuClientes.add_command(label='Insere', command=self.controle.InsereCliente)
        self.menuClientes.add_command(label='Consulta', command=self.controle.ConsultaCliente)
        self.menuBar.add_cascade(label="Clientes", menu=self.menuClientes)
        
        self.menuFaturamento.add_command(label='Faturamento por Produto', command=self.controle.FatProd)
        self.menuFaturamento.add_command(label='Faturamento por Cliente', command=self.controle.FatCliente)
        self.menuFaturamento.add_command(label='Faturamento por Período', command=self.controle.FatPeriodo)
        self.menuFaturamento.add_command(label='Lucro Líquido', command=self.controle.LucroLiquido)
        self.menuBar.add_cascade(label="Faturamento", menu=self.menuFaturamento)
        
        self.menuVendas.add_command(label='Vender', command=self.controle.Vender)
        self.menuVendas.add_command(label='Vendas por Cliente', command=self.controle.VendaCliente)
        self.menuVendas.add_command(label='10 Mais Vendidos', command=self.controle.MaisVendidos)
        self.menuBar.add_cascade(label="Vendas", menu=self.menuVendas)
        
        self.menuSair.add_command(label='Salvar', command=self.controle.Salvar)
        self.menuBar.add_cascade(label="Sair", menu=self.menuSair)
        
        self.root.config(menu=self.menuBar)
        
        self.frameLogo = tk.Frame(self.root)
        self.frameLogo.pack(expand=True)
        
        self.logoImg = tk.PhotoImage(file='Logo.png')
        self.logo = tk.Label(self.frameLogo, image=self.logoImg)
        self.logo.place(x=0, y=0, relwidth=0.5, relheight=0.5)
        self.logo.pack()
        

class CtrlPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Loja de Roupas MVC")
        
        self.CtrlProdutos = pdt.CtrlProdutos(self)
        self.CtrlClientes = clt.CtrlClientes(self)
        self.CtrlVendas = vnd.CtrlVendas(self)
        
        self.limite = LimitePrincipal(self.root, self)
        self.root.mainloop()
        
    def InsereProduto(self):
        self.CtrlProdutos.InsereProduto()
    
    def ConsultaProduto(self):
        self.CtrlProdutos.ConsultaProduto()
    
    def InsereCliente(self):
        self.CtrlClientes.InsereCliente()
    
    def ConsultaCliente(self):
        self.CtrlClientes.ConsultaCliente()
    
    def FatProd(self):
        self.CtrlProdutos.FatProd()
    
    def FatCliente(self):
        self.CtrlClientes.FatCliente()
    
    def FatPeriodo(self):
        self.CtrlVendas.FatPeriodo()
    
    def LucroLiquido(self):
        self.CtrlVendas.LucroLiquido()
    
    def Vender(self):
        self.CtrlVendas.InsereVenda()
    
    def VendaCliente(self):
        self.CtrlVendas.ConsultaVenda()
    
    def MaisVendidos(self):
        self.CtrlVendas.MaisVendidos()
    
    def Salvar(self):
        self.CtrlProdutos.SalvaProdutos()
        self.CtrlClientes.SalvaClientes()
        self.CtrlVendas.SalvaVendas()
        print("Salvar")
        self.root.destroy()

if __name__== '__main__':
    prog = CtrlPrincipal()