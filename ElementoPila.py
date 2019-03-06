class ElementoPila(object):
	def __init__(self,ind,name):
		self.ind=ind
		self.name=name
	def __str__(self):
		return "%s"%(self.name)
class Terminal(ElementoPila):
	def __init__(self,ind,name)
		