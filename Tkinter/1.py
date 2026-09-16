#Tkinter
#Libraries
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

#Creat window
root = Tk()
root.title("App Name")
root.geometry("500x500")
root.resizable(1,1)
root.config(bg="gray")
root.iconbitmap(r"D:\HTML CSS\Sealix AI\images\sealix-logo.ico")

#Lable
tex = Label(root , text="Hello World" , bg="gray" , fg="white" , font=("Arial" , 20))
tex.pack()

#Entry
inpu = Entry(root , width=20 , bg="lightgray" , fg="black" , font=("Arial" , 15))
inpu.insert(END,"Write Somethings...")
inpu.delete(0, END)
inpu.pack()
print(inpu.get())

#Text
longinpu = Text(root , width=20 , height=3 , bg="white" , fg="gray" , font=("Arial" , 10))
longinpu.insert(END,"Write Somethings...")
longinpu.pack()
print(longinpu.get("1.0" , END))

#Checkbutton
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
checkbu = Checkbutton(root , text="Option 1" , bg="gray" , font=("Arial" , 10) , variable=check1)
checkbu.pack()
checkbu = Checkbutton(root , text="Option 2" , bg="gray" , font=("Arial" , 10) , variable=check2)
checkbu.pack()
checkbu = Checkbutton(root , text="Option 3" , bg="gray" , font=("Arial" , 10) , variable=check3)
checkbu.pack()

#Radiobutton
radio = IntVar()
radiobu = Radiobutton(root , text="Option 1" , bg="gray" , fg="blue" , font=("Arial" , 10) , variable=radio , value=1)
radiobu.pack()
radiobu = Radiobutton(root , text="Option 2" , bg="gray" , fg="blue" , font=("Arial" , 10) , variable=radio , value=2)
radiobu.pack()
radiobu = Radiobutton(root , text="Option 3" , bg="gray" , fg="blue" , font=("Arial" , 10) , variable=radio , value=3)
radiobu.pack()

#Combobox(ttk)
combo = ttk.Combobox(root , text="Option 3" , font=("Arial" , 10) , value=["Option 1" , "Option 2" , "Option 3"])
combo.current(2)
combo.pack()
print(combo.get())

#Listbox
lis = Listbox(root , width=30 , height=5 , bg="lightgray" , fg="gray" , font=("Arial" , 13))
lis.insert(0,"Option 1")
lis.insert(1,"Option 2")
lis.insert(2,"Option 3")
lis.pack()

#Messagebox(messagebox)
def messa1():
    messagebox.showinfo("Button","Thanks for clicking me!")
def messa2():
    messagebox.showerror("Report","You can not report anything!")

#Add new window
def new_page():
    root2 = Tk()
    root2.mainloop()

#Delete widgets
def clear_page():
    for i in root.winfo_children():
        i.destroy()

#Button
butt = Button(root , text="Click me" , width=20 , height=3 , bg="pink" , fg="black" , font=("Arial" , 10) , relief="raised" , borderwidth=20 , activebackground="green" , activeforeground="white" , command=messa1)
butt.pack()

#Canvas
can = Canvas(root , width=300 , height=200 , bg="lightblue" , relief="flat" , borderwidth=20)

can.create_rectangle(200 , 100 , 200 , 30)
can.pack()

#PhotoImage
img = PhotoImage(file=r"D:\CLASS\Python - 201\Tkinter\1.png")
lab = Label(root, image=img)
lab.place(x=910,y=50)

#Open,Save(filedialog)
def open():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            longinpu.delete(1.0,END)
            longinpu.insert(END, content)
def save():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")#فرمت
    if file_path:
        content = longinpu.get(1.0,END)
        with open(file_path, 'w') as file:
            file.write(content)

#Menu
men = Menu(root)

file_men = Menu(men , tearoff=0)
file_men.add_command(label="Open" , command=open)
file_men.add_command(label="Save" , command=save)
file_men.add_separator()
file_men.add_command(label="New page" , command=new_page)
file_men.add_command(label="Clear" , command=clear_page)
men.add_cascade(label="File",menu=file_men)

help_men = Menu(men , tearoff=0)
help_men.add_command(label="report" , command=messa2)
help_men.add_command(label="Do Nothing")
men.add_cascade(label="Help",menu=help_men)

root.config(menu=men)

#Frame
fram = Frame(root, bg="lightgray", width=3000, height=200)
fram.place(x=0,y=0)

labelf = Label(fram, text="Enter your name:")
labelf.pack(pady=10)

entryf = Entry(fram)
entryf.pack()

buttonf = Button(fram, text="تأیید")
buttonf.pack(pady=10)

#Locations
"""
.pack() --> padx=00 , pady=00 , side=right,left
.grid() --> padx=00 , pady=00 , row=0 , column=0
.place() --> x=00 , y=00
"""

#Run app
root.mainloop()