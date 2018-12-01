from tkinter import *
from tkinter import ttk
from math import *

root=Tk()
style=ttk.Style()
style.theme_use("alt")
style.configure("TFrame",background="black")
style.configure("TButton",background="yellow",foreground="black")
style.configure("TLabel",background="black",foreground="white")
root.configure(width=280,height=400,background="black")

#Frames
f1=ttk.Frame(root,width=200,height=200,padding=(10,10),relief=RIDGE)
f1.pack()

f2=ttk.Frame(root,width=200,height=200,padding=(10,10),relief=RIDGE)
f2.pack()



#دالة حساب الفائدة البسيطة

def Ct1():
    c=en1.get()
    C=float(c)
    I=en2.get()
    i=float(I)
    T=en3.get()
    t=float(T)
    Ct1=C*(1+i*t)
    print("Ct1= ",Ct1," S.P")
    

#دالة حساب الفائدة المركبة
    
def Ct2():
    c=en1.get()
    C=float(c)
    I=en2.get()
    i=float(I)
    T=en3.get()
    t=float(T)
    Ct2=C*(1+i)**t
    print("Ct2= ",Ct2," S.P")



          
#اضافات كبسات الى الفرام الاولى

bu1=ttk.Button(f1,text="فائدة بسيطة",command=Ct1)
bu1.grid(row=0,column=0,padx=18)


bu2=ttk.Button(f1,text="فائدة مركبة",command=Ct2)
bu2.grid(row=0,column=3,padx=18)



#اضافة النصوص

tx1=ttk.Label(f2,text="المبلغ المستثمر",padding=(8,8))
tx1.grid(row=0,column=0,)

tx2=ttk.Label(f2,text=" معدل الفائدة ",padding=(8,8))
tx2.grid(row=1,column=0)

tx3=ttk.Label(f2,text="المدة بالسنوات",padding=(8,8))
tx3.grid(row=2,column=0)
tx4=ttk.Label(f2,text="@  T   A   R   E   K",padding=(8,8))
tx4.grid(row=3,column=0,rowspan=2,columnspan=3)


#اضافة خانات الادخال
              
en1=ttk.Entry(f2,font=("Arial",8))
en1.grid(row=0,column=2)

en2=ttk.Entry(f2,font=("Arial",8))
en2.grid(row=1,column=2)

en3=ttk.Entry(f2,font=("Arial",8))
en3.grid(row=2,column=2)






root.mainloop()



###############------------TarekGhajary------------#################
