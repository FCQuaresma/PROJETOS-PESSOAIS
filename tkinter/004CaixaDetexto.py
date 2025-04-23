from tkinter import *

raiz = Tk()

e = Entry(raiz, width=50)
e.pack()
e.insert(0, "Digite seu nome aqui: ")

def meuClique():
    ola = "olá " + e.get()
    meuRotulo = Label(raiz, text  = ola)
    meuRotulo.pack()

myBotao = Button(raiz, text = 'Coloque seu nome', command = meuClique)
myBotao.pack()

raiz.mainloop()
