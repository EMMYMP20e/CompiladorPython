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


class Rule2(Node):
	def __init__(self,pila):
		self.name="R2"


class Rule3(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		id2=pila.pop()
		self.name="R3"


class Rule4(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		self.name="R4"


class Rule5(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		self.name="R5"


class Rule6(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#;
		pila.pop()
		id1=pila.pop()
		pila.pop()
		idn=pila.pop()
		pila.pop()
		tipo=pila.pop()
		self.name="R6"


class Rule7(Node):
	def __init__(self,pila):
		self.name="R7"


class Rule8(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		idn=pila.pop()
		pila.pop()
		pila.pop()		#,
		self.name="R8"


class Rule9(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#)
		pila.pop()
		id2=pila.pop()
		pila.pop()
		pila.pop()		#(
		pila.pop()
		idn=pila.pop()
		pila.pop()
		tipo=pila.pop()
		self.name="R9"


class Rule10(Node):
	def __init__(self,pila):
		self.name="R10"


class Rule11(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		idn=pila.pop()
		pila.pop()
		tipo=pila.pop()
		self.name="R11"


class Rule12(Node):
	def __init__(self,pila):
		self.name="R12"


class Rule13(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		idn=pila.pop()
		pila.pop()
		tipo=pila.pop()
		pila.pop()
		pila.pop()		#,
		self.name="R13"


class Rule14(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#}
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#{
		self.name="R14"


class Rule15(Node):
	def __init__(self,pila):
		self.name="R15"


class Rule16(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		id2=pila.pop()
		self.name="R16"


class Rule17(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		self.name="R17"


class Rule18(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		self.name="R18"


class Rule19(Node):
	def __init__(self,pila):
		self.name="R19"


class Rule20(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		id2=pila.pop()
		self.name="R20"


class Rule21(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#;
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#=
		pila.pop()
		idn=pila.pop()
		self.name="R21"


class Rule22(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		id2=pila.pop()
		pila.pop()
		pila.pop()		#)
		pila.pop()
		id3=pila.pop()
		pila.pop()
		pila.pop()		#(
		pila.pop()
		pila.pop()		#if
		self.name="R22"


class Rule23(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#)
		pila.pop()
		id2=pila.pop()
		pila.pop()
		pila.pop()		#(
		pila.pop()
		pila.pop()		#while
		self.name="R23"


class Rule24(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#;
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#return
		self.name="R24"

class Rule25(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#;
		pila.pop()
		id1=pila.pop()
		self.name="R25"


class Rule26(Node):
	def __init__(self,pila):
		self.name="R26"


class Rule27(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#else
		self.name="R27"


class Rule28(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#}
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#{
		self.name="R28"

class Rule29(Node):
	def __init__(self,pila):
		self.name="R29"


class Rule30(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		self.name="R30"


class Rule31(Node):
	def __init__(self,pila):
		self.name="R31"


class Rule32(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		id2=pila.pop()
		self.name="R32"


class Rule33(Node):
	def __init__(self,pila):
		self.name="R33"

class Rule34(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		id2=pila.pop()
		pila.pop()
		pila.pop()		#,
		self.name="R34"


class Rule35(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		self.name="R35"


class Rule36(Node):
	def __init__(self,pila):
		pila.pop()
		idn=pila.pop()
		self.name="R36"


class Rule37(Node):
	def __init__(self,pila):
		pila.pop()
		ent=pila.pop()
		self.name="R37"


class Rule38(Node):
	def __init__(self,pila):
		pila.pop()
		real=pila.pop()
		self.name="R38"


class Rule39(Node):
	def __init__(self,pila):
		pila.pop()
		cadena=pila.pop()
		self.name="R39"


class Rule40(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#)
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#(
		pila.pop()
		idn=pila.pop()
		self.name="R40"


class Rule41(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		self.name="R41"


class Rule42(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		self.name="R42"


class Rule43(Node):
	def __init__(self,pila):
		pila.pop()
		pila.pop()		#)
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#(
		self.name="R43"


class Rule44(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#opSuma
		self.name="R44"


class Rule45(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#opNot
		self.name="R45"


class Rule46(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#opMul
		pila.pop()
		id2=pila.pop()
		self.name="R46"


class Rule47(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#opSuma
		pila.pop()
		id2=pila.pop()
		self.name="R47"


class Rule48(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#opMRelac
		pila.pop()
		id2=pila.pop()
		self.name="R48"


class Rule49(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#opIgualdad
		pila.pop()
		id2=pila.pop()
		self.name="R49"


class Rule50(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#opAnd
		pila.pop()
		id2=pila.pop()
		self.name="R50"


class Rule51(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		pila.pop()
		pila.pop()		#opOr
		pila.pop()
		id2=pila.pop()
		self.name="R51"


class Rule52(Node):
	def __init__(self,pila):
		pila.pop()
		id1=pila.pop()
		self.name="R52"