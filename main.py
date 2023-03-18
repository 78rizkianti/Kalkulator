from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("Kalkulator")
root.geometry("315x410")
root["bg"] = "#EFF5F5"

myfont = font.Font(size=15)

e = Entry(root,width=25,borderwidth=0)
e["font"] = myfont
e["bg"] = "#EFF5F5"
e["fg"] = "#000000"
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

def angka(nilai):
  sebelum = e.get()
  e.delete(0,END)
  e.insert(0,str(sebelum)+str(nilai))

def tambah():
  nomor_awal = e.get()
  global n_awal
  global mtk
  mtk = "penjumlahan"
  n_awal = int(nomor_awal)
  e.delete(0,END)

def kurang():
  nomor_awal = e.get()
  global n_awal
  global mtk
  mtk = "pengurangan"
  n_awal = int(nomor_awal)
  e.delete(0,END)

def bagi():
  nomor_awal = e.get()
  global n_awal
  global mtk
  mtk = "pembagian"
  n_awal = int(nomor_awal)
  e.delete(0,END)

def kali():
  nomor_awal = e.get()
  global n_awal
  global mtk
  mtk = "perkalian"
  n_awal = int(nomor_awal)
  e.delete(0,END)

def akar():
  nomor_awal = e.get()
  global n_awal
  n_awal = int(nomor_awal) 
  e.delete(0,END)
  e.insert(0,math.sqrt(n_awal))

def pangkat():
  nomor_awal = e.get()
  global n_awal
  n_awal = int(nomor_awal) 
  e.delete(0,END)
  e.insert(0,n_awal **2)

def sisabagi():
  nomor_awal = e.get()
  global n_awal
  global mtk
  mtk = "sisabagi"
  n_awal = int(nomor_awal)
  e.delete(0,END)

def samadengan():
  nomor_akhir = e.get()
  e.delete(0,END)
  if mtk == "penjumlahan" :
    e.insert(0,n_awal + int(nomor_akhir))
  elif mtk == "pengurangan" :
    e.insert(0,n_awal - int(nomor_akhir))
  if mtk == "pembagian" :
    try:
      hitung = n_awal / int(nomor_akhir)
      e.insert(0,hitung)
    except ZeroDivisionError:
      e.insert(0, 'tidak ada hasil pada kalkulator')
  elif mtk == "perkalian" :
    e.insert(0,n_awal * int(nomor_akhir))
  elif mtk == "sisabagi" :
    e.insert(0,n_awal % int(nomor_akhir))

def hapus():
  e.delete(0,END)

btn1 = Button(root,text="1",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(1))
btn2 = Button(root,text="2",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(2))
btn3 = Button(root,text="3",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(3))
btn4 = Button(root,text="4",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(4))
btn5 = Button(root,text="5",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(5))
btn6 = Button(root,text="6",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(6))
btn7 = Button(root,text="7",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(7))
btn8 = Button(root,text="8",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(8))
btn9 = Button(root,text="9",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(9))
btn0 = Button(root,text="0",padx=30,bg="#D6E4E5",fg="#000000",pady=20,command=lambda:angka(0))

tmb = Button(root,text="+",padx=27,bg="#EB6440",fg="#000000",pady=20,command=tambah)
krg = Button(root,text="-",padx=28,bg="#EB6440",fg="#000000",pady=20,command=kurang)
bgi = Button(root,text="/",padx=28,bg="#EB6440",fg="#000000",pady=20,command=bagi)
kli = Button(root,text="x",padx=27,bg="#EB6440",fg="#000000",pady=20,command=kali)
samde = Button(root,text="=",padx=67,bg="#497174",fg="#000000",pady=20,command=samadengan)
hps = Button(root,text="C",padx=28,bg="#497174",pady=20,command=hapus)

akr = Button(root,text="√",padx=28,bg="#497174",pady=20,command=akar)
sib = Button(root,text="mod",padx=21,bg="#EB6440",fg="#000000",pady=20,command=sisabagi)
pkt = Button(root,text="x²",padx=28,bg="#497174",pady=20,command=pangkat)

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

tmb.grid(row=1,column=3,pady=2)
krg.grid(row=2,column=3,pady=2)
bgi.grid(row=3,column=3,pady=2)
kli.grid(row=4,column=3,pady=2)
samde.grid(row=5,column=2,pady=2,columnspan=2)
hps.grid(row=4,column=0,pady=2)

akr.grid(row=5,column=0,pady=2)
sib.grid(row=4,column=2,pady=2)
pkt.grid(row=5,column=1,pady=2)
root.mainloop()