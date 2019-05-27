
class SimboloFuncion(object):
	def __init__(self,tipo,ambito):
		self.tipo=tipo
		self.ambito=ambito
	def get_Tipo(self):
		return self.tipo
	def get_Ambito(self):
		return self.ambito


class SimboloVariable(object):
	def __init__(self,tipo,nombre,ambito):
		self.tipo=tipo
		self.nombre=nombre
		self.ambito=ambito
	def get_Tipo(self):
		return self.tipo
	def get_Nombre(self):
		return self.nombre
	def get_Ambito(self):
		return self.ambito

class TablaSimbolos(object):
	def __init__(self):
		self.tablaVariables=[]
		self.tablaFunciones=[]
		self.ambito=""
		self.listaErrores=[]
		self.tipoAnterior=""
	def add_tablaVariables(self,simVar):
		self.tablaVariables.append(simVar)
	def add_tablaFunciones(self,simFun):
		self.tablaFunciones.append(simFun)
	def isInTablaVariables(self,simVar):
		for i in self.tablaVariables:
			if i.get_Nombre()==simVar.get_Nombre():
				#print(i.get_Nombre(),simVar.get_Nombre())
				
				#print(i.get_Ambito(),simVar.get_Ambito())
				if i.get_Ambito()==simVar.get_Ambito():
					return True
				if i.get_Ambito()=="" and simVar.get_Ambito()!="":
					return True
		return False
	def isIntablaFunciones(self,simFun):
		for i in self.tablaFunciones:
			if i.get_Ambito()==simFun.get_Ambito():
				return True
		return False
	def add_Error(self,msg):
		self.listaErrores.append(msg)
	def cambia_Ambito(self,ambito):
		self.ambito=ambito
	def get_Ambito(self):
		return self.ambito
	def set_TipoAnterior(self,tipo):
		self.tipoAnterior=tipo
	def get_TipoAnterior(self):
		return self.tipoAnterior
	def get_TipoFuncion(self,ambito):
		for i in self.tablaFunciones:
			if i.get_Ambito()==ambito:
				return i
		v=SimboloFuncion("","")
		return v
	def get_TipoVariable(self,nombre):
		for i in self.tablaVariables:
			if i.get_Nombre()==nombre:
				return i
		v=SimboloVariable("","","")
		return v
	def get_ListaErrores(self):
		return self.listaErrores
	def printTables(self):
		for i in self.tablaFunciones:
			print(i.get_Tipo(),i.get_Ambito())
		for i in self.tablaVariables:
			print(i.get_Ambito(),i.get_Tipo(),i.get_Nombre())
	def get_ListaVariables(self):
		return self.tablaVariables
class CodigoGenerado(object):
	def __init__(self):
		self.lines=[]
	def addLine(self,line):
		self.lines.append(line)
	def get_Codigo(self):
		return self.lines



class Node(object):
	def __init__(self,node):
		self.node=node
		self.name=" "
	def __str__(self):
		return self.name
	def get_Name(self):
		return self.name


class Rule1(Node):
	def __init__(self,pila):
		pila.pop()
		self.node=pila.pop()
		self.name="R1"
	def get_Node(self):
		return self.node

	def muestra(self):
		msg=""
		msg+=self.name+'\n'
		tabs=1
		msg=self.node.muestra(msg,tabs)
		return msg

	def semantico(self):
		"""tV=[]	#tabla de variables
		tF=[]	#tabla de funciones
		ambito=""
		self.node.semantico(tF,tV,ambito)#pasar tabla por parametro en cada uno"""
		tablaSim=TablaSimbolos()
		self.node.semantico(tablaSim)
		tablaSim.printTables()
		return tablaSim

	def codeGen(self):
		code=CodigoGenerado()
		self.node.codeGen(code)
		return code



class Rule2(Node):
	def __init__(self,pila):
		self.name="R2"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg
	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass


class Rule3(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.id2=pila.pop()
		self.name="R3"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id2.semantico(tablaSim)
		self.id1.semantico(tablaSim)

	def codeGen(self,code):
		self.id2.codeGen(code)
		self.id1.codeGen(code)
		


class Rule4(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		self.name="R4"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule5(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		self.name="R5"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule6(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#;
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.idn=pila.pop()
		pila.pop()
		self.tipo=pila.pop()
		self.name="R6"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=self.tipo+'\n'
		for i in range(tabs):
			msg+='  |'
		msg+=self.idn+'\n'
		msg=self.id1.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+=';\n'
		return msg
	def semantico(self,tablaSim):
		"""sv=SimboloVariable(tipo,idn,ambito)
		for i in tV:
			if i.get_Name()==sv.get_Name():
				if i.get_Ambito()==sv.get_Ambito():
					return "Var"
		tV.add(sv)
		self.id1.semantico()"""
		sv=SimboloVariable(self.tipo,self.idn,tablaSim.get_Ambito())
		if tablaSim.isInTablaVariables(sv):
			tablaSim.add_Error("Variable: "+self.idn+" redefinida")
		else:
			tablaSim.add_tablaVariables(sv)
		tablaSim.set_TipoAnterior(self.tipo)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)



class Rule7(Node):
	def __init__(self,pila):
		self.name="R7"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg
	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass



class Rule8(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.idn=pila.pop()
		pila.pop()
		pila.pop()		#,
		self.name="R8"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=',\n'
		for i in range(tabs):
			msg+='  |'
		msg+=self.idn+'\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.sv=SimboloVariable(tablaSim.get_TipoAnterior(),self.idn,tablaSim.get_Ambito())
		if tablaSim.isInTablaVariables(self.sv):
			tablaSim.add_Error("Variable: "+self.idn+" redefinida")
		else:
			tablaSim.add_tablaVariables(self.sv)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule9(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#)
		pila.pop()
		self.id2=pila.pop()
		pila.pop()
		pila.pop()		#(
		pila.pop()
		self.idn=pila.pop()
		pila.pop()
		self.tipo=pila.pop()
		self.name="R9"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=self.tipo+'\n'
		for i in range(tabs):
			msg+='  |'
		msg+=self.idn+'\n'
		for i in range(tabs):
			msg+='  |'
		msg+='(\n'
		msg=self.id2.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+=')\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		sf=SimboloFuncion(self.tipo,self.idn)
		if tablaSim.isIntablaFunciones(sf):
			tablaSim.add_Error("Funcion: "+self.idn+" redefinida")
		else:
			tablaSim.add_tablaFunciones(sf)
		tablaSim.cambia_Ambito(self.idn)
		self.id2.semantico(tablaSim)
		self.id1.semantico(tablaSim)
		tablaSim.cambia_Ambito("")
	def codeGen(self,code):
		self.id2.codeGen(code)
		self.id1.codeGen(code)


class Rule10(Node):
	def __init__(self,pila):
		self.name="R10"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg

	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass


class Rule11(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.idn=pila.pop()
		pila.pop()
		self.tipo=pila.pop()
		self.name="R11"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=self.tipo+'\n'
		for i in range(tabs):
			msg+='  |'
		msg+=self.idn+'\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		sv=SimboloVariable(self.tipo,self.idn,tablaSim.get_Ambito())
		if tablaSim.isInTablaVariables(sv):
			tablaSim.add_Error("Variable: "+self.idn+" redefinida")
		else:
			tablaSim.add_tablaVariables(sv)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule12(Node):
	def __init__(self,pila):
		self.name="R12"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg

	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass


class Rule13(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.idn=pila.pop()
		pila.pop()
		self.tipo=pila.pop()
		pila.pop()
		pila.pop()		#,
		self.name="R13"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=',\n'
		for i in range(tabs):
			msg+='  |'
		msg+=self.tipo+'\n'
		for i in range(tabs):
			msg+='  |'
		msg+=self.idn+'\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		sv=SimboloVariable(self.tipo,self.idn,tablaSim.get_Ambito())
		if tablaSim.isInTablaVariables(sv):
			tablaSim.add_Error("Variable: "+self.idn+" redefinida")
		else:
			tablaSim.add_tablaVariables(sv)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule14(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#}
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#{
		self.name="R14"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+='{\n'
		msg=self.id1.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+='}\n'
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule15(Node):
	def __init__(self,pila):
		self.name="R15"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg

	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass



class Rule16(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.id2=pila.pop()
		self.name="R16"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id2.semantico(tablaSim)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id2.codeGen(code)
		self.id1.codeGen(code)


class Rule17(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		self.name="R17"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule18(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		self.name="R18"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule19(Node):
	def __init__(self,pila):
		self.name="R19"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg

	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass


class Rule20(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.id2=pila.pop()
		self.name="R20"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id2.semantico(tablaSim)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id2.codeGen(code)
		self.id1.codeGen(code)


class Rule21(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#;
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#=
		pila.pop()
		self.idn=pila.pop()
		self.name="R21"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=self.idn+'\n'
		for i in range(tabs):
			msg+='  |'
		msg+='=\n'
		msg=self.id1.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+=';\n'
		return msg

	def semantico(self,tablaSim):
		sv=SimboloVariable("",self.idn,tablaSim.get_Ambito())
		if (not tablaSim.isInTablaVariables(sv)):
			tablaSim.add_Error("Variable: "+self.idn+" No Declarada")
		tipo1=tablaSim.get_TipoVariable(self.idn)
		print(tipo1.get_Tipo())
		tipo2=self.id1.semantico(tablaSim)
		if tipo1.get_Tipo()!=tipo2.get_Tipo():
			try:
				n1=tipo1.get_Nombre()
			except:
				n1=tipo1.get_Ambito()
			try:
				n2=tipo2.get_Nombre()
			except:
				n2=tipo2.get_Ambito()
			tablaSim.add_Error(n1+" y "+n2+" son incompatibles "+tipo1.get_Tipo()+","+tipo2.get_Tipo())
	def codeGen(self,code):
		num=self.id1.codeGen(code)
		code.addLine("mov DWORD ["+self.idn+"],"+num+"\n")

class Rule22(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.id2=pila.pop()
		pila.pop()
		pila.pop()		#)
		pila.pop()
		self.id3=pila.pop()
		pila.pop()
		pila.pop()		#(
		pila.pop()
		pila.pop()		#if
		self.name="R22"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+='if(\n'
		msg=self.id3.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+=')\n'
		msg=self.id2.muestra(msg,tabs)
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id3.semantico(tablaSim)
		self.id2.semantico(tablaSim)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id3.codeGen(code)
		self.id2.codeGen(code)
		self.id1.codeGen(code)


class Rule23(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#)
		pila.pop()
		self.id2=pila.pop()
		pila.pop()
		pila.pop()		#(
		pila.pop()
		pila.pop()		#while
		self.name="R23"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+='while(\n'
		msg=self.id2.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+=')\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id2.semantico(tablaSim)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id2.codeGen(code)
		self.id1.codeGen(code)


class Rule24(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#;
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#return
		self.name="R24"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+='return\n'
		msg=self.id1.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+=';\n'
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)

class Rule25(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#;
		pila.pop()
		self.id1=pila.pop()
		self.name="R25"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+=';\n'
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule26(Node):
	def __init__(self,pila):
		self.name="R26"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg

	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass


class Rule27(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#else
		self.name="R27"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+='else\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)

class Rule28(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#}
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#{
		self.name="R28"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+='{\n'
		msg=self.id1.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+='}\n'
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)

class Rule29(Node):
	def __init__(self,pila):
		self.name="R29"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg

	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass



class Rule30(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		self.name="R30"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule31(Node):
	def __init__(self,pila):
		self.name="R31"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg

	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass


class Rule32(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.id2=pila.pop()
		self.name="R32"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id2.semantico(tablaSim)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id2.codeGen(code)
		self.id1.codeGen(code)


class Rule33(Node):
	def __init__(self,pila):
		self.name="R33"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		return msg

	def semantico(self,tablaSim):
		pass
	def codeGen(self,code):
		pass


class Rule34(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		self.id2=pila.pop()
		pila.pop()
		pila.pop()		#,
		self.name="R34"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=',\n'
		msg=self.id2.muestra(msg,tabs)
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id2.semantico(tablaSim)
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id2.codeGen(code)
		self.id1.codeGen(code)


class Rule35(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		self.name="R35"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		return self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)
		


class Rule36(Node):
	def __init__(self,pila):
		pila.pop()
		self.idn=pila.pop()
		self.name="R36"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=self.idn+'\n'
		return msg

	def semantico(self,tablaSim):
		sv=SimboloVariable("",self.idn,tablaSim.get_Ambito())
		if not tablaSim.isInTablaVariables(sv):
			tablaSim.add_Error("Variable: "+self.idn+" No Declarada")
		return tablaSim.get_TipoVariable(self.idn)
	def codeGen(self,code):
		return "DWORD ["+self.idn+"]"



class Rule37(Node):
	def __init__(self,pila):
		pila.pop()
		self.ent=pila.pop()
		self.name="R37"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=self.ent+'\n'
		return msg

	def semantico(self,tablaSim):
		v=SimboloVariable("int",self.ent,"")
		return v
	def codeGen(self,code):
		return self.ent
		


class Rule38(Node):
	def __init__(self,pila):
		pila.pop()
		self.real=pila.pop()
		self.name="R38"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=self.real+'\n'
		return msg

	def semantico(self,tablaSim):
		v=SimboloVariable("float",self.real,"")
		return v
	def codeGen(self,code):
		return self.real


class Rule39(Node):
	def __init__(self,pila):
		pila.pop()
		self.cadena=pila.pop()
		self.name="R39"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=self.cadena+'\n'
		return msg

	def semantico(self,tablaSim):
		v=SimboloVariable("string",self.cadena,"")
		return v
	def codeGen(self,code):
		pass


class Rule40(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#)
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#(
		pila.pop()
		self.idn=pila.pop()
		self.name="R40"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+=self.idn+'(\n'
		msg=self.id1.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+=')\n'
		return msg

	def semantico(self,tablaSim):
		sf=SimboloFuncion("",self.idn)
		if not tablaSim.isIntablaFunciones(sf):
			tablaSim.add_Error("Funcion: "+self.idn+" No Declarada")
		self.id1.semantico(tablaSim)
		return tablaSim.get_TipoFuncion(self.idn)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule41(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		self.name="R41"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule42(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		self.name="R42"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule43(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#)
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#(
		self.name="R43"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+='(\n'
		msg=self.id1.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+=')\n'
		return msg

	def semantico(self,tablaSim):
		return self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)



class Rule44(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#opSuma
		self.name="R44"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+='opSuma\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		return self.id1.semantico(tablaSim)
	def codeGen(self,code):
		return self.id1.codeGen(code)


class Rule45(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#opNot
		self.name="R45"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		for i in range(tabs):
			msg+='  |'
		msg+='opNot\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		return self.id1.semantico(tablaSim)
	def codeGen(self,code):
		self.id1.codeGen(code)


class Rule46(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#opMul
		pila.pop()
		self.id2=pila.pop()
		self.name="R46"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+='opMul\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		tipo1=self.id2.semantico(tablaSim)
		tipo2=self.id1.semantico(tablaSim)
		if tipo1.get_Tipo()!=tipo2.get_Tipo():
			try:
				n1=tipo1.get_Name()
			except:
				n1=tipo1.get_Ambito()
			try:
				n2=tipo1.get_Name()
			except:
				n2=tipo1.get_Ambito()
			tablaSim.add_Error(n1+" y "+n2+" son incompatibles "+tipo1.get_Tipo()+","+tipo2.get_Tipo())
			v=SimboloVariable("","","")
			return v
		return tipo1


class Rule47(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#opSuma
		pila.pop()
		self.id2=pila.pop()
		self.name="R47"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+='opSuma\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		tipo1=self.id2.semantico(tablaSim)
		tipo2=self.id1.semantico(tablaSim)
		if tipo1.get_Tipo()!=tipo2.get_Tipo():
			try:
				n1=tipo1.get_Nombre()
			except:
				n1=tipo1.get_Ambito()
			try:
				n2=tipo1.get_Nombre()
			except:
				n2=tipo1.get_Ambito()
			tablaSim.add_Error(n1+" y "+n2+" son incompatibles "+tipo1.get_Tipo()+","+tipo2.get_Tipo())
			v=SimboloVariable("","","")
			return v
		return tipo1
	def codeGen(self,code):
		dato1=self.id2.codeGen(code)
		dato2=self.id1.codeGen(code)
		code.addLine("mov eax,"+dato1+"\n")
		code.addLine("mov ebx,"+dato2+"\n")
		code.addLine("add eax,ebx"+"\n")
		return "eax"



class Rule48(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#opMRelac
		pila.pop()
		self.id2=pila.pop()
		self.name="R48"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+='opMRelac\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		tipo1=self.id2.semantico(tablaSim)
		tipo2=self.id1.semantico(tablaSim)
		if tipo1.get_Tipo()!=tipo2.get_Tipo():
			try:
				n1=tipo1.get_Nombre()
			except:
				n1=tipo1.get_Ambito()
			try:
				n2=tipo2.get_Nombre()
			except:
				n2=tipo2.get_Ambito()
			tablaSim.add_Error(n1+" y "+n2+" son incompatibles "+tipo1.get_Tipo()+","+tipo2.get_Tipo())
			v=SimboloVariable("","","")
			return v
		return tipo1


class Rule49(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#opIgualdad
		pila.pop()
		self.id2=pila.pop()
		self.name="R49"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+='opIgualdad\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		tipo1=self.id2.semantico(tablaSim)
		tipo2=self.id1.semantico(tablaSim)
		print(tipo.get_Tipo(),tipo2.get_Tipo())
		if tipo1.get_Tipo()!=tipo2.get_Tipo():
			try:
				n1=tipo1.get_Nombre()
			except:
				n1=tipo1.get_Ambito()
			try:
				n2=tipo2.get_Nombre()
			except:
				n2=tipo2.get_Ambito()
			tablaSim.add_Error(n1+" y "+n2+" son incompatibles "+tipo1.get_Tipo()+","+tipo2.get_Tipo())
			v=SimboloVariable("","","")
			return v
		return tipo1


class Rule50(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#opAnd
		pila.pop()
		self.id2=pila.pop()
		self.name="R50"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+='opAnd\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		tipo1=self.id2.semantico(tablaSim)
		tipo2=self.id1.semantico(tablaSim)
		if tipo1.get_Tipo()!=tipo2.get_Tipo():
			try:
				n1=tipo1.get_Nombre()
			except:
				n1=tipo1.get_Ambito()
			try:
				n2=tipo2.get_Nombre()
			except:
				n2=tipo2.get_Ambito()
			tablaSim.add_Error(n1+" y "+n2+" son incompatibles "+tipo1.get_Tipo()+","+tipo2.get_Tipo())
			v=SimboloVariable("","","")
			return v
		return tipo1


class Rule51(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		pila.pop()
		pila.pop()		#opOr
		pila.pop()
		self.id2=pila.pop()
		self.name="R51"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id2.muestra(msg,tabs)
		for i in range(tabs):
			msg+='  |'
		msg+='opOr\n'
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		tipo1=self.id2.semantico(tablaSim)
		tipo2=self.id1.semantico(tablaSim)
		if tipo1.get_Tipo()!=tipo2.get_Tipo():
			try:
				n1=tipo1.get_Nombre()
			except:
				n1=tipo1.get_Ambito()
			try:
				n2=tipo2.get_Nombre()
			except:
				n2=tipo2.get_Ambito()
			tablaSim.add_Error(n1+" y "+n2+" son incompatibles "+tipo1.get_Tipo()+","+tipo2.get_Tipo())
			v=SimboloVariable("","","")
			return v
		return tipo1


class Rule52(Node):
	def __init__(self,pila):
		pila.pop()
		self.id1=pila.pop()
		self.name="R52"
	def muestra(self,msg,tabs):
		for i in range(tabs):
			msg+='  |'
		msg+=self.name+'\n'
		tabs+=1
		msg=self.id1.muestra(msg,tabs)
		return msg

	def semantico(self,tablaSim):
		return self.id1.semantico(tablaSim)
	def codeGen(self,code):
		return self.id1.codeGen(code)