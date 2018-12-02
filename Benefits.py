#!/usr/bin/python3

from tkinter import Tk, RIDGE, ttk, messagebox

root = Tk()
style = ttk.Style()
style.theme_use("alt")
style.configure("TFrame", background="black")
style.configure("TButton", background="yellow", foreground="black")
style.configure("TLabel", background="black", foreground="white")
root.configure(width=280, height=400, background="black")

# Frames
f1 = ttk.Frame(root, width=200, height=200, padding=(10, 10), relief=RIDGE)
f1.pack()

f2 = ttk.Frame(root, width=200, height=200, padding=(10, 10), relief=RIDGE)
f2.pack()


# Simple Benefit's Function

def SB():
    c = en1.get()
    C = float(c)
    I = en2.get()
    i = float(I)
    T = en3.get()
    t = float(T)
    SB = C * (1 + (i/100) * t)
    #print("SB= ", SB, " S.P")
    messagebox.showinfo("Simple Benefit","Simple Benefit = {}".format(SB))


#Compound Benefit's Function

def CB():
    c = en1.get()
    C = float(c)
    I = en2.get()
    i = float(I)
    T = en3.get()
    t = float(T)
    CB = C * (1 + (i/100)) ** t
    #print("CB= ", CB, " S.P")
    messagebox.showinfo("Compound Benefit", "Compound Benefit = {}".format(CB))


# Add Buttons

bu1 = ttk.Button(f1, text="Simple Benefit", command=SB)
bu1.grid(row=0, column=0, padx=18)

bu2 = ttk.Button(f1, text="Compound Benefit", command=CB)
bu2.grid(row=0, column=3, padx=18)

# Add Labels

tx1 = ttk.Label(f2, text="Amount invested", padding=(8, 8))
tx1.grid(row=0, column=0, padx=9)

tx2 = ttk.Label(f2, text="Rate  % ", padding=(8, 8))
tx2.grid(row=1, column=0, padx=9)

tx3 = ttk.Label(f2, text="Period (Year)", padding=(8, 8))
tx3.grid(row=2, column=0, padx=9)
tx4 = ttk.Label(f2, text="@  T   A   R   E   K", padding=(8, 8))
tx4.grid(row=3, column=0, rowspan=2, columnspan=3)

#Add Entries

en1 = ttk.Entry(f2, font=("Arial", 8))
en1.grid(row=0, column=2, padx=9)

en2 = ttk.Entry(f2, font=("Arial", 8))
en2.grid(row=1, column=2, padx=9)

en3 = ttk.Entry(f2, font=("Arial", 8))
en3.grid(row=2, column=2, padx=9)

root.mainloop()

###############------------TarekGhajary------------#################
