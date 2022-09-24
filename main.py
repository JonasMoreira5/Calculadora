from tkinter import *
from tkinter import ttk

# Cores
cor1 = "#064d85" # Azul escuro
cor2 = "#21130d" # Preta 
cor3 = "#38576b" # Azul carregado
cor4 = "#ECEFF1" # Cizenta
cor5 = "#FFAB40" # Laranja
cor6 = "#feffff" # branca

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(background=cor2)

# Criação dos frames
frame_tela = Frame(janela, width=235, height=50,background=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, background=cor4)
frame_corpo.grid(row=1, column=0)

# Criação dos botões
# Linha 1
b_1 = Button(frame_corpo, text="C", width=8, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, text="/", width=3, height=2,background=cor5, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

# Linha 2
b_4 = Button(frame_corpo, text="7", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo, text="8", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_corpo, text="9", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, text="*", width=3, height=2,background=cor5, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

# linha 3
b_8 = Button(frame_corpo, text="4", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=100)

b_9 = Button(frame_corpo, text="5", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=100)

b_10 = Button(frame_corpo, text="6", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=100)

b_11 = Button(frame_corpo, text="-", width=3, height=2,background=cor5, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=100)

# linha 4
b_12 = Button(frame_corpo, text="1", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo, text="2", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_corpo, text="3", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_corpo, text="+", width=3, height=2,background=cor5, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

# linha 5
b_16 = Button(frame_corpo, text="0", width=8, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=210)

b_17 = Button(frame_corpo, text=".", width=3, height=2,background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=210)

b_18 = Button(frame_corpo, text="=", width=3, height=2,background=cor5, fg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=210)



janela.mainloop()
