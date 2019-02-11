from Tkinter import *

root=Tk()

root.title("Compilador en Python")

root.geometry("450x220")

root.resizable(0,0)

#root.config(bg="green")

miFrame=Frame(root, width=500, height=400)

miFrame.pack();

miLabel=Label(miFrame, text="Hola")

miLabel.pack()

root.mainloop()