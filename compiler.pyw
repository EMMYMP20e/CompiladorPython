from Tkinter import *
from Lexico import Lexico

root=Tk()

root.title("Compilador en Python")

root.geometry("500x400")#500x360

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

inFrame.config( width=480, height=190, bg="#ECEFF1") #

inFrame.place(x=10,y=37);

inFrame.config(bd=3,relief="ridge")

#		-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
'''
textEntry=Text(inFrame)

textEntry.config(bg="white",fg="black", font=("Consolas",12))

textEntry.place(x=10,y=30)'''
TextArea = Text(inFrame,width=400, height=100)
ScrollBar = Scrollbar(inFrame)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
#ScrollBar.place(x=50,7=0)
TextArea.place(x=0,y=0)



def sintaxAnalysis(l):
	ids=l.get_ids()
	'''copia=list(ids)
	c=0
	while c<copia.count(5):
		ids.remove(5)
		c+=1
	c=0
	for i in copia:
		if i==5:
			ids.insert(c,1)
		c+=1
	'''
	ids.append(23)
	print ids
	stack=[]
	'''
	tableLR=[[2,0,0,1],[0,0,-1,0],[0,3,-3,0],[2,0,0,4],[0,0,-2,0]]
	print tableLR
	simbols=[3,3]
	reductions=[6,2]
	'''
	simbols=[]
	reductions=[]
	tableLR=[]
	fileRules = open("rules.txt", "r")
	for linea in fileRules.readlines():
		nums=linea.split()
		simbols.append(int(nums.pop(0)))
		reductions.append(int(nums.pop(0)))
	fileRules.close() 
	fileTable=open("tableLR.txt","r")
	for line in fileTable.readlines():
		ints=[]
		strLine=line.split()
		for s in strLine:
			ints.append(int(s))
		tableLR.append(ints)
	fileTable.close()

	state=False
	stack.append(0)
	stack.append(0)
	count=0
	while True:
		x=stack.pop()
		stack.append(x)

		try:
			y=ids[count]
		except:
			break
		try:
			action=tableLR[x][y]
		except:
			break
		print ("Pila: ",stack)
		print ("entrada: ",y)
		print ("Salida",action)
		if action==0:
			break;
		if action>0:
			stack.append(ids[count])
			stack.append(action)
			count+=1
		elif action<0:
			if action==-1:
				state=True
				break
			index=(action*-1)-2
			sim=simbols[index]
			red=reductions[index]
			red=red*2
			print sim,red
			while red>0:
				stack.pop()
				red-=1
			b=stack.pop()
			stack.append(b)
			
			x=tableLR[b][sim]
			stack.append(sim)
			stack.append(x)
	
	if state==True:
		mensaje.set("Input Aceptado")
	else:
		mensaje.set("Input Incorrecto")


#		-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
def analisis():
	l=Lexico()
	l.set_source(TextArea.get("1.0",END))
	l.analysis()
	l.get_message().remove("")
	#print(l.get_ids())
	sintaxAnalysis(l)
	
	


boton=Button(inFrame,text="Analizar", command=analisis)

boton.place(x=300,y=29)

#---------------------------------------------------------------------
outputFrame=Frame(root)

outputFrame.config( width=480, height=35, bg="#009A80") #009AF6

outputFrame.place(x=10,y=230);

outputFrame.config(bd=3,relief="ridge")

miLabel=Label(outputFrame, text="Compilador: ")

miLabel.config(bg="#009A80",fg="white", font=("Consolas",12))

miLabel.place(x=0,y=0)

outFrame=Frame(root)

outFrame.config( width=480, height=90, bg="white") #009AF6

outFrame.place(x=10,y=265);

outFrame.config(bd=3,relief="ridge")

"""s=Scrollbar(outFrame)

listBox=Listbox(outFrame, width=64,height=10,yscrollcommand=s.set)

s.config(command=listBox.yview)

s.pack(side=RIGHT, fill=Y)

listBox.pack(side=LEFT, fill=BOTH, expand=True)"""

mensaje=StringVar()
mensaje.set("")

RLabel=Label(outFrame, textvariable=mensaje)

RLabel.config(bg="white",fg="black", font=("Consolas",12))

RLabel.place(x=5,y=10)


root.mainloop() 






	








