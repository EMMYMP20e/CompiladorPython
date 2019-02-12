from Tkinter import *
from Lexico import Lexico

root=Tk()

root.title("Compilador en Python")

root.geometry("500x360")

root.resizable(1,1)

#root.config(bg="green")

# Frame inputFrame	-	-	-	-	-	-	-	-	-	-	-	-	-
inputFrame=Frame(root)

inputFrame.config( width=480, height=35, bg="#00695C") #009AF6

inputFrame.place(x=10,y=5);

inputFrame.config(bd=3,relief="ridge")

# InputLabel		-	-	-	-	-	-	-	-	-	-	-	-	-

inLabel=Label(inputFrame, text="Input: ")

inLabel.config(bg="#00695C",fg="white", font=("Consolas",12))

inLabel.place(x=0,y=0)
#		-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-

inFrame=Frame(root)

inFrame.config( width=480, height=90, bg="#ECEFF1") #

inFrame.place(x=10,y=37);

inFrame.config(bd=3,relief="ridge")

#		-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-

textEntry=Entry(inFrame)

textEntry.config(bg="white",fg="black", font=("Consolas",12))

textEntry.place(x=10,y=30)

#		-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-

def analisis():
	#mensaje.set("ffffff")
	listBox.delete(0,END)
	l=Lexico()
	print(textEntry.get())
	l.set_source(textEntry.get())
	l.analysis()
	print(l.get_message())
	l.get_message().remove("")
	for m in l.get_message():
		listBox.insert(END,m)


boton=Button(inFrame,text="Analizar", command=analisis)

boton.place(x=300,y=29)

#---------------------------------------------------------------------
outputFrame=Frame(root)

outputFrame.config( width=480, height=35, bg="#009A80") #009AF6

outputFrame.place(x=10,y=130);

outputFrame.config(bd=3,relief="ridge")

miLabel=Label(outputFrame, text="Compilador: ")

miLabel.config(bg="#009A80",fg="white", font=("Consolas",12))

miLabel.place(x=0,y=0)

outFrame=Frame(root)

outFrame.config( width=480, height=90, bg="white") #009AF6

outFrame.place(x=10,y=165);

outFrame.config(bd=3,relief="ridge")

s=Scrollbar(outFrame)

listBox=Listbox(outFrame, width=64,height=10,yscrollcommand=s.set)

s.config(command=listBox.yview)

s.pack(side=RIGHT, fill=Y)

listBox.pack(side=LEFT, fill=BOTH, expand=True)


root.mainloop() 