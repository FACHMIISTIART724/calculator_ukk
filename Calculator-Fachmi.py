
from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("CALCULATOR - Fachmi")
root.geometry("317x400")
root["bg"] = "#FEFBF3"

myfont = font.Font(size=15)

e = Entry(root,width=25,borderwidth=0)
e["font"] = myfont
e["bg"] = "#FEFBF3"
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

def angka(nilai):
    sebelum = e.get()
    e.delete(0,END)
    e.insert(0,str(sebelum)+str(nilai))
    
def tambah():
    nomor_awal = e.get()
    global n_awal
    global math
    math = "penambahan"
    n_awal = int(nomor_awal)
    e.delete(0,END)

def kurang():
    nomor_awal = e.get()
    global n_awal
    global math
    math = "pengurangan"
    n_awal = int(nomor_awal)
    e.delete(0,END)

def kali():
    nomor_awal = e.get()
    global n_awal
    global math
    math = "perkalian"
    n_awal = int(nomor_awal)
    e.delete(0,END)

def bagi():
    nomor_awal = e.get()
    global n_awal
    global math
    math = "pembagian"
    n_awal = int(nomor_awal)
    e.delete(0,END)

def hapus():
    e.delete(0,END)

def samadengan():
    nomor_akhir = e.get()
    e.delete(0,END)

    if math == "penambahan":
        e.insert(0,n_awal + int(nomor_akhir))
    elif math == "pengurangan":
        e.insert(0,n_awal - int(nomor_akhir))
    elif math == "perkalian":
        e.insert(0,n_awal * int(nomor_akhir))
    elif math == "pembagian":
        try:
            hitung = n_awal / int(nomor_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError:
            e.insert(0,'0')
    elif math == "sisabagi":
        e.insert(0,n_awal % int(nomor_akhir))





btn1 = Button(root,text="1",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(1))
btn2 = Button(root,text="2",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(2))
btn3 = Button(root,text="3",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(3))
btn4 = Button(root,text="4",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(4))
btn5 = Button(root,text="5",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(5))
btn6 = Button(root,text="6",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(6))
btn7 = Button(root,text="7",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(7))
btn8 = Button(root,text="8",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(8))
btn9 = Button(root,text="9",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(9))
btn0 = Button(root,text="0",padx=25,bg="#F8F0DF",fg="#161E54",font=('bold'),pady=20,command=lambda:angka(0))
tambah = Button(root,text="+",padx=25,bg="#9D9D9D",fg="#161E54",font=('bold'),pady=20,command=tambah)
kurang = Button(root,text="-",padx=27,bg="#9D9D9D",fg="#161E54",font=('bold'),pady=20,command=kurang)
kali = Button(root,text="x",padx=25,bg="#9D9D9D",fg="#161E54",font=('bold'),pady=20,command=kali)
bagi = Button(root,text="/",padx=27,bg="#9D9D9D",fg="#161E54",font=('bold'),pady=20,command=bagi)
hapus = Button(root,text="C",padx=25,bg="#9D9D9D",fg="#161E54",font=('bold'),pady=20,command=hapus)
sama = Button(root,text="=",padx=24.5,bg="#9D9D9D",fg="#161E54",font=('bold'),pady=20,command=samadengan)



btn1.grid(row=3,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=1,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)

tambah.grid(row=1,column=3,pady=2)
kurang.grid(row=2,column=3,pady=2)
kali.grid(row=3,column=3,pady=2)
bagi.grid(row=4,column=3,pady=2)
hapus.grid(row=4,column=0,pady=2)
sama.grid(row=4,column=2,pady=2)

root.mainloop()