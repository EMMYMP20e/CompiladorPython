from Tkinter import *
from Lexico import Lexico
from sintacticTree import *
from ScrolledText import ScrolledText
import os


root=Tk()

root.title("Compilador en Python")

root.geometry("930x520")#500x360

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

inFrame.config( width=480, height=250, bg="#ECEFF1") #

inFrame.place(x=10,y=37);

inFrame.config(bd=3,relief="ridge")

#		-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
'''
textEntry=Text(inFrame)

textEntry.config(bg="white",fg="black", font=("Consolas",12))

textEntry.place(x=10,y=30)'''
TextArea=ScrolledText(inFrame,undo=True)
TextArea.config(width=50, height=14)
TextArea.place(x=0,y=0)
#BTextArea.place(x=0,y=0)

"""TextArea = Text(inFrame,width=400, height=100)
ScrollBar = Scrollbar(inFrame)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
#ScrollBar.place(x=400,y=10)
TextArea.place(x=0,y=0)"""
#ScrollBar.pack(side=RIGHT, fill=Y)



def sintaxAnalysis(l):
	ids=l.get_ids()
	node=Node(None)
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
	print(ids)
	stack=[]
	'''
	'''
	h=l.get_eps()
	simbols=[]
	reductions=[]
	tableLR=[]
	names=[]
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
	stack.append('$')
	stack.append(0)
	count=0
	while True:
		x=stack.pop()
		stack.append(x)
		try:
			y=ids[count]
		except:
			print('y')
			break
		try:
			action=tableLR[x][y]
		except:
			print(x,y)
			break
		
		strStack=[]
		for i in stack:
			try:
				strStack.append(i.get_Name())
			except:
				strStack.append(i)
		print ("Pila: ",strStack)
		print ("Entrada: ",y)
		print ("Salida",action)
		if action==0:
			break;
		if action>0:
			stack.append(h[count])
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
			daRule="R"+str(index+1)
			#print(" -"+daRule,red)
			if (index+1)==1:
				node=Rule1(stack)
			elif (index+1)==2:
				node=Rule2(stack)
			elif (index+1)==3:
				node=Rule3(stack)
			elif (index+1)==4:
				node=Rule4(stack)
			elif (index+1)==5:
				node=Rule5(stack)
			elif (index+1)==6:
				node=Rule6(stack)
			elif (index+1)==7:
				node=Rule7(stack)
			elif (index+1)==8:
				node=Rule8(stack)
			elif (index+1)==9:
				node=Rule9(stack)
			elif (index+1)==10:
				node=Rule10(stack)
			elif (index+1)==11:
				node=Rule11(stack)
			elif (index+1)==12:
				node=Rule12(stack)
			elif (index+1)==13:
				node=Rule13(stack)
			elif (index+1)==14:
				node=Rule14(stack)
			elif (index+1)==15:
				node=Rule15(stack)
			elif (index+1)==16:
				node=Rule16(stack)
			elif (index+1)==17:
				node=Rule17(stack)
			elif (index+1)==18:
				node=Rule18(stack)
			elif (index+1)==19:
				node=Rule19(stack)
			elif (index+1)==20:
				node=Rule20(stack)
			elif (index+1)==21:
				node=Rule21(stack)
			elif (index+1)==22:
				node=Rule22(stack)
			elif (index+1)==23:
				node=Rule23(stack)
			elif (index+1)==24:
				node=Rule24(stack)
			elif (index+1)==25:
				node=Rule25(stack)
			elif (index+1)==26:
				node=Rule26(stack)
			elif (index+1)==27:
				node=Rule27(stack)
			elif (index+1)==28:
				node=Rule28(stack)
			elif (index+1)==29:
				node=Rule29(stack)
			elif (index+1)==30:
				node=Rule30(stack)
			elif (index+1)==31:
				node=Rule31(stack)
			elif (index+1)==32:
				node=Rule32(stack)
			elif (index+1)==33:
				node=Rule33(stack)
			elif (index+1)==34:
				node=Rule34(stack)
			elif (index+1)==35:
				node=Rule35(stack)
			elif (index+1)==36:
				node=Rule36(stack)
			elif (index+1)==37:
				node=Rule37(stack)
			elif (index+1)==38:
				node=Rule38(stack)
			elif (index+1)==39:
				node=Rule39(stack)
			elif (index+1)==40:
				node=Rule40(stack)
			elif (index+1)==41:
				node=Rule41(stack)
			elif (index+1)==42:
				node=Rule42(stack)
			elif (index+1)==43:
				node=Rule43(stack)
			elif (index+1)==44:
				node=Rule44(stack)
			elif (index+1)==45:
				node=Rule45(stack)
			elif (index+1)==46:
				node=Rule46(stack)
			elif (index+1)==47:
				node=Rule47(stack)
			elif (index+1)==48:
				node=Rule48(stack)
			elif (index+1)==49:
				node=Rule49(stack)
			elif (index+1)==50:
				node=Rule50(stack)
			elif (index+1)==51:
				node=Rule51(stack)
			elif (index+1)==52:
				node=Rule52(stack)
				#print(stack)
			else:
				while red>0:
					stack.pop()
					red-=1
			b=stack.pop()
			stack.append(b)
			
			x=tableLR[b][sim]
			stack.append(node)
			stack.append(x)
	if state==True:
		salidaTxt.insert('1.0','Sintaxis Aceptada\n')
		tree=node.muestra()
		treeTxt.insert(END,tree)
		lista=node.semantico()
		listaErrores=lista.get_ListaErrores()
		if len(listaErrores)==0:
			salidaTxt.insert(END,'Semantica Aceptada\n')
			#cmd="cmd"
			#subprocess.Popen(cmd)
			for i in range(0,10):
				print('\n')
			doc="global _main\nextern _printf\nsection .bss\n"
			for n in lista.get_ListaVariables():
				doc+=n.get_Nombre()+": dd 0\n"
			doc+="\nsection .text\n\n_main:\n"
			cds=node.codeGen().get_Codigo()
			for i in cds:
				doc+=i
			cont=0
			for n in lista.get_ListaVariables():
				doc+="push DWORD ["+n.get_Nombre()+"]\n"
				cont+=1
			doc+="\npush message\ncall _printf\nadd esp,"
			doc+=str(((cont*4)+4))+"\n"
			doc+="ret\n\nmessage:\ndb '"
			variables=lista.get_ListaVariables()
			variables.reverse()
			for i in variables:
				doc+=i.get_Nombre()+": %d "
			doc+="', 10,0"
			#fileAsm=open("C:\\MinGW\\bin\\Codes\\test.asm","w")
			fileAsm=open("C:\\test.asm","w")
			fileAsm.write(doc)
			fileAsm.close()
			#os.system('cd C:\\MinGW\\bin\\Codes & nasm -fwin32 test.asm & gcc test.obj -o test.exe & C:\\MinGW\\bin\\Codes\\test.exe')
			os.system('cd C:\\ & nasm -fwin32 test.asm & gcc test.obj -o test.exe & C:\\test.exe')
		else:
			salidaTxt.insert(END,'---Errores Semanticos:---\n\n')
		for i in listaErrores:
			salidaTxt.insert(END,'-'+i+'\n')
	else:
		salidaTxt.insert('1.0','Sintaxis Incorrecta\n')
	
	#tabla=[],[]
	#tabla.add(2,3)
	#print tabla



#		-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
def analisis():
	l=Lexico()
	l.set_source(TextArea.get("1.0",END))
	l.analysis()
	l.get_message().remove("")
	salidaTxt.delete('1.0',END)
	treeTxt.delete('1.0',END)
	#print(l.get_ids())
	sintaxAnalysis(l)

	
	


boton=Button(inputFrame,text="Analizar", command=analisis)

boton.place(x=400,y=0)

#---------------------------------------------------------------------
outputFrame=Frame(root)

outputFrame.config( width=480, height=35, bg="#009A80") #009AF6

outputFrame.place(x=10,y=285);

outputFrame.config(bd=3,relief="ridge")

miLabel=Label(outputFrame, text="Compilador: ")

miLabel.config(bg="#009A80",fg="white", font=("Consolas",12))

miLabel.place(x=0,y=0)

outFrame=Frame(root)

outFrame.config( width=480, height=180, bg="white") #009AF6

outFrame.place(x=10,y=320);

outFrame.config(bd=3,relief="ridge")

"""s=Scrollbar(outFrame)

listBox=Listbox(outFrame, width=64,height=10,yscrollcommand=s.set)

s.config(command=listBox.yview)

s.pack(side=RIGHT, fill=Y)

listBox.pack(side=LEFT, fill=BOTH, expand=True)"""

"""mensaje=StringVar()
mensaje.set("")

s=Scrollbar(outFrame)

RLabel=Label(outFrame,textvariable=mensaje)

RLabel.config(bg="white",fg="black", font=("Consolas",12))

RLabel.place(x=5,y=10)"""
"""salidaTxt=Text(outFrame)

salidaTxt.pack(side=LEFT, expand=False, fill=BOTH)

sb = Scrollbar(outFrame)
sb.config(command=salidaTxt.yview)
sb.pack(side=RIGHT, fill=Y)
 
salidaTxt.config(yscrollcommand=sb.set)"""
salidaTxt=ScrolledText(outFrame,undo=True)
salidaTxt.config(width=50,height=10)
salidaTxt.place(x=0,y=0)


titleTree=Frame(root)

titleTree.config( width=400, height=35, bg="#009A80") #009AF6

titleTree.place(x=500,y=105);

titleTree.config(bd=3,relief="ridge")

treeLabel=Label(titleTree, text="Arbol Sintactico: ")

treeLabel.config(bg="#009A80",fg="white", font=("Consolas",12))

treeLabel.place(x=0,y=0)

treeFrame=Frame(root)

treeFrame.config( width=400, height=300, bg="white") #009AF6

treeFrame.place(x=500,y=140);

treeFrame.config(bd=3,relief="ridge")


treeTxt=ScrolledText(treeFrame,undo=True)
treeTxt.config(width=41,height=17)
treeTxt.place(x=0,y=0)

root.mainloop() 






	








