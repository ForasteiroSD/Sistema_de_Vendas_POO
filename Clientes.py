import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

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


class LimiteInsereCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title("Cliente")
        self.controle = controle

        self.frameCpf = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameEnd = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCpf.pack()
        self.frameNome.pack()
        self.frameEnd.pack()
        self.frameEmail.pack()
        self.frameButton.pack()

        self.labelCpf = tk.Label(self.frameCpf, text="CPF: ")
        self.labelCpf.pack(side="left")
        self.inputCpf = tk.Entry(self.frameCpf, width=20)
        self.inputCpf.pack(side="left")

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.labelEnd = tk.Label(self.frameEnd, text="Endereço: ")
        self.labelEnd.pack(side="left")
        self.inputEnd = tk.Entry(self.frameEnd, width=20)
        self.inputEnd.pack(side="left")

        self.labelEmail = tk.Label(self.frameEmail, text="Email: ")
        self.labelEmail.pack(side="left")
        self.inputEmail = tk.Entry(self.frameEmail, width=20)
        self.inputEmail.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton, text="Insere Cliente")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.InserirCliente)

        self.buttonLimpa = tk.Button(self.frameButton, text="Limpar")           
        self.buttonLimpa.pack(side="left")
        self.buttonLimpa.bind("<Button>", controle.LimparInsere)

        self.buttonConclui = tk.Button(self.frameButton, text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirInsere)


class LimiteConsultaCliente(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Cliente")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack()
        self.frameButton.pack()        

        self.labelCod = tk.Label(self.frameCod, text="Informe o CPF do cliente: ")
        self.labelCod.pack(side="left")
        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton, text="Consultar Cliente")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.MostrarCliente)

        self.buttonLimpa = tk.Button(self.frameButton, text="Limpar")           
        self.buttonLimpa.pack(side="left")
        self.buttonLimpa.bind("<Button>", controle.LimparMostra)

        self.buttonConclui = tk.Button(self.frameButton, text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.ConcluirMostra)


class LimiteMensagem:
    def __init__(self, titulo, string):
        messagebox.showinfo(titulo, string)
        
class CtrlClientes:
    def __init__(self, controlePrincipal):
        self._controlePrincipal = controlePrincipal

        if os.path.isfile('Clientes.pickle'):
            with open('Clientes.pickle', 'rb') as arq:
                self.listaClientes = pickle.load(arq)
        else:
            self.listaClientes = []

    def SalvaClientes(self):
        if len(self.listaClientes) > 0:
            with open('Clientes.pickle', 'wb') as arq:
                pickle.dump(self.listaClientes, arq)
        
    def InsereCliente(self):
        self._limInsere = LimiteInsereCliente(self)

    def InserirCliente(self, event):
        try:
            cpf = int(self._limInsere.inputCpf.get())
        except ValueError:
            LimiteMensagem('Erro', 'O CPF deve ser um número.')
            return
        
        nome = self._limInsere.inputNome.get()
        end = self._limInsere.inputEnd.get()
        email = self._limInsere.inputEmail.get()

        cliente = Cliente(cpf, nome, end, email)
        self.listaClientes.append(cliente)
        LimiteMensagem('Sucesso', 'Cliente inserido com sucesso')
        self.LimparInsere(event)

    def LimparInsere(self, event):
        self._limInsere.inputCpf.delete(0, tk.END)
        self._limInsere.inputNome.delete(0, tk.END)
        self._limInsere.inputEnd.delete(0, tk.END)
        self._limInsere.inputEmail.delete(0, tk.END)

    def ConcluirInsere(self, event):
        self._limInsere.destroy()
        
    def ConsultaCliente(self):
        self._limConsulta = LimiteConsultaCliente(self)
        
    def MostrarCliente(self, event):
        try:
            cpf = int(self._limConsulta.inputCod.get())
        except ValueError:
            LimiteMensagem('Erro', 'O CPF deve ser um número.')
            return
        
        string = 'Nome -- Endereço -- Email\n'
        for cliente in self.listaClientes:
            if cpf == cliente.cpf:
                string += f"{cliente.nome} -- {cliente.endereco} -- {cliente.email}\n"
                LimiteMensagem(f"Dados do Cliente {cpf}", string)
                self.LimparMostra(event)
                return
            
        LimiteMensagem('Erro', f'Cliente com CPF {cpf} não cadastrado.')


    def LimparMostra(self, event):
        self._limConsulta.inputCod.delete(0, tk.END)

    def ConcluirMostra(self, event):
        self._limConsulta.destroy()

    def ClientesCadastrados(self):
        return self.listaClientes
