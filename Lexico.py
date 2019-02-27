class Lexico(object):
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
					state=3
			elif state==1:
				if (c<'0' or c>'9'):
					state=3
				if c=='.':
					state=2
			elif state==2:
				if (c<'0' or c>'9'):
					state=3
				else:
					state=4
			elif state==4:
				if (c<'0' or c>'9'):
					state=3
			if (state==3):
				break
		if state==1:
			self.id=1
			return True
		if (state ==3):
			self.id=-1
			return False
		if state==4:
			self.id=2
			return True	

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
			self.id=-1
		if self.id!=-1:
			return True
		else:
			return False


	def is_ID(self):
		src=self.__source
		if src=="":
			self.id=-1
			return False
		if((src[0] < 'a' or src[0] > 'z') and (src[0] < 'A' or src[0] > 'Z')):
			self.id=-1
			return False
		else:
			for c in src:
				if((c < 'a' or c > 'z') and (c < 'A' or c > 'Z') and (c < '0' or c > '9') and c != '_'):
					self.id=-1
					return False
			self.id=0
			return True

	def analysis(self):
		parte=""
		state=0
		copia=self.__source
		i=0
		state=0
		while i<len(copia):
			c=copia[i]
			parte+=c
			print parte,state,self.id
			self.__source=parte
			if state==0:
				if self.is_ID():
					state=1
				if self.is_Reserved():
					state=3
					i=i-1
				elif self.is_Number():
					state=5
				elif (c==' '  or c=='\t' or c=='\n'):
					state=0
					parte=""
			elif state==1:
				if self.is_ID():
					state=1
				if self.is_Reserved():
					state=2
					i=i-1
					print "hola"
				elif (c==' '  or c=='\t' or c=='\n'):
					state=2
					i=i-1
				else:
					cid=self.id
					self.__source=c
					if self.is_Reserved():
						state=2
						if anterior==1:
							self.id=0
						else:
							self.id=cid
						print self.id
						self.addMsg()
						self.addID()
						self.is_Reserved()
						parte=""
						i=i-1

			elif state==2:
				if self.id==7:
					c=copia[i+1]
					if c=='=':
						i=i+1
				print self.id
				self.addMsg()
				self.addID()
				parte=""
				state=0

			elif state==3:
				if self.id==7:
					c=copia[i+1]
					if c=='=':
						i=i+1
				print self.id
				self.addMsg()
				self.addID()
				parte=""
				state=0

			elif state==4:
				if ~is_Number():
					if c!='.':
						state=5
				cid=self.id
				self.__source=c
				if self.is_Reserved():
					state=2
					self.id=cid
					print self.id
					self.addMsg()
					self.addID()
					self.is_Reserved()
					parte=""
					i=i-1
			elif state==5:
				self.id=-1
				print self.id
				self.addMsg()
				self.addID()
				break;
			i+=1
			anterior=state



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