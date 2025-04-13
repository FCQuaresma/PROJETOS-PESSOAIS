from tkinter import *

raiz = Tk()

def meuClique():
    meuRotulo = Label(raiz, text='Olha só! Cliquei em um botao !')
    meuRotulo.pack()

meuBotao = Button(raiz, text='Clique aqui!', command=meuClique, fg="red", bg="yellow")
meuBotao.pack()


raiz.mainloop()