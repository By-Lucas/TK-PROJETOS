
from logging import root
from tkinter import * #BIBLIOTECA tkinter PARA FAZER INTERFACE
from tkinter import ttk #Biblioteca pra criar treevew
import pymysql.cursors
from mysql.connector import charsets
from tkinter import messagebox


#CODIGO ABAIXO MOSTRA AS FUNCOES DE COMO PRINTAR RESULTADO DECLARANDO,
#SEMPRE É USADO self PARA PODER MOSTRAR RESULTADO E FAAZER CALCULOS E DECLARAR AS VARIAVEIS
'''
class Janelalogin():
    def __init__(self):
        self.x = 10
        print(self.x)
    
    def mostrar(self):
        print('como vai voce')

Janelalogin().mostrar()
'''
'''================================================'''
#SEGUNDA JANELA, MENU PRINCIPAL
class AdminJanela():

    def CadastrarProduto(self):
        self.cadastrar = Tk()
        self.cadastrar.title('Cadastro de Produtos')
        self.cadastrar['bg'] = '#3C626D'
        self.cadastrar.geometry('+300+150')

        Label(self.cadastrar,text='Cadastre os produtos', font=12, bg='#3C626D', fg='white').grid(row=0, column=0, columnspan=4, padx=56, pady=5)

        #CRIAR LABEL E ESPAÇÕ DE ENTRAR        
        Label(self.cadastrar, text='Nome', font=12, bg='#3C626D', fg='white').grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.nome = Entry(self.cadastrar, width=25)
        self.nome.grid(row=1, columnspan=2, column=1, pady=5, padx=5)

        #CRIAR LABEL E ESPAÇÕ DE ENTRAR
        Label(self.cadastrar, text='Ingredientes', font=12, bg='#3C626D', fg='white').grid(row=2, column=0, columnspan=1, padx=5, pady=5)
        self.ingredientes = Entry(self.cadastrar, width=25)
        self.ingredientes.grid(row=2, columnspan=2, column=1, pady=5, padx=5)
        
        #CRIAR LABEL E ESPAÇÕ DE ENTRAR
        Label(self.cadastrar, text='Grupo', font=12, bg='#3C626D', fg='white').grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self.grupo = Entry(self.cadastrar, width=25)
        self.grupo.grid(row=3, columnspan=2, column=1, pady=5, padx=5)

        #CRIAR LABEL E ESPAÇÕ DE ENTRAR
        Label(self.cadastrar, text='Preço', font=12, bg='#3C626D', fg='white').grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        self.preco = Entry(self.cadastrar, width=25)
        self.preco.grid(row=4, columnspan=2, column=1, pady=5, padx=5)

        #BOTAO CADASTRAR PRODUTOS
        Button(self.cadastrar, text='Cadastrar', command=self.CadastrarProdutosBackEnd, width=15,bg='gray',relief='flat',highlightcolor ='#165C37').grid(row=5, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Excluir',command=self.RemoverCadastrosBackEnd, width=15,bg='gray',relief='flat',highlightcolor ='#165C37').grid(row=5, column=1, padx=5, pady=5)
        Button(self.cadastrar, text='Atualizar',command=self.AtualizarProdutosBackEnd, width=15,bg='gray',relief='flat',highlightcolor ='#165C37').grid(row=6, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Limpar Produtos',command=self.LimpasCadastrosBackEnd,width=15,bg='gray',relief='flat',highlightcolor ='#165C37').grid(row=6, column=1, padx=5, pady=5)
        

        #CRIA A TREEVIEW
        self.tree = ttk.Treeview(self.cadastrar, height=18, 
        columns=("c1", "c2", "c3", "c4"), 
        show="headings")  


        self.tree.column("c1", width=150,minwidth=50, anchor="center", stretch=NO)
        self.tree.column("c2", width=230,minwidth=50, anchor="center", stretch=NO)
        self.tree.column("c3", width=100,minwidth=50, anchor="center", stretch=NO)
        self.tree.column("c4", width=70,minwidth=50, anchor="center", stretch=NO)
        self.tree.heading("c1", text="Nome")
        self.tree.heading("c2", text="Ingredientes")
        self.tree.heading("c3", text="Grupo")
        self.tree.heading("c4", text="Preço")
        #self.tree.pack() # 0 .pack MOSTRA TUDO ORGANIZADO, MAS VAMOS SEGUIR O CURSO USANDO O .grid
        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.MostrarProdutosBackEnd()

        self.cadastrar.mainloop()


    #CODIGO ABAIXO MOSTRA COMO VISUALISAR ARQUIVOS DO MYSQL DIRETAMENTE NUMA TREEVIEW
    def MostrarProdutosBackEnd(self):
        try:
            conexao = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db ="erp",
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM produtos')
                resultados = cursor.fetchall()
        except:
            print('Erro ao conectado ao banco de dados')

        self.tree.delete(*self.tree.get_children())

        linhav = []

        for linha in resultados:
            linhav.append(linha['nome'])
            linhav.append(linha['ingredientes'])
            linhav.append(linha['grupo'])
            linhav.append(linha['preco'])

            self.tree.insert("", END, values=linhav, iid=linha['id'], tag='1')

            linhav.clear()

    #CODIGO ABAIXO É PARA INSERIR OS PRODUTOS NA TABELA DO BANCO DE DADOS E MOSTRAR NA TREEVIE
    def CadastrarProdutosBackEnd(self):
        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        try:
            conexao = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db ="erp",
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into produtos(nome, ingredientes, grupo, preco) values(%s, %s, %s, %s)', (nome, ingredientes, grupo, preco))
                conexao.commit()
        except:
            print('Erro ao conectado ao banco de dados')
        
        self.MostrarProdutosBackEnd()

    #DELETAR PRODUTO SELECIONADO NA TREEVIEW
    def RemoverCadastrosBackEnd(self):

        idDeletar = int(self.tree.selection()[0])
    
        try:
            conexao = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db ="erp",
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('delete from produtos where id = {}'.format(idDeletar))
                conexao.commit()
        except:
            print('Erro ao conectado ao banco de dados')
        
        self.MostrarProdutosBackEnd()

        self.cadastrar.mainloop()

    #ATUALIZA A LISTA DE PRODUTOS
    def AtualizarProdutosBackEnd(self):
        try:
            conexao = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db ="erp",
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                conexao.commit()
        except:
            print('Erro ao conectado ao banco de dados')

        self.MostrarProdutosBackEnd()

        self.cadastrar.mainloop()

    #LIMPA TODOS OS REGISTROS DA TABELA PRODUTOS E NAO APAGA A TABELA
    def LimpasCadastrosBackEnd(self):
        if messagebox.askokcancel('Limpar Dados CUIDADO!!', 'Deseja excluir todos os dados da tabela?\nNAO HA VOLTA!'):
            try:
                conexao = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    db ="erp",
                    charset = 'utf8mb4',
                    cursorclass = pymysql.cursors.DictCursor
                )
            except:
                print('Erro ao conectar ao banco de dados')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('TRUNCATE TABLE produtos') #LIMPA TODOS OS REGISTROS DA TABELA PRODUTOS
                    conexao.commit()
            except:
                print('Erro ao conectado ao banco de dados')

            self.MostrarProdutosBackEnd()

    def __init__(self):
        self.root = Tk()
        self.root.title('MENU PRINCIPAL'.center(238))# Titulo do programa e adcionado o titulo no centro
        self.root.geometry('800x500+400+150') # Largura e altura 
        self.root.resizable(False, False)
        self.root['bg'] = '#153943'
        Label(self.root, text='MENU PRINCIAL', font='arial 20', bg='green',fg='white',  width=52).grid(row=0, column=0)
        sair = Button(self.root, text='Sair',command=exit, font='Arial 14', cursor='hand2', fg='white', bg='red', width=5)
        sair.place(x=725, y=450) 

        Button(self.root, text='Pedidos', width=25,font= 'arial 12', fg='#BEA503', bg='#292F88').grid(row=1, column=0, padx=10, pady=10)
        Button(self.root, text='Cadastros', width=25,font= 'arial 12',command=self.CadastrarProduto, fg='#BEA503', bg='#292F88').grid(row=2, column=0, padx=10, pady=10)


        self.root.mainloop()
     #CRIAR UMA JANELA DIFERENTE USANDO self E root
class Janelalogin(): #JANELA PRINCIPAL(JANELA DE LOGIN)
     #ESSA PARTE FAZ O BOTAO DE ENTRAR FAZER A VERIFICACAO SE O LOGIN 
     #ESTÁ CERTO OU ERRADO PRA DEPOIS ABRIR A PROXIMA JANELA

    def verificarLogin(self):
        autenticado = False
        usuarioMaster = False
        try:
            conexao = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db ="erp",
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao conectar ao banco de dados')

        usuario = self.login.get()
        senha = self.senha.get()
         
        try:
            with conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM cadastros')
                resultado = cursor.fetchall()
        except:
            print('Erro ao conectado ao banco de dados')
        for linha in resultado:
            if usuario == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
            else:
                autenticado = False
        if not autenticado:
            messagebox.showinfo('Login Erro', ' Email ou senha invalido')
        if autenticado:
            self.root.destroy()
            if usuarioMaster:
                AdminJanela()
                
    def cadastroBackEnd(self):
        codigoPadrao = '123'   # codigo padrao de acesso somente do ADM

        if self.CodigoSeguranca.get() == codigoPadrao:
            if len(self.login.get()) <= 20:
                if len(self.senha.get()) <= 50:
                    nome = self.login.get()
                    senha = self.senha.get()

                    try:
                        conexao = pymysql.connect(
                            host="localhost",
                            user="root",
                            password="",
                            db ="erp",
                            charset = "utf8mb4",
                            cursorclass = pymysql.cursors.DictCursor
                        )
                    except:
                       print('Erro ao conectar ao banco de dados')
                    
                    try:
                        with conexao.cursor as cursor:
                            cursor.execute('insert into cadastros(nome, senha, nivel) values(%s, %s, %s)', (nome, senha, 1))
                            conexao.commit()
                        messagebox.showinfo('Cadastro', 'Usuario cadastrado com sucesso!')
                        self.root.destroy()
                    except:
                        print('Erro ao inserir dados') # Este aqui é o correto
                        messagebox.showinfo('ERRO','Erro ao inserir dados')  # este foi adicionado        
                else:
                    messagebox.showinfo('ERRO','Por favor insira uma senha com 20 ou menos caracteres')
            else:
                 messagebox.showinfo('ERRO','Por favor insira um nome com 50 ou menos caracteres')
        else:
            messagebox.showinfo('ERRO','Erro no codigo de segurança, tente novamente')

    def cadastros (self):
        Label(self.root, text='Chave de segurança', font=12).grid(row=3, column=0, padx=5, pady=5)
        self.CodigoSeguranca = Entry(self.root, show='*', font=12)
        self.CodigoSeguranca.grid(row=3, column=1, padx=5, pady=10)
        Button(self.root, text='Confirmar Cadastro',command=self.cadastroBackEnd, font=12, width=15, bg='blue',fg='white', cursor='hand2').grid(row=4, column=0,columnspan=3, pady=5, padx=10)
           
    def UpdateBackEnd(self):
        try:
            conexao = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db ="erp",
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao conectar ao banco de dados')
         
        try:
            with conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM cadastros')
                resultado = cursor.fetchall()
        except:
            print('Erro ao conectado ao banco de dados')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultado:
            linhaV.append(linha['id'])
            linhaV.append(linha['nome'])
            linhaV.append(linha['senha'])
            linhaV.append(linha['nivel'])

            self.tree.insert("", END, values= linhaV, iid= linha['id'], tags='1')

            linhaV.clear()

    #TREEVIWE PARA VISUALIZAR CADASTROS
    def visualzarCadastros(self):
        self.vc = Toplevel()
        self.vc.geometry('+400+200')
        self.vc.resizable(True, True)
        self.vc.title('Visualizar Cadastros')

        #CRIA A TREEVIEW
        self.tree = ttk.Treeview(self.vc, height=18, 
        columns=("c1", "c2", "c3", "c4"), 
        show="headings")  


        self.tree.column("c1", width=50,minwidth=50, anchor="center", stretch=NO)
        self.tree.column("c2", width=250,minwidth=50, anchor="center", stretch=NO)
        self.tree.column("c3", width=200,minwidth=50, anchor="center", stretch=NO)
        self.tree.column("c4", width=200,minwidth=50, anchor="center", stretch=NO)
        self.tree.heading("c1", text="ID")
        self.tree.heading("c2", text="Usuario")
        self.tree.heading("c3", text="Senha")
        self.tree.heading("c4", text="Nivel")
        #self.tree.pack() # 0 .pack MOSTRA TUDO ORGANIZADO, MAS VAMOS SEGUIR O CURSO USANDO O .grid
        self.tree.grid(row=0, column=0, padx=5, pady=5)


        self.UpdateBackEnd() #chamar essa DEF para que seja exibido as informações dentro da TREVIEW

        self.vc.mainloop()

    #GRAFICOS  E BOTOES DO BANCO DE DADOS
    def __init__(self):
        self.root = Tk()
        self.root.geometry('+635+300')
        self.root['bg'] = '#3C626D'
        self.root.title('PYTHON E MYSQL')# Titulo do programa e adcionado o titulo no centro
        self.root.resizable(False, False) # Aqui ninguem pode alterar a largura e nem a altura
        Label(self.root,text='Faça o Login', font='arial 18', bg='green',fg='white', width=30).grid(row=0, column=0, columnspan=2)

        Label(self.root,text='Digite seu Usuario:', font=12, bg='#3C626D', fg='white').grid(row=1, column=0)

        Label(self.root,text='Digite sua senha:', font=12,bg='#3C626D', fg='white').grid(row=2, column=0)

        self.login = Entry(self.root, font=12)
        self.login.grid(row=1, column=1, padx=5, pady=5)
        
        self.senha = Entry(self.root, font=12, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Button(self.root, text='Entrar', command=self.verificarLogin, font='Arial 14', cursor='hand2', fg='white', bg='green').grid(row=5, column=0, pady=5, padx=5)

        botaoCadastrados = Button(self.root, text='Visualizar Cadastros',command=self.visualzarCadastros, font='Arial 14', cursor='hand2', fg='white', bg='blue')
        botaoCadastrados.grid(row=6, column=1, padx=5, pady=5)
        
        btcadastro = Button(self.root, text='Cadastrar',command=self.cadastros, font='Arial 14', cursor='hand2', fg='white', bg='orange')
        btcadastro.grid(row=5, column=1, padx=5, pady=5)


        botaoCsair = Button(self.root, text='Sair',command=exit, font='Arial 14', cursor='hand2', fg='white', bg='red', width=5)
        botaoCsair.grid(row=6,column=0,columnspan=1, pady=5, padx=5)
        

        self.root.mainloop()

Janelalogin()


