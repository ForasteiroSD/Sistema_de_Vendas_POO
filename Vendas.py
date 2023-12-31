import tkinter as tk
from tkinter import messagebox
from datetime import datetime
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
        self.geometry('390x223')
        self.title("Venda")
        self.controle = controle

        self.frameClienteCpf = tk.Frame(self)
        self.frameClienteNome = tk.Frame(self)
        self.frameProd = tk.Frame(self)
        self.frameProdDados = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameClienteCpf.pack(pady=(7, 3))
        self.frameClienteNome.pack()
        self.frameProd.pack(pady=(3, 7))
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
        self.inputProdCod.pack(side="left", padx=(0, 15))

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
        self.buttonInsere.pack(side="left", padx=4)
        self.buttonInsere.bind("<Button>", controle.InformarData)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Cancelar Nota")           
        self.buttonLimpa.pack(side="left")
        self.buttonLimpa.bind("<Button>", controle.CancelarNota)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left", padx=4)
        self.buttonConclui.bind("<Button>", controle.ConcluirInsere)

class LimiteInformaData(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Data de Venda")
        self.controle = controle

        self.frameData = tk.Frame(self)
        self.frameInfo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameData.pack(pady=7)
        self.frameInfo.pack()
        self.frameButton.pack(pady=7)

        self.labelData = tk.Label(self.frameData,text="Informe a Data: ")
        self.labelData.pack(side="left")
        self.inputData = tk.Entry(self.frameData, width=15)
        self.inputData.pack(side="left")
        self.labelData = tk.Label(self.frameInfo,text="Digite a data do seguinte modo: DD/MM/AAAA")
        self.labelData.pack(side="top")

        self.buttonCriar = tk.Button(self.frameButton ,text="Emitir Nota")           
        self.buttonCriar.pack(side="left", padx=4)
        self.buttonCriar.bind("<Button>", controle.CriarNota)

        self.buttonCancela = tk.Button(self.frameButton ,text="Adicionar mais produtos")           
        self.buttonCancela.pack(side="left")
        self.buttonCancela.bind("<Button>", controle.CancelarData)

class LimiteConsultaVenda(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x128')
        self.title("Venda")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameIni = tk.Frame(self)
        self.frameFim = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack(pady=7)
        self.frameIni.pack()
        self.frameFim.pack(pady=7)
        self.frameButton.pack()        

        self.labelCod = tk.Label(self.frameCod,text="Informe o CPF do cliente: ", width=20)
        self.labelCod.pack(side="left")
        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")

        self.labelIni = tk.Label(self.frameIni,text="Informe a Data de Início: ", width=20)
        self.labelIni.pack(side="left")
        self.inputIni = tk.Entry(self.frameIni, width=20)
        self.inputIni.pack(side="left")
        
        self.labelFim = tk.Label(self.frameFim,text="Informe a Data Final: ", width=20)
        self.labelFim.pack(side="left")
        self.inputFim = tk.Entry(self.frameFim, width=20)
        self.inputFim.pack(side="left")
        

        self.buttonInsere = tk.Button(self.frameButton ,text="Consultar Vendas")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.MostrarVendas)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Limpar")           
        self.buttonLimpa.pack(side="left", padx=4)
        self.buttonLimpa.bind("<Button>", controle.LimparMostra)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirMostra)

class LimiteFaturamentoPeriodo(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Faturamento por Período")
        self.controle = controle

        self.frameDataI = tk.Frame(self)
        self.frameDataF = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameDataI.pack(pady=7)
        self.frameDataF.pack()
        self.frameButton.pack(pady=7)        

        self.labelDataI = tk.Label(self.frameDataI,text="Informe a data inicial: ", width=20)
        self.labelDataI.pack(side="left")
        self.inputDataI = tk.Entry(self.frameDataI, width=20)
        self.inputDataI.pack(side="left")

        self.labelDataF = tk.Label(self.frameDataF,text="Informe a data final: ", width=20)
        self.labelDataF.pack(side="left")
        self.inputDataF = tk.Entry(self.frameDataF, width=20)
        self.inputDataF.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Consultar Faturamento")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.FaturamentoPeriodo)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Limpar")           
        self.buttonLimpa.pack(side="left", padx=4)
        self.buttonLimpa.bind("<Button>", controle.LimparFatPeriodo)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirFatPeriodo)

class LimiteFaturamentoProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('325x70')
        self.title("Faturamento por Produto")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack(pady=7)
        self.frameButton.pack()        

        self.labelCod = tk.Label(self.frameCod,text="Informe o código do produto: ", width=24)
        self.labelCod.pack(side="left")
        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Consultar Faturamento")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.FaturamentoProduto)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Limpar")           
        self.buttonLimpa.pack(side="left", padx=4)
        self.buttonLimpa.bind("<Button>", controle.LimparFatProd)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirFatProd)

class LimiteLucroLiquido(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Lucro Líquido por Período")
        self.controle = controle

        self.frameDataI = tk.Frame(self)
        self.frameDataF = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameDataI.pack(pady=7)
        self.frameDataF.pack()
        self.frameButton.pack(pady=7)        

        self.labelDataI = tk.Label(self.frameDataI,text="Informe a data inicial: ", width=20)
        self.labelDataI.pack(side="left")
        self.inputDataI = tk.Entry(self.frameDataI, width=20)
        self.inputDataI.pack(side="left")

        self.labelDataF = tk.Label(self.frameDataF,text="Informe a data final: ", width=20)
        self.labelDataF.pack(side="left")
        self.inputDataF = tk.Entry(self.frameDataF, width=20)
        self.inputDataF.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Consultar Lucro Líquido")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.LucroPeriodo)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Limpar")           
        self.buttonLimpa.pack(side="left", padx=4)
        self.buttonLimpa.bind("<Button>", controle.LimparLucro)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirLucro)

class LimiteFatCliente(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x70')
        self.title("Faturamente por Cliente")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack()
        self.frameButton.pack()        

        self.labelCpf = tk.Label(self.frameCod, text="Informe o CPF do cliente: ")
        self.labelCpf.pack(side="left")
        self.inputCpf = tk.Entry(self.frameCod, width=20)
        self.inputCpf.pack(side="left", pady=7)

        self.buttonInsere = tk.Button(self.frameButton, text="Verificar Faturamento")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.FaturamentoCliente)

        self.buttonLimpa = tk.Button(self.frameButton, text="Limpar")           
        self.buttonLimpa.pack(side="left", padx=4)
        self.buttonLimpa.bind("<Button>", controle.LimparFatCliente)

        self.buttonConclui = tk.Button(self.frameButton, text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirFatCliente)

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
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            LimiteMensagem('Erro', 'Data inválida')
            return
       
        produtosCadastrados = self._controlePrincial.CtrlProdutos.ProdutosCadastrados()
        total = 0

        for produto in self.listaProdutos:
            total += produto[0].precoVenda * produto[1]
            for prod in produtosCadastrados:
                if prod.codigo == produto[0].codigo:
                    prod.quantidade = prod.quantidade - produto[1]
                    break

        v = Venda(len(self.listaVendas), data, self.listaProdutos, total, self.Cliente)
        self.listaVendas.append(v)

        self.listaProdutos = []
        self.Cliente = False
        LimiteMensagem('Sucesso', f'Nota Emitida. Valor total: R${total:,.2f}')
        self.CancelarData(event)

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
        self._limConsulta = LimiteConsultaVenda(self)

    def MostrarVendas(self, event):
        try:
            codCliente = int(self._limConsulta.inputCod.get())
        except ValueError:
            LimiteMensagem('Erro', 'CPF inválido')
            return
        
        dataInicial = self._limConsulta.inputIni.get()
        dataFinal = self._limConsulta.inputFim.get()

        try:
            dataInicial = datetime.strptime(dataInicial, "%d/%m/%Y")
            dataFinal = datetime.strptime(dataFinal, "%d/%m/%Y")
            if dataInicial > dataFinal:
                raise ValueError
        except ValueError:
            LimiteMensagem('Erro', 'Data(s) Inválida(s).')
            return

        vendasEncontradas = []
        for venda in self.listaVendas:
            if venda.cliente.cpf == codCliente and dataInicial <= venda.data <= dataFinal:
                vendasEncontradas.append(venda)

        if vendasEncontradas:
            mensagem = f"Vendas para o cliente {codCliente} de {dataInicial.strftime('%d/%m/%Y')} até {dataFinal.strftime('%d/%m/%Y')}:\n\n"
            for venda in vendasEncontradas:
                mensagem += f"Nota Fiscal: {venda.cod} - "
                mensagem += f"Valor Total: R${venda.valorTotal:,.2f}\n"
            LimiteMensagem('Vendas Encontradas', mensagem)
        else:
            LimiteMensagem('Vendas Não Encontradas', 'Nenhuma venda encontrada para o cliente no período especificado.')
    
    def LimparMostra(self, event):
        self._limConsulta.inputCod.delete(0, tk.END)
        self._limConsulta.inputIni.delete(0, tk.END)
        self._limConsulta.inputFim.delete(0, tk.END)

    def ConcluirMostra(self, event):
        self._limConsulta.destroy()
        
    def MaisVendidos(self):
        prods = self._controlePrincial.CtrlProdutos.ProdutosCadastrados()
        maisVendidos = []
        qntsVendidas = {}
        
        for venda in self.listaVendas:
            for prod in venda.produtos:
                try:
                    qntsVendidas[prod[0].codigo] += prod[1]
                except:
                    qntsVendidas[prod[0].codigo] = prod[1]
        
        for i in sorted(qntsVendidas, key = qntsVendidas.get, reverse=True):
            maisVendidos.append((i, qntsVendidas[i]))
        
        maisVendidos = maisVendidos[:10]
        # print(maisVendidos)
        
        string = 'Código - Descrição - Preço de venda - Unidades vendidas\n'
        for codigo in maisVendidos:
            for prod in prods:
                if(prod.codigo == codigo[0]):
                    string += f'{prod.codigo} -  {prod.descricao} - R${prod.precoVenda:,.2f} -  {codigo[1]} unidade(s)\n'
                    
        LimiteMensagem("10 Produtos mais vendidos", string)

    
    def FatCliente(self):
        self._limFatCliente = LimiteFatCliente(self)
    
    def FaturamentoCliente(self, event):
        try:
            cpfSel = int(self._limFatCliente.inputCpf.get())
        except:
            LimiteMensagem("Erro", "CPF Inválido")
            return
        
        cliente = None
        total = 0
        for venda in self.listaVendas:
            if(venda.cliente.cpf == cpfSel):
                cliente = venda.cliente
                total += venda.valorTotal
        
        if(cliente == None): LimiteMensagem("Erro", "Cliente inexistente")
        else:
            string = f"Nome: {cliente.nome}\n"
            string += f"Faturamento: {total}"
            LimiteMensagem("Faturamento", string)
            self.LimparFatCliente(event)
    
    def LimparFatCliente(self, event):
        self._limFatCliente.inputCpf.delete(0, tk.END)
    
    def ConcluirFatCliente(self, event):
        self._limFatCliente.destroy()

    def FatPeriodo(self):
        self._limitefatPeriodo = LimiteFaturamentoPeriodo(self)

    def FaturamentoPeriodo(self, event):
        datai = self._limitefatPeriodo.inputDataI.get()
        dataf = self._limitefatPeriodo.inputDataF.get()

        try:
            datai = datetime.strptime(datai, "%d/%m/%Y")
            dataf = datetime.strptime(dataf, "%d/%m/%Y")
            if datai > dataf:
                raise ValueError
        except ValueError:
            LimiteMensagem('Erro', 'Data(s) inválida(s)')
            return
        
        totalV = 0
        for venda in self.listaVendas:
            if venda.data >= datai and venda.data <= dataf:
                totalV += venda.valorTotal

        if totalV == 0:
            LimiteMensagem(f'Faturamento {datai.day}/{datai.month}/{datai.year} até {dataf.day}/{dataf.month}/{dataf.year}', 'Não houverem vendas nesse período.')
            return
        
        LimiteMensagem(f'Faturamento {datai.day}/{datai.month}/{datai.year} até {dataf.day}/{dataf.month}/{dataf.year}', f'Faturamento: R${totalV:,.2f}')
        self.LimparFatPeriodo(event)

    def LimparFatPeriodo(self, event):
        self._limitefatPeriodo.inputDataI.delete(0, len(self._limitefatPeriodo.inputDataI.get()))
        self._limitefatPeriodo.inputDataF.delete(0, len(self._limitefatPeriodo.inputDataF.get()))

    def ConcluirFatPeriodo(self, event):
        self._limitefatPeriodo.destroy()
        
    def FatProd(self):
        self._limiteFatProduto = LimiteFaturamentoProduto(self)
    
    def FaturamentoProduto(self, event):
        cod = self._limiteFatProduto.inputCod.get()

        if cod == '':
            LimiteMensagem('Erro', 'Digite um código')
            return
        
        try:
            cod = int(cod)
        except ValueError:
            LimiteMensagem('Erro', 'O código deve ser um valor inteiro')
            return
        
        totalV = 0
        for venda in self.listaVendas:
            for produtos in venda.produtos:
                if cod == produtos[0].codigo:
                    totalV += produtos[0].precoVenda * produtos[1]
        
        if totalV == 0:
            LimiteMensagem(f'Faturamento Produto {cod}', 'Não houverem vendas desse produto.')
            return

        LimiteMensagem(f'Faturamento Produto {cod}', f'Faturamento: R${totalV:,.2f}')
        self.LimparFatProd(event)

    def LimparFatProd(self, event):
        self._limiteFatProduto.inputCod.delete(0, len(self._limiteFatProduto.inputCod.get()))

    def ConcluirFatProd(self, event):
        self._limiteFatProduto.destroy()

    def LucroLiquido(self):
        self._limiteLucroLiquido = LimiteLucroLiquido(self)

    def LucroPeriodo(self, event):
        datai = self._limiteLucroLiquido.inputDataI.get()
        dataf = self._limiteLucroLiquido.inputDataF.get()

        try:
            datai = datetime.strptime(datai, "%d/%m/%Y")
            dataf = datetime.strptime(dataf, "%d/%m/%Y")
            if datai > dataf:
                raise ValueError
        except ValueError:
            LimiteMensagem('Erro', 'Data(s) inválida(s)')
            return
        
        totalV = 0
        totalC = 0
        for venda in self.listaVendas:
            if venda.data >= datai and venda.data <= dataf:
                for produtos in venda.produtos:
                    totalV += produtos[0].precoVenda * produtos[1]
                    totalC += produtos[0].precoCompra * produtos[1]

        
        if totalV == 0:
            LimiteMensagem(f'Lucro Líquido {datai.day}/{datai.month}/{datai.year} até {dataf.day}/{dataf.month}/{dataf.year}', 'Não houverem vendas nesse período.')
            return
        
        lucro = totalV - totalC
        LimiteMensagem(f'Lucro Líquido {datai.day}/{datai.month}/{datai.year} até {dataf.day}/{dataf.month}/{dataf.year}', f'Valor Vendido: R${totalV:,.2f}\nValor gasto: R${totalC:,.2f}\nLucro Líquido: R${lucro:,.2f}')
        self.LimparLucro(event)

    def LimparLucro(self, event):
        self._limiteLucroLiquido.inputDataI.delete(0, len(self._limiteLucroLiquido.inputDataI.get()))
        self._limiteLucroLiquido.inputDataF.delete(0, len(self._limiteLucroLiquido.inputDataF.get()))

    def ConcluirLucro(self, event):
        self._limiteLucroLiquido.destroy()