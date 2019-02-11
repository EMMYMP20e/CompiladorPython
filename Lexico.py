class Lexico(object):
	#source=""
	
	#id=0
	
	#message=[""]
	def __init__(self):
		self.source=""
		self.id=0
		self.message=[""]
	def set_source(self,source):
		self.__source=source
	def set_message(self,message):
		self.__message=message

	def get_source(self):
		return self.__source
	def get_message(self):
		return self.message

	def is_Number(self):
		state=0
		for c in self.__source:
			if state==0:
				if (c>=0 and c<=9):
					state=1
				else:
					state=7

			elif state==1:
				if (c<0 or c>9):
					state=6
				elif c=='.':
					state=2

			elif state==2:
				if (c<0 or c>9):
					state=3
				else:
					state=4

			elif state==4:
				if (c<0 or c>9):
					state=5
				elif (c=='.'):
					state=3
			if (state==3 or state ==5 or state ==6 or state==7):
				break
		if state==1:
			id=1
		if (state ==3 or state==7):
			id=-1
		if state==4:
			id=2
		if state==5:
			id=-2
		if state==6:
			id=-3
	def is_Reserved(self):
		if (source == "+" or source == "-"):
			id = 5
		elif (source == "*" or source == "/"):
			id = 6;
		elif (source == "="):
			id = 18;
		elif (source == "<" or source == ">" or source == "<=" or source == ">="):
			id = 7;
		elif (source == "&&"):
			id = 9;
		elif (source == "||"):
			id = 8;
		elif (source == "!"):
			id = 10;
		elif (source == "("):
			id = 14;
		elif (source == ")"):
			id = 15;
		elif (source == "{"):
			id = 16;
		elif (source == "}"):
			id = 17;
		elif (source == ";"):
			id = 12;
		elif (source == ","):
			id = 13;
		elif (source == "int" or source == "float" or source == "void"):
			id = 4;
		elif (source == "string"):
			id = 3;
		elif (source == "if"):
			id = 19;
		elif (source == "while"):
			id = 20;
		elif (source == "return"):
			id = 21;
		elif (source == "else"):
			id = 22;
		elif (source == "$"):
			id = 23;
		else:
			id = -1;

	def is_ID(self):
		if((source[0] < 'a' or source[0] > 'z') and (source[0] < 'A' or source[0] > 'Z')):
			id=-1
		else:
			for c in source:
				if((c < 'a' or c > 'z') and (c < 'A' or c > 'Z') and (c < '0' or c > '9') and c != '_'):
					id=-1
					break
			id=0

	def analysis(self):
		parte=""
		copia=self.__source
		global id
		for c in copia:
			parte+=c
			source=parte
			if c==' ':
				parte=""
				if(id>=0 and id<=2):
					addMsg()
			self.is_Number()
			if(id==-2 or id==-3):
				if id==-2:
					id=2
				if id==-3:
					id=1
				parte=""+c
				source=parte
				self.addMsg()
				id=-1
			if id==-1:
				is_Reserved()
				if id==-1:
					is_ID()
			if id>=3:
				parte=""
				source==parte
				self.addMsg()
		if(id>=0 and id<=2):
			self.addMsg()



	def addMsg(self):
		if id==-1:
			message.append("Error Lexico, ")
		elif id==0:
			message.append("Identificador, ")
		elif id==1:
			message.append("Numero entero, ")
		elif id==2:
			message.append("Numero real, ")
		elif id==3:
			message.append("Cadena, ")
		elif id==4:
			message.append("Tipo de dato, ")
		elif id==5:
			message.append("Operador de adicion, ")
		elif id==6:
			message.append("Operador de multiplicaion, ")
		elif id==7:
			message.append("Operador Relacional, ")
		elif id==8:
			message.append("Operador Or, ")
		elif id==9:
			message.append("Operador And, ")
		elif id==10:
			message.append("Operador Not, ")
		elif id==11:
			message.append("Operador de Igualdad, ")
		elif id==12:
			message.append("Simbolo Punto y coma, ")
		elif id==13:
			message.append("Simbolo Coma, ")
		elif (id == 14 or id == 15):
			message.append("Simbolo Parentesis, ")
		elif (id == 16 or id == 17):
			message.append("Simbolo Llave, ")
		elif id==18:
			message.append("Operador de Asignacion, ")
		elif id==19:
			message.append("Condicional if, ")
		elif id==20:
			message.append("Ciclo whie, ")
		elif id==21:
			message.append("Retorno de valor, ")
		elif id==22:
			message.append("Condicional else, ")
		elif id==23:
			message.append("Simbolo $, ")




		