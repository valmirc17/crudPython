from tkinter import *
from tkinter import messagebox
import subprocess

# Funções
def Sair() :
    resposta = messagebox.askquestion("Sair do sistema?","Você tem certeza que deseja sair?")
    if resposta == 'yes':
        tela.destroy()

def validar_acesso(usuario, senha) :
    if usuario == 'admin' and senha == '123' :
        abrir_app()
    
    else:
        messagebox.showerror("Erro de login","Usuário ou senha incorretos.")
def abrir_app() :
    tela.destroy()
    subprocess.run(["python","AulaCrud.py"])

def click_botao():
    usuario = txt_usuario.get()
    senha = txt_senha.get()
    validar_acesso(usuario,senha)    
    
# Configuração da janela
janela = Tk()
janela.title("Login")

largura_janela = 400
altura_janela = 250

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

fonte = ("Arial", 12)

# Frame para centralizar os itens na tela
tela = Frame(janela)
tela.pack(expand=True, padx=20, pady=20)

# Componentes da tela
lbl_usuario = Label(tela, text='Usuario:', font=fonte)
lbl_usuario.grid(row=0, column=0)
txt_usuario = Entry(tela)
txt_usuario.grid(row=0, column=1, pady=5)

lbl_senha = Label(tela, text='Senha:', font=fonte)
lbl_senha.grid(row=1, column=0)
txt_senha = Entry(tela)
txt_senha.grid(row=1, column=1, pady=5)

# Botões
btn_entrar = Button(tela, text='Entrar', font=fonte, command=click_botao)
btn_entrar.grid(row=2, column=0, pady=5, padx=5)
btn_sair = Button(tela, text='Sair', font=fonte, command=Sair)
btn_sair.grid(row=2, column=1, pady=5, padx=5)

tela.mainloop()