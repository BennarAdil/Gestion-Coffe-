from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
import string
import random
root =Tk()
root.title("Edit Student")
root.title('Gestion Serveur')
root.geometry("1140x500")

root.background = PhotoImage(file='backgrounds/back.png')
root.background_label = Label(root, image=root.background)
root.background_label.pack()

root.refresh_button = Button(root, text='Gestion des Serveur',fg='white',font='Times 15 bold', bg='#7B241C',bd=6, height=5, width=25)
root.refresh_button.place(x=80, y=150)


root.mainloop()