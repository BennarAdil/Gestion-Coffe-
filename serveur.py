from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox





def Serveur(Master):
 root = Toplevel(Master)
 root.title('Gestion Serveur')
 root.geometry("880x500")
 
 style = ttk.Style()
 
# Pick A Theme
 style.theme_use('default')

# Configure the Treeview Colors
 style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
 style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
 tree_frame = Frame(root)
 tree_frame.pack(side = TOP,padx=20,pady=10,anchor=NW)

# Create a Treeview Scrollbar
 tree_scroll = Scrollbar(tree_frame)
 tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
 my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
 my_tree.pack()

# Configure the Scrollbar
 tree_scroll.config(command=my_tree.yview)

# Define Our Columns
 my_tree['columns'] = ("Nom", "Prenom", "Adresse", "Horaire","ID")

# Format Our Columns
 my_tree.column("#0", width=0, stretch=NO)
 my_tree.column("Nom", anchor=W, width=140)
 my_tree.column("Prenom", anchor=W, width=140)

 my_tree.column("Adresse", anchor=CENTER, width=140)
 my_tree.column("Horaire", anchor=CENTER, width=140)

 my_tree.column('ID', stretch=NO, minwidth=0, width=0)

# Create Headings
 my_tree.heading("#0", text="", anchor=W)
 my_tree.heading("Nom", text="Nom", anchor=W)
 my_tree.heading("Prenom", text="Prenom", anchor=W)

 my_tree.heading("Adresse", text="Adresse", anchor=CENTER)
 my_tree.heading("Horaire", text="Horaire", anchor=CENTER)



# Create Striped Row Tags
 my_tree.tag_configure('oddrow', background="white")
 my_tree.tag_configure('evenrow', background="lightblue")




 search_frame = LabelFrame(root, text="Cherche Serveur", font='Times 15 bold')
 search_frame.place(x=600,y=10)
 search_entry = Entry(search_frame,bd=5)
 search_entry.grid(row=0, column=0, padx=10, pady=10)

 

 dropdown=ttk.Combobox(search_frame,state='readonly', width = 12,font=("Helvetica",12))
 dropdown['values']=("Id", "Nom", "Prenom", "Horaire", "Adresse")
 dropdown.grid(row=1, column=0, padx=10, pady=10)
 searchBtn=Button(search_frame,text="Search",fg='#FAE9E9',font='Times 9 bold', bg='#641E16',bd=6 ,width=10,command=lambda: Chercher(search_entry,dropdown,my_tree))
 searchBtn.grid(row=0, column=3, padx=10, pady=10)
 ResetBtn=Button(search_frame,text="Reset",fg='#FAE9E9',font='Times 9 bold', bg='#641E16',bd=6 ,width=10,command=lambda: Reset(my_tree))
 ResetBtn.grid(row=1, column=3, padx=10, pady=10)


# Add Record Entry Boxes
 data_frame = LabelFrame(root, text="Formulaire Serveur",font='Times 15 bold')
 data_frame.pack(fill="x", expand="yes",padx=20)



 fn_label = Label(data_frame, text="Nom",font='Times 12 bold')
 fn_label.grid(row=0, column=0, padx=10, pady=10)
 fn_entry = Entry(data_frame,bd=5)
 fn_entry.grid(row=0, column=1, padx=10, pady=10)

 ln_label = Label(data_frame, text="Prenom",font='Times 12 bold')
 ln_label.grid(row=0, column=2, padx=10, pady=10)
 ln_entry = Entry(data_frame,bd=5)
 ln_entry.grid(row=0, column=3, padx=10, pady=10)



 address_label = Label(data_frame, text="Address",font='Times 12 bold')
 address_label.grid(row=1, column=0, padx=10, pady=10)
 address_entry = Entry(data_frame,bd=5)
 address_entry.grid(row=1, column=1, padx=10, pady=10)

 city_label = Label(data_frame, text="Horaire",font='Times 12 bold')
 city_label.grid(row=1, column=2, padx=10, pady=10)
 city_entry = Entry(data_frame,bd=5)
 city_entry.grid(row=1, column=3, padx=10, pady=10)
 

 
 button_frame = LabelFrame(root, text="Gerer Serveur",font='Times 15 bold')
 button_frame.pack(fill="x", expand="yes", padx=20)

 update_button = Button(button_frame, text="Ajouter", command=lambda: Ajouter(my_tree,fn_entry,ln_entry,address_entry,city_entry),fg='#FAE9E9',font='Times 9 bold', bg='#641E16',bd=6 ,width=10)
 update_button.grid(row=0, column=0, padx=10, pady=10)

 add_button = Button(button_frame, text="Modifier", command=lambda: Modifier(my_tree,fn_entry,ln_entry,address_entry,city_entry),fg='#FAE9E9',font='Times 9 bold', bg='#641E16',bd=6 ,width=10)
 add_button.grid(row=0, column=1, padx=10, pady=10)

 remove_all_button = Button(button_frame, text="Supprimer", command=lambda: Supprimer(my_tree),fg='#FAE9E9',font='Times 9 bold', bg='#641E16',bd=6 ,width=10)
 remove_all_button.grid(row=0, column=2, padx=10, pady=10)
 
 query_database(my_tree)
 root.mainloop()


def Reset(my_tree):
     my_tree.delete(*my_tree.get_children())
     query_database(my_tree)


def Chercher(search_entry,dropdown,my_tree):
     search_term = search_entry.get()
     search_type = dropdown.get()
     query= ""
     if search_entry and search_type:
          conn = sqlite3.connect('coffee.db')
          cur = conn.cursor()
          query= "SELECT * FROM servers WHERE " +  search_type + "=?"
          cur.execute(query,(search_term,))
          records = cur.fetchall()
          if records:
             my_tree.delete(*my_tree.get_children())
             for record in records:
      
                 my_tree.insert(parent='', index='end', text='', values=(record[1],record[2], record[3], record[4],record[0]), tags=('evenrow'))
                 my_tree.tag_configure(tagname='evenrow', background='#E6B0AA')
             
 
                      		   
		   
	 


			
			
def query_database(my_tree):
	# Create a database or connect to one that exists
    
    conn = sqlite3.connect('coffee.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM servers")
    records = cur.fetchall()
	
	# Add our data to the screen
    

	#for record in records:
	#	print(record)
	
    for record in records:
      
            my_tree.insert(parent='', index='end', text='', values=(record[1],record[2], record[3], record[4],record[0]), tags=('evenrow'))
            my_tree.tag_configure(tagname='evenrow', background='#E6B0AA')
            
       
		

	

	# Close our connection

	




def Ajouter(my_tree,fn_entry,ln_entry,address_entry,city_entry):
 conn = sqlite3.connect('coffee.db')
 cur = conn.cursor()
 nom = fn_entry.get()
 prenom = ln_entry.get()
 add = address_entry.get()
 city = city_entry.get()
 cur.execute("SELECT Id FROM servers ORDER BY ID DESC LIMIT 1")
 last_id = cur.fetchall()[0][0] + 1
 print(last_id)
 if nom != "" and prenom !="" and add != "" and city != "":
   query = "INSERT INTO servers(id,Nom,Prenom,Adresse,horaire) VALUES(?,?,?,?,?)"
   cur.execute(query,(last_id,nom,prenom,add,city)) 
   conn.commit()
   messagebox.showinfo("Success","Le serveur est bien Ajouter")  
		 
  
 my_tree.insert(parent='', index='end', text='', values=(nom,prenom,add,city,last_id), tags=('evenrow',))

def Supprimer(my_tree):
    conn = sqlite3.connect('coffee.db')
    cur = conn.cursor()
    id= my_tree.item(my_tree.focus())['values'][4]
    query="DELETE FROM servers where id=" + str(id)
    print(query)	
    cur.execute(query,())
    conn.commit()
    selected_item = my_tree.selection() ## get selected item
    my_tree.delete(selected_item)
    messagebox.showinfo("Success","Le serveur est bien Supprimer")  
	
	#cur.execute()

	


def Modifier(my_tree,fn_entry,ln_entry,address_entry,city_entry):
    conn = sqlite3.connect('coffee.db')
    cur = conn.cursor()
    selected_item = my_tree.selection()
    nom = fn_entry.get()
    prenom = ln_entry.get()
    add = address_entry.get()
    horaire = city_entry.get()
    name=my_tree.item(my_tree.focus())['values'][0]
    last_name= my_tree.item(my_tree.focus())['values'][1] 
    adresse=my_tree.item(my_tree.focus())['values'][2]
    hor= my_tree.item(my_tree.focus())['values'][3] 
    id= my_tree.item(my_tree.focus())['values'][4]
    print(my_tree.item(my_tree.focus())['values'])
	#query="UPDATE servers set nom=?,prenom=?,adresse=?,ville=? where nom=? and prenom=?"
    query="UPDATE servers set id = " + str(id) 
    if nom : 
         query += ",nom=" + "'" + nom+"'"
    else:
         nom = name    
    if prenom :   
         query += ",prenom=" + "'" + prenom+"'"
    else :
         prenom=last_name    
    if add:    
        query += ",adresse=" + "'" + add+"'"
    else:
         add=adresse     
    if horaire:    
         query += ",Horaire=" + "'" + horaire+"'"
			 
    else:
         horaire= hor   
    query += " where id="+str(id) 
    print(query)  
    cur.execute(query)
    conn.commit()
    my_tree.item(selected_item, text="blub", values=(nom,prenom,add,horaire,id))
    messagebox.showinfo("Success","Le serveur est bien Modifier")  

# Add Buttons







