from tkinter import *
import tkinter as tk
import pymongo

def Salvar() :
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    cpf = txt_cpf.get()
    
    txt_codigo.delete(0,tk.END)
    txt_nome.delete(0,tk.END)
    txt_idade.delete(0,tk.END)
    txt_cpf.delete(0,tk.END)

    cliente = {"codigo": codigo, "nome": nome, "idade": idade, "cpf": cpf}
    collection.insert_one(cliente)

def Alterar() :
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    cpf = txt_cpf.get()
    
    cliente = {"codigo": codigo, "nome": nome, "idade": idade, "cpf": cpf}
    collection.update_one({"codigo":codigo},{"$set":cliente})
    
def Excluir() :
    codigo = txt_codigo.get()
    collection.delete_one({"codigo":codigo})
    
def Consultar() :
    codigo = txt_codigo.get()
    resultado = collection.find_one({"codigo":codigo})
    
    if resultado :
        txt_nome.insert(END, f"{resultado['nome']}\n")
        txt_idade.insert(END, f"{resultado['idade']}\n")
        txt_cpf.insert(END, f"{resultado['cpf']}\n")
    else :
        lbl_resultado.config(text="Nenhum resultado encontrado!")

# Configuração da janela
janela = Tk()
janela.title("Cadastro de clientes")

largura_janela = 600
altura_janela = 400

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

fonte = ("Arial", 12)

# Frame para centralizar os itens na tela
tela = Frame(janela)
tela.pack(expand=True, padx=20, pady=20)

# Conexão com o BD
banco = pymongo.MongoClient("mongodb://localhost:27017/")
db = banco["banco"]
collection = db["clientes"]

# Componentes da tela

Label(tela, text="Cadastro de clientes", font=("Arial", 18)).grid(row=0, columnspan=2, pady=10)

lbl_codigo = Label(tela, text='Código:', font=fonte)
lbl_codigo.grid(row=1, column=0)
txt_codigo = Entry(tela)
txt_codigo.grid(row=1, column=1, pady=5)

lbl_nome = Label(tela, text='Nome:', font=fonte)
lbl_nome.grid(row=2, column=0)
txt_nome = Entry(tela)
txt_nome.grid(row=2, column=1, pady=5)

lbl_idade = Label(tela, text='Idade:', font=fonte)
lbl_idade.grid(row=3, column=0)
txt_idade = Entry(tela)
txt_idade.grid(row=3, column=1, pady=5)

lbl_cpf = Label(tela, text='CPF:', font=fonte)
lbl_cpf.grid(row=4, column=0)
txt_cpf = Entry(tela)
txt_cpf.grid(row=4, column=1, pady=5)

# Botões
btn_salvar = Button(tela, text='Salvar', font=fonte, command=Salvar)
btn_salvar.grid(row=5, column=0, pady=5, padx=5)

btn_alterar = Button(tela, text='Alterar', font=fonte, command=Alterar)
btn_alterar.grid(row=5, column=1, pady=5, padx=5)

btn_excluir = Button(tela, text='Excluir', font=fonte, command=Excluir)
btn_excluir.grid(row=6, column=0, pady=5, padx=5)

btn_consultar = Button(tela, text='Consultar', font=fonte, command=Consultar)
btn_consultar.grid(row=6, column=1, pady=5, padx=5)

btn_sair = Button(tela, text='Sair', font=fonte, command=janela.quit)
btn_sair.grid(row=7, column=0, pady=5, padx=5)

lbl_resultado = Label(tela, text='', font=fonte)

janela.mainloop()
