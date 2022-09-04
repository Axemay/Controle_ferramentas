from secrets import randbelow
import tkinter as tk
from tkinter import ttk
from tkinter import Frame, ttk
from tkinter import END
from tkinter import messagebox
from tkinter import Scrollbar
from CRUD_F import *
from CRUD_T import *

class funcsRF (Csvf):
    def vazioF(self, msg):
        if msg == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")

        else:

            return msg

    def buscaF(self):
        self.view_frame2.delete(*self.view_frame2.get_children())

        # self.entry_nomeE.insert(END, '%')
        pesquisa = self.vPesquisa_ReservaF.get()
        buscacpflista = self.busca_cod(pesquisa)

        if pesquisa == "":
            messagebox.showerror("Erro", "O campo deve ser preenchidos")
        else:
            for i in buscacpflista:
                self.view_frame2.insert("", END, values=i)

            self.limpar_dadosFF()
            return
        self.select_listF()

    def select_listF(self):
        self.view_frame2.delete(*self.view_frame2.get_children())
        # self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        # lista = self.leitor_dict()
        # lista = self.leitura()
        lista = self.leitorf()

        for i in lista:
            if i == ["codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material", "tempo"]:
                continue

            self.view_frame2.insert("", END, values = i)

    def limpar_dadosFF(self):
        self.vPesquisa_ReservaF.delete(0, END)

    def doubleclickF(self, event):
        self.limpar_dadosFF()
        self.view_frame2.selection()
        global fvalida
        fvalida = True

        for n in self.view_frame2.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.view_frame2.item(n, 'values')

            self.vPesquisa_ReservaF.insert(END, col1)
            self.vPesquisa_ReservaF.insert(END, ",")
            self.vPesquisa_ReservaF.insert(END, col2)
            self.vPesquisa_ReservaF.insert(END, ",")
            self.vPesquisa_ReservaF.insert(END, col4)
            self.vPesquisa_ReservaF.insert(END, ",")
            self.vPesquisa_ReservaF.insert(END, col8)

class funcsRT (Csv):
    def vazio(self, msg):
        if msg == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")

        else:

            return msg

    def buscaT(self):


        self.view_frame1.delete(*self.view_frame1.get_children())

        # self.entry_nomeE.insert(END, '%')
        pesquisa = self.vPesquisa_ReservaT.get()
        buscacpflista = self.busca_cpf(pesquisa)

        if pesquisa == "":
            messagebox.showerror("Erro", "O campo deve ser preenchidos")
        else:
            for i in buscacpflista:
                self.view_frame1.insert("", END, values=i)

            self.limpar_dadosT()
            return
        self.select_listT()

    def select_listT(self):
        self.view_frame1.delete(*self.view_frame1.get_children())
        # self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        # lista = self.leitor_dict()
        # lista = self.leitura()
        lista = self.leitor()
        for i in lista:
            if i == ["cpf", "nome", "telefone", "turno", "equipe"]:
                continue
            self.view_frame1.insert("", END, values=i)

    def limpar_dadosT(self):
        self.vPesquisa_ReservaT.delete(0, END)

    def doubleclickT(self, event):
        self.limpar_dadosT()
        self.view_frame1.selection()
        global fvalida
        fvalida = True

        for n in self.view_frame1.selection():
            col1, col2, col3, col4, col5 = self.view_frame1.item(n, 'values')

            self.vPesquisa_ReservaT.insert(END, col1)
            self.vPesquisa_ReservaT.insert(END, ",")
            self.vPesquisa_ReservaT.insert(END, col2)
            self.vPesquisa_ReservaT.insert(END, ",")
            self.vPesquisa_ReservaT.insert(END, col3)

class Reserva (funcsRT, funcsRF) :
    def janela_cadastro_reservas(self):
        self.cadastro_reservas = tk.Toplevel()
        self.cadastro_reservas.title('Janela de Cadastro de Reservas')
        self.cadastro_reservas.iconphoto(False, tk.PhotoImage(file='../ico/reserva.png'))
        self.cadastro_reservas.configure(background='#B9B7BD')
        self.cadastro_reservas.geometry('1380x780')
        self.cadastro_reservas.resizable(True, True)
        self.cadastro_reservas.maxsize(width= 1920, height=1080) # dimensões máximas
        self.cadastro_reservas.minsize(width= 600, height= 400) # dimensões mínimas

####################################  FRAMES ==============================================================

        self.frame_1 = Frame(self.cadastro_reservas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_1.place(relx=0.048, rely=0.006, relwidth=0.9, relheight=0.23)

        self.frame_2 = Frame(self.cadastro_reservas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_2.place(relx=0.048, rely=0.245, relwidth=0.9, relheight=0.23)

        self.frame_3 = Frame(self.cadastro_reservas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_3.place(relx=0.01, rely=0.65, relwidth=0.98, relheight=0.34)
###################################  ENTRY LABELS BOTOES ===============================================

        self.Pesquisa_ReservaT = tk.Label(self.frame_1, text='Pesquisa por CPF:', bg='#ffd', fg='#0D0D0D',
                                          font=('poppins', 14, 'bold'))
        self.Pesquisa_ReservaT.place(relx=0.0, rely=0.0, relwidth=0.15, relheight=0.15)
        self.vPesquisa_ReservaT = tk.Entry(self.frame_1, bd=3, font=('poppins', 11, 'bold'))
        self.vPesquisa_ReservaT.place(relx=0.155, rely=0.0, relwidth=0.4, relheight=0.14)

    ##  Botão Tecnico
        self.bupT = tk.Button(self.frame_1, text="Pesquisar", bd=5, command= self.buscaT)
        self.bupT.place(relx=0.63, rely=0.0,  relwidth=0.1, relheight=0.15)

        self.batualizarT = tk.Button(self.frame_1, text="Atualizar Lista", bd=5, command= self.select_listT)
        self.batualizarT.place(relx=0.74, rely=0.0, relwidth=0.1, relheight=0.15)
    ##  ENTRY,  LABELS FERRAMENTA
        self.Pesquisa_ReservaF = tk.Label(self.frame_2, text='Pesquisa por Codigo da Ferramenta:', bg='#ffd', fg='#0D0D0D',
                                          font=('poppins', 11, 'bold'))
        self.Pesquisa_ReservaF.place(relx=0.0, rely=0.0, relwidth=0.224, relheight=0.15)
        self.vPesquisa_ReservaF = tk.Entry(self.frame_2, bd=3, font=('poppins', 11, 'bold'))
        self.vPesquisa_ReservaF.place(relx=0.23, rely=0.0, relwidth=0.4, relheight=0.14)

    ##  Botão FERRAMENTA
        self.bupT = tk.Button(self.frame_2, text="Pesquisar", bd=5, command=self.buscaF)
        self.bupT.place(relx=0.68, rely=0.0, relwidth=0.1, relheight=0.15)

        self.batualizarT = tk.Button(self.frame_2, text="Atualizar Lista", bd=5, command=self.select_listF)
        self.batualizarT.place(relx=0.79, rely=0.0, relwidth=0.1, relheight=0.15)
    ##  OUTROS BOTÕES, ENTRYS E LEBELS
        self.Data_entrega = tk.Label(self.cadastro_reservas, text='Data da Entrega :', bg='#ffd', fg='#0D0D0D',
                                      font=('poppins', 14, 'bold'))
        self.Data_entrega.place(relx=0.55, rely=0.5, relwidth=0.14, relheight=0.04)
        self.vData_entrega = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
        self.vData_entrega.place(relx=0.7, rely=0.5, relwidth=0.12, relheight=0.04)

        self.Hora_entrega = tk.Label(self.cadastro_reservas, text='Hora da Entrega :', bg='#ffd', fg='#0D0D0D',
                                     font=('poppins', 14, 'bold'))
        self.Hora_entrega.place(relx=0.55, rely=0.55, relwidth=0.14, relheight=0.04)
        self.vHora_entrega = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
        self.vHora_entrega.place(relx=0.7, rely=0.55, relwidth=0.12, relheight=0.04)
#-------------------------------------------------------------------
        self.Data_retirada = tk.Label(self.cadastro_reservas, text='Data da Retirada :', bg='#ffd', fg='#0D0D0D',
                                          font=('poppins', 14, 'bold'))
        self.Data_retirada.place(relx=0.14, rely=0.5, relwidth=0.14, relheight=0.04)
        self.vData_retirada = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
        self.vData_retirada.place(relx=0.29, rely=0.5, relwidth=0.12, relheight=0.04)

        self.Hora_retirada = tk.Label(self.cadastro_reservas, text='Hora da Retirada :', bg='#ffd', fg='#0D0D0D',
                                     font=('poppins', 14, 'bold'))
        self.Hora_retirada.place(relx=0.14, rely=0.55, relwidth=0.14, relheight=0.04)
        self.Hora_retirada = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
        self.Hora_retirada.place(relx=0.29, rely=0.55, relwidth=0.12, relheight=0.04)
#--------------------------------------------------------------------

        self.bupF = tk.Button(self.cadastro_reservas, text="Reservar", bd=5)
        self.bupF.place(relx=0.43, rely=0.6, relwidth=0.1, relheight=0.05)

############################### TRUE VIEW ==============================================================================
    ## true view frame 1
        self.dados_colunas = ("cpf", "nome", "telefone")

        self.view_frame1 = ttk.Treeview(self.frame_1, columns=self.dados_colunas, selectmode='browse')

        self.view_frame1.heading("#0", text="")
        self.view_frame1.heading("cpf", text="CPF")
        self.view_frame1.heading("nome", text="NOME")
        self.view_frame1.heading("telefone", text="TELEFONE")



        self.view_frame1.column("#0", width=0)
        self.view_frame1.column("cpf", minwidth=0, width=300, anchor=tk.CENTER)
        self.view_frame1.column("nome", minwidth=0, width=350, anchor=tk.CENTER)
        self.view_frame1.column("telefone", minwidth=0, width=350, anchor=tk.CENTER)


        self.view_frame1.place(relx=0.005, rely=0.155, relwidth=0.98, relheight=0.8)

        self.scrolbar_lista = Scrollbar(self.frame_1, orient="vertical", command=self.view_frame1.yview)
        self.view_frame1.configure(yscrollcommand=self.scrolbar_lista.set)
        self.scrolbar_lista.place(relx=0.985, rely=0.15, relwidth=0.015, relheight=0.8)

        self.scrolbar_lista2 = Scrollbar(self.frame_1, orient="horizontal", command=self.view_frame1.xview)
        self.view_frame1.configure(xscrollcommand=self.scrolbar_lista2.set)
        self.scrolbar_lista2.place(relx=0.005, rely=0.93, relwidth=0.97, relheight=0.07)
        self.view_frame1.bind("<Double-1>", self.doubleclickT)
        self.select_listT()

## true view frame 2
        self.dados_colunas = ( "codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material", "tempo")

        self.view_frame2 = ttk.Treeview(self.frame_2, columns=self.dados_colunas, selectmode='browse')

        self.view_frame2.heading("#0", text="")
        self.view_frame2.heading("codigo", text="CÓDIGO", )
        self.view_frame2.heading("descricao", text="DESCRIÇÃO", )
        self.view_frame2.heading("fabricante", text="FABRICANTE", )
        self.view_frame2.heading("voltagem", text="VOLTAGEM", )
        self.view_frame2.heading("partnumber", text="PARTNUMBER", )
        self.view_frame2.heading("tamanho", text="TAMANHO", )
        self.view_frame2.heading("unidade", text="UNIDADE")
        self.view_frame2.heading("tipo", text="TIPO")
        self.view_frame2.heading("material", text="MATERIAL")
        self.view_frame2.heading("tempo", text="TEMPO DE RESERVA")


        self.view_frame2.column("#0", width=0)
        self.view_frame2.column("codigo", minwidth=0, width=300, anchor=tk.CENTER)
        self.view_frame2.column("descricao", minwidth=0, width=300, anchor=tk.CENTER)
        self.view_frame2.column("fabricante", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("voltagem", minwidth=0, width=300, anchor=tk.CENTER)
        self.view_frame2.column("partnumber", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("tamanho", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("unidade", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("tipo", minwidth=0, width=350, anchor=tk.CENTER)
        self.view_frame2.column("material", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("tempo", minwidth=0, width=0, anchor=tk.CENTER)

        self.view_frame2.place(relx=0.005, rely=0.155, relwidth=0.98, relheight=0.8)

        self.scrolbar_lista = Scrollbar(self.frame_2, orient="vertical", command=self.view_frame2.yview)
        self.view_frame2.configure(yscrollcommand=self.scrolbar_lista.set)
        self.scrolbar_lista.place(relx=0.985, rely=0.15, relwidth=0.015, relheight=0.8)

        self.scrolbar_lista2 = Scrollbar(self.frame_2, orient="horizontal", command=self.view_frame2.xview)
        self.view_frame2.configure(xscrollcommand=self.scrolbar_lista2.set)
        self.scrolbar_lista2.place(relx=0.005, rely=0.93, relwidth=0.97, relheight=0.07)
        self.view_frame2.bind("<Double-1>", self.doubleclickF)
        self.select_listF()




    ## true view frame 3
        self.dados_colunas = ("cpf", "nome", "telefone", "codigo", "descricao", "voltagem", "tipo", "data", "hora")
        self.view_frame3 = ttk.Treeview(self.frame_3, columns=self.dados_colunas, selectmode='browse')

        self.view_frame3.heading("#0", text="")
        self.view_frame3.heading("cpf", text="CPF")
        self.view_frame3.heading("nome", text="NOME")
        self.view_frame3.heading("telefone", text="TELEFONE")
        self.view_frame3.heading("codigo", text="CÓDIGO", )
        self.view_frame3.heading("descricao", text="DESCRIÇÃO", )
        self.view_frame3.heading("voltagem", text="VOLTAGEM", )
        self.view_frame3.heading("tipo", text="TIPO")
        self.view_frame3.heading("data", text="DATA")
        self.view_frame3.heading("hora", text="HORA")


        self.view_frame3.column("#0", width=0)
        self.view_frame3.column("cpf", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("nome", minwidth=0, width=170, anchor=tk.CENTER)
        self.view_frame3.column("telefone", minwidth=0, width=150, anchor=tk.CENTER)
        self.view_frame3.column("codigo", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("descricao", minwidth=0, width=200, anchor=tk.CENTER)
        self.view_frame3.column("voltagem", minwidth=0, width=100, anchor=tk.CENTER)
        self.view_frame3.column("tipo", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("data", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("hora", minwidth=0, width=120, anchor=tk.CENTER)



        self.view_frame3.place(relx=0.005, rely=0.03, relwidth=0.98, relheight=0.90)

        self.scrolbar_lista = Scrollbar(self.frame_3, orient="vertical", command=self.view_frame3.yview)
        self.view_frame3.configure(yscrollcommand=self.scrolbar_lista.set)
        self.scrolbar_lista.place(relx=0.985, rely=0.03, relwidth=0.018, relheight=0.85)

        self.scrolbar_lista2 = Scrollbar(self.frame_3, orient="horizontal", command=self.view_frame3.xview)
        self.view_frame3.configure(xscrollcommand=self.scrolbar_lista2.set)
        self.scrolbar_lista2.place(relx=0.005, rely=0.93, relwidth=0.97, relheight=0.07)
        # self.view_frame2f.bind("<Double-1>", self.doubleclickf)
        # self.select_listT()