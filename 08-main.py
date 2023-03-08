from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# janela ###############

janela = Tk()
janela.title('')
janela.geometry('1240x800')
janela.iconbitmap("logo.ico")
janela.configure(background=co9)
janela.resizable(False,False)
style = ttk.Style(janela)
style.theme_use("clam")

################# FRAMES ###############

frame_cima = Frame(janela, width=1240, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0)

frame_Meio = Frame(janela, width=1240, height=303, bg=co1,pady=20, relief="flat")
frame_Meio.grid(row=1, column=0, padx=1, pady=0,sticky=NSEW)

frame_Baixo = Frame(janela, width=1240, height=300, bg=co1, relief="flat")
frame_Baixo.grid(row=2, column=0, padx=1, pady=0,sticky=NSEW)

################# FRAME MEIO  ###############



################# IMAGEM ###############
app_img = Image.open('inv.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, text="Formu", width=1240, compound=LEFT,relief=RAISED, anchor=NW,font=('Verdana 20 bold'),bg=co1,fg=co4)
app_logo.place(x=0,y=0) 

################# ENTRADAS DE DADOS  ###############

# l_nome = Label(frame_Meio,text='nome * ', height=1, anchor=NW,font=('Ivy 15 bold'), bg=co1, fg=co4)
# l_nome.grid(row=10, column=0, padx=180, pady=0,sticky=NSEW)
# e_nome= Entry(frame_Meio, width=30, justify='left', relief=SOLID)
# e_nome.grid(row=2, column=0, padx=1, pady=0,sticky=NSEW)


# l_nomea = Label(frame_Meio,text='nome * ', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
# l_nomea.place(x=10, y= 180)
# e_nomea= Entry(frame_Meio, width=30, justify='left', relief=SOLID)
# e_nomea.place(x=530,y=11)

janela.mainloop()


