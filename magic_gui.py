import magic
from tkinter import *
from tkinter import messagebox

root = Tk()
root.resizable(0,0)
root.title("Mystery Box")

getcode = StringVar()
mystery = magic.generate()

fontL = ("Verdana", 32)
fontE = ("Verdana", 18)

def close(): 
    root.destroy()

def code():
    if getcode.get() == mystery[1]:
        messagebox.showinfo("Very good", "You are master.")
        close()
    else:
        messagebox.showinfo("Wrong", "This is not correct password.")
        close()

label1 = Label(root, text='You won\'t find my magic code', fg='red')
label1.grid(row=1, columnspan=3, sticky='WE', pady=20)

label2 = Label(root, text=mystery[0], relief='sunken', font=fontL)
label2.grid(row=3, columnspan=3, sticky='WE')

entry = Entry(root, textvariable=getcode, font=fontE)
entry.grid(row=5, column=0, pady=20)

button = Button(root, text='OK', command=code)
button.grid(row=5, column=2, pady=20, sticky='NS')

root.mainloop()