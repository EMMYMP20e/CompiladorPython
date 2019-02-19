class Lexico(object):
	#source=""
	
	#id=0
	
	#message=[""]
	def __init__(self):
		self.source=""
		self.id=-1
		self.message=[""]
		self.ids=[]
	def set_source(self,source):
		self.__source=source
	def set_message(self,message):
		self.__message=message

	def get_source(self):
		return self.__source
	def get_message(self):
		return self.message
	def get_ids(self):
		return self.ids

	def is_Number(self):
		state=0
		for c in self.__source:
			if state==0:
				if (c>='0' and c<='9'):
					state=1
				else:
					state=7

			elif state==1:
				if (c<'0' or c>'9'):
					state=6
				if c=='.':
					state=2

			elif state==2:
				if (c<'0' or c>'9'):
					state=3
				else:
					state=4

			elif state==4:
				if (c<'0' or c>'9'):
					state=5
				if c=='.':
					state=3
			if (state==3 or state ==5 or state ==6 or state==7):
				break
		if state==1:
			self.id=1
		if (state ==3 or state==7):
			self.id=-1
		if state==4:
			self.id=2
		if state==5:
			self.id=-2
		if state==6:
			self.id=-3		

	def is_Reserved(self):
		src=self.__source
		if (src == "+" or src == "-"):
			self.id = 5
		elif (src == "*" or src == "/"):
			self.id = 6;
		elif (src == "="):
			self.id = 18;
		elif (src == "<" or src == ">" or src == "<=" or src == ">="):
			self.id = 7;
		elif (src == "&&"):
			self.id = 9;
		elif (src == "||"):
			self.id = 8;
		elif (src == "!"):
			self.id = 10;
		elif (src == "("):
			self.id = 14;
		elif (src == ")"):
			self.id = 15;
		elif (src == "{"):
			self.id = 16;
		elif (src == "}"):
			self.id = 17;
		elif (src == ";"):
			self.id = 12;
		elif (src == ","):
			self.id = 13;
		elif(src == "int" or src == "float" or src == "void"):
			self.id = 4;
		elif (src == "string"):
			self.id = 3;
		elif (src == "if"):
			self.id = 19;
		elif (src == "while"):
			self.id = 20;
		elif (src == "return"):
			self.id = 21;
		elif (src == "else"):
			self.id = 22;
		elif (src == "$"):
			self.id = 23;
		else:
			self.id = -1;

	def is_ID(self):
		src=self.__source
		if src=="":
			self.id=-1
			return
		if((src[0] < 'a' or src[0] > 'z') and (src[0] < 'A' or src[0] > 'Z')):
			self.id=-1
		else:
			for c in src:
				if((c < 'a' or c > 'z') and (c < 'A' or c > 'Z') and (c < '0' or c > '9') and c != '_'):
					self.id=-1
					return
			self.id=0

	def analysis(self):
		parte=""
		copia=self.__source
		for c in copia:
			parte+=c
			self.__source=parte
			if c==' ':
				parte=""
				if(self.id==0):#if(self.id>=0 and self.id<=2):
					self.addMsg()
					self.addID()
			self.is_Number()
			if(self.id==-2 or self.id==-3):
				if self.id==-2:
					self.id=2
				if self.id==-3:
					self.id=1
				parte=""#+c
				self.__source=parte
				self.addMsg()
				self.addID()
				self.id=-1
			if self.id==-1:
				self.is_Reserved()
				if self.id==-1:
					self.is_ID()
					if self.id==-1:
						self.__source=c
						self.is_Reserved()
						d=int(self.id)
						if self.id==-1:
							self.addMsg()
							self.addID()
						else:
							self.id=0
							self.addMsg()
							self.addID()
							self.id=d
							self.addMsg()
							self.addID()
							self.id=-1
						parte=""
			if self.id>=3:
				parte=""
				self.__source=parte
				self.addMsg()
				self.addID()

		if(self.id>=0 and self.id<=2):
			self.addMsg()
			self.addID()

	def addID(self):
		self.ids.append(self.id);

	def addMsg(self):
		if self.id==-1:
			self.message.append("Error Lexico, ")
		elif self.id==0:
			self.message.append("Identificador, ")
		elif self.id==1:
			self.message.append("Numero entero, ")
		elif self.id==2:
			self.message.append("Numero real, ")
		elif self.id==3:
			self.message.append("Cadena, ")
		elif self.id==4:
			self.message.append("Tipo de dato, ")
		elif self.id==5:
			self.message.append("Operador de adicion, ")
		elif self.id==6:
			self.message.append("Operador de multiplicacion, ")
		elif self.id==7:
			self.message.append("Operador Relacional, ")
		elif self.id==8:
			self.message.append("Operador Or, ")
		elif self.id==9:
			self.message.append("Operador And, ")
		elif self.id==10:
			self.message.append("Operador Not, ")
		elif self.id==11:
			self.message.append("Operador de Igualdad, ")
		elif self.id==12:
			self.message.append("Simbolo Punto y coma, ")
		elif self.id==13:
			self.message.append("Simbolo Coma, ")
		elif (self.id == 14 or self.id == 15):
			self.message.append("Simbolo Parentesis, ")
		elif (self.id == 16 or self.id == 17):
			self.message.append("Simbolo Llave, ")
		elif self.id==18:
			self.message.append("Operador de Asignacion, ")
		elif self.id==19:
			self.message.append("Condicional if, ")
		elif self.id==20:
			self.message.append("Ciclo while, ")
		elif self.id==21:
			self.message.append("Retorno de valor, ")
		elif self.id==22:
			self.message.append("Condicional else, ")
		elif self.id==23:
			self.message.append("Simbolo $, ")		