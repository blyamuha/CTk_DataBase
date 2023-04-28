import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
import customtkinter
import customtkinter as CTk
import sqlite3

font1=('Polite Type',14,'bold')

app=customtkinter.CTk()
app.geometry("460x370")
app.title("DataBase")
app.config(bg="#242424")

app.logo = CTk.CTkImage(dark_image=Image.open("db.png"), size=(250, 60))
app.logo_label = CTk.CTkLabel(master=app, text="", image=app.logo)
app.logo_label.grid(row=0, column=0)
app.logo_label.place(x=110,y=40)

db=sqlite3.connect("Employee.db")
db.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE (Employee_ID Integer, Name Text, Author Text)")
cursor=db.cursor()

def insert():
    row=[int(id_entry.get()), author_entry.get(), name_entry.get()]
    cursor.execute("INSERT into EMPLOYEE values (?, ?, ?);", (row))
    db.commit()

def clear():
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    author_entry.delete(0,END)

def delete():
    cursor.execute("DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID=?",[id_entry.get()])
    db.commit()
    
def update():
    new_details=[name_entry.get(),author_entry.get(),int(id_entry.get())]
    cursor.execute("UPDATE EMPLOYEE SET NAME=?, AUTHOR=? WHERE EMPLOYEE_ID=?", new_details)
    db.commit()

id_label=customtkinter.CTkLabel(app, text="ID:", font=font1)
id_label.place(x=110,y=100)
id_entry = customtkinter.CTkEntry(app,
                               placeholder_text="ID",
                               placeholder_text_color="#ffffff",
                               text_color="#ffffff",
                               fg_color="#242424",
                               border_color="#00CF00",
                               font=font1,
                               width=250,
                               )
id_entry.place(x=110,y=100)

name_label=customtkinter.CTkLabel(app, text="Author:", font=font1)
name_label.place(x=110,y=140)
name_entry = customtkinter.CTkEntry(app,
                               placeholder_text="Author",
                               placeholder_text_color="#ffffff",
                               text_color="#ffffff",
                               fg_color="#242424",
                               border_color="#00CF00",
                               font=font1,
                               width=250,
                               )
name_entry.place(x=110,y=140)

author_label=customtkinter.CTkLabel(app, text="Name:", font=font1)
author_label.place(x=110,y=180)
author_entry = customtkinter.CTkEntry(app,
                               placeholder_text="Name",
                               placeholder_text_color="#ffffff",
                               text_color="#ffffff",
                               fg_color="#242424",
                               border_color="#00CF00",
                               font=font1,
                               width=250,
                               )
author_entry.place(x=110,y=180)

save_button = customtkinter.CTkButton(app,
                                      text="Save",
                                      font=font1,
                                      command=insert,
                                      text_color="#202020",
                                      fg_color="#00CF00",
                                      hover_color="#23ac23",
                                      corner_radius=6,
                                      width=120,
                                      )
save_button.place(x=110,y=220)

update_button = customtkinter.CTkButton(app,
                                      text="Update",
                                      font=font1,
                                      command=update,
                                      text_color="#202020",
                                      fg_color="#00CF00",
                                      hover_color="#23ac23",
                                      corner_radius=6,
                                      width=120,
                                      )
update_button.place(x=240,y=220)

clear_button = customtkinter.CTkButton(app,
                                      text="Clear",
                                      font=font1,
                                      command=clear,
                                      text_color="#202020",
                                      fg_color="#00CF00",
                                      hover_color="#23ac23",
                                      corner_radius=6,
                                      width=120,
                                      )
clear_button.place(x=240,y=257)

delete_button = customtkinter.CTkButton(app,
                                      text="Delete",
                                      font=font1,
                                      command=delete,
                                      text_color="#202020",
                                      fg_color="#00CF00",
                                      hover_color="#23ac23",
                                      corner_radius=6,
                                      width=120,
                                      )
delete_button.place(x=110,y=257)

app.mainloop()