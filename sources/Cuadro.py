class Cuadro:
	'''contructor'''
	def __init__(self,tipo,valor,posicion_x, posicion_y,obstaculo):
		self.typ=tipo
		self.valor=valor
		self.posicion_x=posicion_x
		self.posicion_y=posicion_y
		self.obstaculo=obstaculo
		self.peso=1
	def get_typ(self):
		return self.typ

	def get_valor(self):
		return self.valor

	def get_posicion_x(self):
		return self.posicion_x

	def get_posicion_y(self):
		return self.posicion_y

	def get_obstaculo(self):
		return self.obstaculo

	def get_peso(self):
		return self.peso
	
	
		
		