from Tkinter import *
from Lexico import Lexico

root=Tk()

root.title("Compilador en Python")

root.geometry("500x270")

root.resizable(0,0)

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
	mensaje.set("ffffff")
	l=Lexico()
	l.set_source(textEntry.get())
	l.analysis()
	print(l.get_message())


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


mensaje=StringVar()
mensaje.set("gg")

msgLabel=Label(outFrame, textvariable=mensaje)

msgLabel.config(bg="white",fg="black", font=("Consolas",12))


msgLabel.place(x=0,y=0)


#Agregar Scroll a un Text
#scrollVert=Scrollbar(frame,command=textUno.yview) luego no se si pack o place
# en config agrgar sticky="nsew"
#text.config(yscrollcommand=scrollVert.set)
root.mainloop() 