from tkinter import *
from tkinter import Tk,ttk,messagebox
import sqlite3 as sql
from Statics.Colors import *

con = sql.connect('Form.db')

################# Screen ###############

class AppLogin(Tk):
    def __init__(self):
        super().__init__()

        self.title('')
        # self.geometry = 'tamanho da tela'
        # self.iconbitmap('.\Statics\logo.ico')
        self.configure(bg=co9)
        self.resizable(False,False)
        self.Style = ttk.Style(self)
        self.Style.theme_use('clam')

        self.LoginLabel = Label(self)
        self.LoginLabel['text'] = 'Login:'
        self.LoginLabel.grid(row=0,column=0)

        self.LoginEntry = Entry(self)
        self.LoginEntry['width'] = 20
        self.LoginEntry.grid(row=0,column=1,padx=5)

        self.PasswordLabel = Label(self)
        self.PasswordLabel['text'] = 'Senha:'
        self.PasswordLabel.grid(row=1,column=0,pady=5)

        self.PasswordEntry = Entry(self)
        self.PasswordEntry['width'] = 20
        self.PasswordEntry.grid(row=1,column=1,padx=5,pady=5)

        self.LoginBtt = Button(self)
        self.LoginBtt['text'] = 'Login'
        self.LoginBtt['command'] = self.Login
        self.LoginBtt.grid(row=2,column=0,pady=5,padx=20)

        self.CadastroBtt = Button(self)
        self.CadastroBtt['text'] = 'Cadastrar'
        self.CadastroBtt['command'] = self.Cadastro
        self.CadastroBtt.grid(row=2,column=1,pady=5,padx=20)

    def Login(self):
        nome = self.LoginEntry.get()
        senha = self.PasswordEntry.get()

        cur = con.cursor()
        cur.execute('''SELECT * FROM usuarios WHERE nome = ? AND senha = ?''', (nome, senha))
        resultado = cur.fetchone()

        if resultado is not None:
            print('Login realizado com sucesso!')
            from main08 import AppMain
            root0 = AppMain()
            root0.mainloop()
        else:
            print('Nome de usuário ou senha incorretos.')
    
    def Cadastro(self):
        if __name__ == '__main__':
            root0 = AppCad()
            root0.mainloop()


class AppCad(Tk):
    def __init__(self):
        super().__init__()

        self.title('Cadastro')
        # self.geometry = 'tamanho da tela'
        # self.iconbitmap('.\Statics\logo.ico')
        self.configure(bg=co9)
        self.resizable(False,False)
        self.Style = ttk.Style(self)
        self.Style.theme_use('clam')

        self.LoginLabel = Label(self)
        self.LoginLabel['text'] = 'Login:'
        self.LoginLabel.grid(row=0,column=0)

        self.LoginEntry = Entry(self)
        self.LoginEntry['width'] = 20
        self.LoginEntry.grid(row=0,column=1,padx=5)

        self.PasswordLabel = Label(self)
        self.PasswordLabel['text'] = 'Senha:'
        self.PasswordLabel.grid(row=1,column=0,pady=5)

        self.PasswordEntry = Entry(self)
        self.PasswordEntry['width'] = 20
        self.PasswordEntry.grid(row=1,column=1,padx=5,pady=5)

        self.LoginBtt = Button(self)
        self.LoginBtt['text'] = 'Voltar'
        self.LoginBtt['command'] = self.Voltar
        self.LoginBtt.grid(row=2,column=0,pady=5,padx=20)

        self.CadastroBtt = Button(self)
        self.CadastroBtt['text'] = 'Salvar'
        self.CadastroBtt['command'] = self.Salvar
        self.CadastroBtt.grid(row=2,column=1,pady=5,padx=20)

    def Voltar(self):
        self.destroy()

    def Salvar(self):
        nome = self.LoginEntry.get()
        senha = self.PasswordEntry.get()

        cur = con.cursor()
        cur.execute('''INSERT INTO usuarios (nome, senha) VALUES (?, ?)''', (nome, senha))
        con.commit()

        messagebox.showinfo("Cadastro", "Cadastro efetuado com sucesso.")
        self.destroy()

if __name__ == '__main__':
    root = AppLogin()
    root.mainloop()

con.close()