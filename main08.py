from tkinter import *
from tkinter import Tk,ttk
from Statics.Colors import *
# from PIL import Image, ImageTk

################# janela ###############

class AppMain(Tk):
    def __init__(self):
        super().__init__()

        self.title('')
        self.geometry('1240x800')
        # self.iconbitmap('.\Statics\logoO.bmp')
        self.configure(bg=co9)
        self.resizable(False,False)
        self.Style = ttk.Style(self)
        self.Style.theme_use('clam')

################# FRAMES ###############
        self.Frame_Cima = Frame(self)
        self.Frame_Cima['width'] = 1240
        self.Frame_Cima['height'] = 50
        self.Frame_Cima['bg'] = co2
        self.Frame_Cima['relief'] = 'flat'
        self.Frame_Cima.grid(row=0, column=0)

        self.Frame_Meio = Frame(self)
        self.Frame_Meio['width'] = 1240
        self.Frame_Meio['height'] = 303
        self.Frame_Meio['bg'] = co3
        self.Frame_Meio['pady'] = 20
        self.Frame_Meio['relief'] = 'flat'
        self.Frame_Meio.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)

        self.Frame_Baixo = Frame(self)
        self.Frame_Baixo['width'] = 1240
        self.Frame_Baixo['height'] = 300
        self.Frame_Baixo['bg'] = co4
        self.Frame_Baixo['relief'] = 'flat'
        self.Frame_Baixo.grid(row=2, column=0, padx=1, pady=0, sticky=NSEW)


################# FRAME MEIO  ###############



################# IMAGEM ###############

# app_img = Image.open('inv.png')
# app_img = app_img.resize((45,45))
# app_img = ImageTk.PhotoImage(app_img)

# app_logo = Label(frame_cima, image=app_img, text="Formu", width=1240, compound=LEFT,relief=RAISED, anchor=NW,font=('Verdana 20 bold'),bg=co1,fg=co4)
# app_logo.place(x=0,y=0) 

################# ENTRADAS DE DADOS  ###############

# l_nome = Label(frame_Meio,text='nome * ', height=1, anchor=NW,font=('Ivy 15 bold'), bg=co1, fg=co4)
# l_nome.grid(row=10, column=0, padx=180, pady=0,sticky=NSEW)
# e_nome= Entry(frame_Meio, width=30, justify='left', relief=SOLID)
# e_nome.grid(row=2, column=0, padx=1, pady=0,sticky=NSEW)


# l_nomea = Label(frame_Meio,text='nome * ', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
# l_nomea.place(x=10, y= 180)
# e_nomea= Entry(frame_Meio, width=30, justify='left', relief=SOLID)
# e_nomea.place(x=530,y=11)

if __name__ == '__main__':
    root = AppMain()
    root.mainloop()