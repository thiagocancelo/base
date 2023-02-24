import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3


ventana = tkinter.Tk()
ventana.geometry("450x300+500+250")
ventana.configure(bg="Pink")
bd = sqlite3.connect('Cancelo.db')
cur = bd.cursor()

#Funcion para guardar datos
def guardar(): 
    nombre = caja1.get()
    apellido = caja2.get()
    dni = caja3.get()
    telefono = caja4.get()  
    sql = 'INSERT OR IGNORE INTO Usuarios (nombre, apellido, dni, telefono) VALUES ("{}", "{}", "{}", "{}");'
    cur.execute(sql.format(nombre,apellido,dni,telefono))
    bd.commit()
    
    caja1.delete(0,"end")
    caja2.delete(0,"end")
    caja3.delete(0,"end")
    caja4.delete(0,"end")
    
    print("Datos Guardados Exitosamente")
  
  
#Funcion para buscar datos
def buscar(event):
    
    caja1.delete(0, END)
    caja2.delete(0, END)
    caja3.delete(0, END)
    caja4.delete(0, END)
    
    
    print("elegido",event)
    sql = "select nombre, apellido, telefono, dni from Usuarios where dni=?"
    resp = cur.execute(sql, (event[0],))
    resp = cur.fetchall() 
    print("resp", resp)
    
    caja1.insert(0, resp[0][0])    
    caja2.insert(0, resp[0][1])
    caja3.insert(0, resp[0][2])
    caja4.insert(0, resp[0][3])


def llenar_combo():
    sql = 'SELECT dni, nombre, apellido, telefono from Usuarios;'
    cur.execute(sql)
    resp = cur.fetchall() 
    for i in resp:
        OptionList.append(i)


def click_nombre(nombre):
    print("nombre: ", nombre)
    sql = 'SELECT nombre from Usuarios;'
    cur.execute(sql)
    resp = cur.fetchall() 
    for i in resp:
        OptionList.append(i)

OptionList = []
llenar_combo()



variable = tk.StringVar(ventana)
variable.set("Buscar Datos guardados")

opt = tk.OptionMenu(ventana, variable , *OptionList, command = buscar)
opt.config(width=50, font=(12))
opt.pack()

Label(ventana, text = "nombre:").pack()
caja1 = Entry(ventana)
caja1.bind("<Button-1>", click_nombre)
caja1.pack()

Label(ventana, text = "apellido:").pack()
caja2 = Entry(ventana)
caja2.pack()

Label(ventana, text = "dni").pack()
caja3 = Entry(ventana)
caja3.pack()

Label(ventana, text = "telefono:").pack()
caja4 = Entry(ventana)
caja4.pack()

boton = ttk.Button(text="Guardar Datos", command = guardar)
boton.place(x=170, y=260)


ventana.mainloop()