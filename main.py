from tkinter import *
from tkinter import messagebox
import sqlite3
from createUser import *
from client import *
from serveur import *
from menu import *

con = sqlite3.connect("coffee.db")
cur=con.cursor()

fenetre = Tk()
fenetre.title('Cafe BSB')


def authServeur(fenetre,Username,Password):
    all_users = cur.execute("SELECT * FROM admin").fetchall()
    found=0
    for user in all_users:
        if user[2]==Username and user[3] == Password:
                  found = 1
                  messagebox.showinfo("Success", "Login: " + Username + " Sucess")
                  name = user[1]
                  Serveur(fenetre)
                  
                  
                  
                   
    if found == 0:
        messagebox.showinfo("Error", "Logins: " + Username + " N'existe pas ou mot de passe erronÃ©e")   
    return
    



def Login(fenetre,Username,Password):
    all_users = cur.execute("SELECT * FROM users").fetchall()
    found=0
    for user in all_users:
        if user[2]==Username and user[3] == Password:
                  found = 1
                  messagebox.showinfo("Success", "Login: " + Username + " Success")
                  name = user[1]
                  #Menu(fenetre)
                  Client(name,fenetre)
                  
                  
                   
    if found == 0:
        messagebox.showinfo("Error", "Logins: " + Username + " N'existe pas ou mot de passe erronÃ©e")   
    return          

            
   
 

    # create and locate background and icon :
fenetre.background = PhotoImage(file='backgrounds/login.png')
fenetre.background_label = Label(fenetre, image=fenetre.background)
fenetre.background_label.pack()

fenetre.icon = PhotoImage(file='icons/login.png')
fenetre.login_icon = Label(fenetre, image=fenetre.icon,relief="groove", bg='#A83B23')
fenetre.login_icon.place(x=300, y=25)

    # create user name entry and label and locate them on the app .
fenetre.user_name_label = Label(fenetre, text='Username:', font='Times 16 bold',relief="groove", bg='#A83B23',fg='#FAE9E9')
fenetre.user_name_label.place(x=20, y=100)
fenetre.user_name_entry = Entry(fenetre, width=60, bd=5)
fenetre.user_name_entry.insert(0, "")
fenetre.user_name_entry.place(x=160, y=103)

    # create password entry and label and locate it on the app .
fenetre.password_label = Label(fenetre, text='Password :', font='Times 16 bold', relief="groove",bg ='#A83B23',fg='#FAE9E9')
fenetre.password_label.place(x=20, y=140)
fenetre.password_entry = Entry(fenetre, width=60, bd=5, show= '*')
fenetre.password_entry.insert(0, "")
fenetre.password_entry.place(x=160, y=143)

    # create login button and place it on the app .
fenetre.login_button = Button(fenetre, text='Login',fg='#FAE9E9', width=30, height=1, bg ='#A83B23',font='Times 12 bold', bd=5,command=lambda: Login(fenetre,fenetre.user_name_entry.get(),fenetre.password_entry.get()))
fenetre.login_button.place(x=190, y=200)

    # create a button to add a new user to the system , the button will user 'create_user' function calling other class.
fenetre.new_user_button = Button(fenetre, text='Creer compte Serveur',fg='#FAE9E9', bg ='#A83B23',width=30, height=1, font='Times 12 bold', bd=5,command=lambda: CreateUser(fenetre))
fenetre.new_user_button.place(x=190, y=240)

    # create help button to reset password/user name .
fenetre.help_button = Button(fenetre, text='Gestion Serveur',fg='#FAE9E9', width=30,bg='#F39C12', height=1, font='Times 12 bold',bd=5, command=lambda: authServeur(fenetre,fenetre.user_name_entry.get(),fenetre.password_entry.get()))
fenetre.help_button.place(x=190, y=280)


fenetre.geometry("650x550+350+90")
fenetre.mainloop()




