import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class Venda:
    def __init__(self, cod, data, produtos, total, cliente):
        self._cod = cod
        self._data = data
        self._produtos = produtos # Lista de produtos: Cada produto deve ser uma sublista com o produto e a quantidade
        self._valorTotal = total
        self._cliente = cliente

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
    
    @property
    def cliente(self):
        return self._cliente
    
class LimiteInsereVenda(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title("Venda")
        self.controle = controle

        self.frameClienteCpf = tk.Frame(self)
        self.frameClienteNome = tk.Frame(self)
        self.frameProd = tk.Frame(self)
        self.frameProdDados = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameClienteCpf.pack()
        self.frameClienteNome.pack()
        self.frameProd.pack()
        self.frameProdDados.pack()
        self.frameButton.pack()       

        self.labelClienteCpf = tk.Label(self.frameClienteCpf,text="Digite o CPF do cliente: ")
        self.labelClienteCpf.pack(side="left")
        self.cpfDigitado = tk.StringVar()
        self.cpfDigitado.trace_add('write', self.controle.VerificaCliente)
        self.inputClienteCpf = tk.Entry(self.frameClienteCpf, width=20, textvariable=self.cpfDigitado)
        self.inputClienteCpf.pack(side="left")
        self.labelClienteNome = tk.Label(self.frameClienteNome,text="")
        self.labelClienteNome.pack(side="top")

        self.labelProdCod = tk.Label(self.frameProd,text="Código do produto: ")
        self.labelProdCod.pack(side="left")
        self.codDigitado = tk.StringVar()
        self.codDigitado.trace_add('write', self.controle.VerificaProduto)
        self.inputProdCod = tk.Entry(self.frameProd, width=15, textvariable=self.codDigitado)
        self.inputProdCod.pack(side="left")

        self.labelProdQuant = tk.Label(self.frameProd,text="Quantidade: ")
        self.labelProdQuant.pack(side="left")
        self.inputProdQuant = tk.Entry(self.frameProd, width=8)
        self.inputProdQuant.pack(side="left")

        self.textProdDados = tk.Text(self.frameProdDados, height=5, width=45)
        self.textProdDados.pack(pady=10)
        self.textProdDados.config(state=tk.DISABLED)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Produto")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.InserirProduto)

        self.buttonInsere = tk.Button(self.frameButton ,text="Emitir Nota")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.InformarData)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Cancelar Nota")           
        self.buttonLimpa.pack(side="left")
        self.buttonLimpa.bind("<Button>", controle.CancelarNota)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirInsere)

class LimiteInformaData(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title("Data de Venda")
        self.controle = controle

        self.frameData = tk.Frame(self)
        self.frameInfo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameData.pack()
        self.frameInfo.pack()
        self.frameButton.pack()

        self.labelData = tk.Label(self.frameData,text="Informe a Data: ")
        self.labelData.pack(side="left")
        self.inputData = tk.Entry(self.frameData, width=10)
        self.inputData.pack(side="left")
        self.labelData = tk.Label(self.frameInfo,text="Digite a data do seguinte modo: DD/MM/AAAA")
        self.labelData.pack(side="top")

        self.buttonCriar = tk.Button(self.frameButton ,text="Emitir Nota")           
        self.buttonCriar.pack(side="left")
        self.buttonCriar.bind("<Button>", controle.CriarNota)

        self.buttonCancela = tk.Button(self.frameButton ,text="Adicionar mais produtos")           
        self.buttonCancela.pack(side="left")
        self.buttonCancela.bind("<Button>", controle.CancelarData)

class LimiteConsultaVenda:
    def __init__(self):
        print("LimiteConsultaVenda")

class LimiteMensagem:
    def __init__(self, titulo, string):
        messagebox.showinfo(titulo, string)

class CtrlVendas:
    def __init__(self, controlePrincial):
        self._controlePrincial = controlePrincial

        if os.path.isfile('Vendas.pickle'):
            with open('Vendas.pickle', 'rb') as arq:
                self.listaVendas = pickle.load(arq)
        else:
            self.listaVendas = []

    def SalvaVendas(self):
        if len(self.listaVendas) > 0:
            with open('Vendas.pickle', 'wb') as arq:
                pickle.dump(self.listaVendas, arq)
        
    def InsereVenda(self):
        self.listaProdutos = []
        self.Cliente = False
        self._limInsere = LimiteInsereVenda(self)
        
    def VerificaCliente(self, var, index, mode):
        if self.Cliente != False:
            LimiteMensagem('Erro', 'Você não pode alterar o cliente durante a emissão de uma nota.')
            self._limInsere.cpfDigitado.set(self.Cliente.cpf)
            return
        
        if len(self._limInsere.cpfDigitado.get()) == 0:
            self._limInsere.labelClienteNome.configure(text='')
            return
        
        try:
            cpf = int(self._limInsere.cpfDigitado.get())
        except ValueError:
            self._limInsere.labelClienteNome.configure(text='O CPF deve ser um número inteiro')
            return
        
        clientes = self._controlePrincial.CtrlClientes.ClientesCadastrados()
        for cliente in clientes:
            if (cliente.cpf == cpf):
                self._limInsere.labelClienteNome.configure(text=cliente.nome)
                return
            
        self._limInsere.labelClienteNome.configure(text='Não existe cliente com este CPF')

    def VerificaProduto(self, var, index, mode):
        if len(self._limInsere.codDigitado.get()) == 0:
            self._limInsere.textProdDados.config(state='normal')
            self._limInsere.textProdDados.delete('1.0', tk.END)
            self._limInsere.textProdDados.config(state='disabled')
            return
        
        try:
            cod = int(self._limInsere.codDigitado.get())
        except ValueError:
            self._limInsere.textProdDados.config(state='normal')
            self._limInsere.textProdDados.delete('1.0', tk.END)
            self._limInsere.textProdDados.insert('1.0', 'O código deve ser um valor inteiro')
            self._limInsere.textProdDados.config(state='disabled')
            return
        
        produtos = self._controlePrincial.CtrlProdutos.ProdutosCadastrados()
        for produto in produtos:
            if (produto.codigo == cod):
                self._limInsere.textProdDados.config(state='normal')
                self._limInsere.textProdDados.delete('1.0', tk.END)
                self._limInsere.textProdDados.insert('1.0', f'{produto.descricao} -- R${produto.precoVenda:,.2f}')
                self._limInsere.textProdDados.config(state='disabled')
                return
        
        self._limInsere.textProdDados.config(state='normal')
        self._limInsere.textProdDados.delete('1.0', tk.END)
        self._limInsere.textProdDados.insert('1.0', 'Não existe produto com este código')
        self._limInsere.textProdDados.config(state='disabled')

    def InserirProduto(self, event):
        if len(self.listaProdutos) == 10:
            LimiteMensagem('Erro', 'Você não pode inserir mais de 10 produtos em uma nota')
            return
        
        if self.Cliente == False:
            cliente = self._limInsere.labelClienteNome["text"]
            if cliente == '' or cliente == 'Não existe cliente com este CPF' or cliente == 'O CPF deve ser um número inteiro':
                LimiteMensagem('Erro', 'Antes de inserir um cliente é necessário selecionar um cliente')
                return
        
        texto = self._limInsere.textProdDados.get('1.0', tk.END)
        texto = texto[:-1]

        if texto == 'Não existe produto com este código' or texto == 'O código deve ser um valor inteiro' or \
        texto == '':
            LimiteMensagem('Erro', 'Digite um código de produto válido')
            return
        
        cod = int(self._limInsere.codDigitado.get())
        try:
            quant = self._limInsere.inputProdQuant.get()
            quant = int(quant)
        except ValueError:
            LimiteMensagem('Erro', 'Valor inválido para a quantidade')
            return
        
        if quant < 1:
            LimiteMensagem('Erro', 'Valor inválido para a quantidade')
            return

        for produto in self.listaProdutos:
            if cod == produto[0].codigo:
                LimiteMensagem('Erro', 'Você já inseriu este produto na nota')
                return

        produtos = self._controlePrincial.CtrlProdutos.ProdutosCadastrados()
        for produto in produtos:
            if produto.codigo == cod:
                if produto.quantidade < quant:
                    LimiteMensagem('Erro', 'Não há quantidade suficiente disponível no estoque')
                else:
                    self.listaProdutos.append([produto, quant])
                    LimiteMensagem('Sucesso', 'Produto Inserido com sucesso')
                    if self.Cliente == False:
                        clientes = self._controlePrincial.CtrlClientes.ClientesCadastrados()
                        cpf = int(self._limInsere.cpfDigitado.get())
                        for cliente in clientes:
                            if (cliente.cpf == cpf):
                                self.Cliente = cliente
                                break
                    self._limInsere.inputProdCod.delete(0, len(self._limInsere.inputProdCod.get()))
                    self._limInsere.inputProdQuant.delete(0, len(self._limInsere.inputProdQuant.get()))
                    self._limInsere.textProdDados.config(state='normal')
                    self._limInsere.textProdDados.delete('1.0', tk.END)
                    self._limInsere.textProdDados.config(state='disabled')

    def InformarData(self, event):
        if len(self.listaProdutos) == 0:
            LimiteMensagem("Erro", 'Você não pode emitir uma nota sem um cliente e produtos')
            return
        self._limiteData = LimiteInformaData(self)
    
    def CriarNota(self, event):
        data = self._limiteData.inputData.get()
        data1 = data.split('/')
        if len(data1) == 3:

            try:
                data1[0] = int(data1[0])
                data1[1] = int(data1[1])
                data1[2] = int(data1[2])
            except ValueError:
                LimiteMensagem('Erro', 'Data inválida')
                return
            
            if data1[0] < 1 or data1[1] < 1:
                LimiteMensagem('Erro', 'Data inválida')
                return

            if data1[1] == 4 or data1[1] == 6 or data1[1] == 9 or data1[1] == 11:
                if data1[0] > 30:
                    LimiteMensagem('Erro', 'Data inválida')
                    return
            elif data1[1] == 2:
                if data1[0] > 28:
                    LimiteMensagem('Erro', 'Data inválida')
                    return
            else:
                if data1[0] > 31:
                    LimiteMensagem('Erro', 'Data inválida')
                    return

            produtosNota = []
            produtosCadastrados = self._controlePrincial.CtrlProdutos.ProdutosCadastrados()
            total = 0

            for produto in self.listaProdutos:
                produtosNota.append(produto)
                total += produto[0].precoVenda * produto[1]
                for prod in produtosCadastrados:
                    if prod.codigo == produto[0].codigo:
                        prod.quantidade = prod.quantidade - produto[1]
                        break

            v = Venda(len(self.listaVendas), data, produtosNota, total, self.Cliente)
            self.listaVendas.append(v)

            self.listaProdutos.clear()
            self.Cliente = False
            LimiteMensagem('Sucesso', f'Nota Emitida. Valor total: R${total:,.2f}')
            self.CancelarData(event)
            return
        
        LimiteMensagem('Erro', 'Data inválida')

    def CancelarData(self, event):
        self._limiteData.destroy()

    def CancelarNota(self, event):
        self.listaProdutos.clear()
        self.Cliente = False
        self._limInsere.inputProdCod.delete(0, len(self._limInsere.inputProdCod.get()))
        self._limInsere.inputProdQuant.delete(0, len(self._limInsere.inputProdQuant.get()))
        self._limInsere.textProdDados.config(state='normal')
        self._limInsere.textProdDados.delete('1.0', tk.END)
        self._limInsere.textProdDados.config(state='disabled')
        self._limInsere.labelClienteNome.configure(text='')
        self._limInsere.cpfDigitado.set('')
        LimiteMensagem("Sucesso", 'Nota Cancelada')

    def ConcluirInsere(self, event):
        self._limInsere.destroy()

    def ConsultaVenda(self):
        self._limConsulta = LimiteConsultaVenda()
        
    def FatPeriodo(self):
        print("Faturamento por período")
        
    def LucroLiquido(self):
        print("Lucro Líquido")
        
    def MaisVendidos(self):
        print("10 mais vendidos")