from tkinter import *
import sqlite3
con = sqlite3.connect("coffee.db")
cur=con.cursor()
from datetime import date
# fenêtre principale



def Facturation(Items,Total,Master,name):
 fenetre = Toplevel(Master)
 today = date.today()  
 fenetre.title('Cafe BSB')

 
 fenetre.user_name_label = Label(fenetre, text=name, relief="groove",font='Times 16 bold',bg='#FAE9E9')
 fenetre.user_name_label.place(x=1, y=1)
 fenetre.user_name_label = Label(fenetre, text=str(today.strftime("%m.%d.%Y")),relief="groove", font='Times 16 bold',bg='#FAE9E9')
 fenetre.user_name_label.place(x=350, y=1)
 fenetre.user_name_label = Label(fenetre, text='Facture', relief="groove",font='Times 16 bold',bg='#FAE9E9')
 fenetre.user_name_label.place(x=180, y=80)
# libellé
 
 x=0
 pas = 50
 y=180
 
 for i in Items.keys():
     quan = Items[i]
     prix = cur.execute("SELECT prix FROM items where nom =" + "'"+ i +"'").fetchall()[0][0]
     itemNom = cur.execute("SELECT Item_Nom FROM items where nom =" + "'"+ i +"'").fetchall()[0][0]
     fenetre.item_label = Label(fenetre, text="x" +str(Items[i])+"      " +  itemNom    +": " + str(prix*quan) + "dh",relief="groove", font='Times 16 bold',bg='#FAE9E9')
     fenetre.item_label.place(x=115, y=y+x)
     x=x+pas
  
 fenetre.Total_label = Label(fenetre, text='Total: ' + str(Total), relief="groove",font='Times 20 bold',bg='#FAE9E9')
 fenetre.Total_label.place(x=300, y=400)
 fenetre.merci_label = Label(fenetre, text='nous vous attendons a nouveau', relief="groove",font='Times 12 bold',bg='#FAE9E9')
 fenetre.merci_label.place(x=120, y=500)

 fenetre.geometry("450x550+350+200")
 fenetre.mainloop()