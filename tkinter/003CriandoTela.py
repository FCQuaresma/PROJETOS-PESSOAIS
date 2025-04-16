import tkinter as tk
from tkinter import messagebox

# Função chamada ao clicar no botão "Entrar"
def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario == 'Felipe' and senha == '123456':
        messagebox.showinfo("Login", "Bem-vindo ao mundo da trilha da Programação do Felipe Quaresma!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Criação da janela
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")

# Widgets
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.pack(pady=(10, 0))

entry_usuario = tk.Entry(janela)
entry_usuario.pack()

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=(10, 0))

entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

salvar_login = tk.IntVar()
check_salvar = tk.Checkbutton(janela, text="Salvar o login?", variable=salvar_login)
check_salvar.pack(pady=(10, 0))

btn_entrar = tk.Button(janela, text="Entrar", command=login)
btn_entrar.pack(pady=10)

# Loop da janela
janela.mainloop()