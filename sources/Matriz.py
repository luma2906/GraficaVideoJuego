
from Cuadro import *
class Matriz:
	"""self.typ=tipo
		self.valor=valor
		self.posicion_x=posicion_x
		self.posicion_y=posicion_y
		self.obstaculo=obstaculo"""
	
	def __init__(self, tam_x, tam_y, matriz):
		print "--------------------ENTRA AL CONSTRUCTOR"
		self.tam_x=tam_x
		self.tam_y=tam_y
		self.lista=[]		
		self.valorObstaculo=2
		self.BuscarMatriz(matriz)

		
	def BuscarMatriz(self,matriz):
		n=0
		print "Tamx = "+str(self.tam_x)+" tamy = "+str(self.tam_y)
		for i in range(0, self.tam_y):
			for j in range(0,self.tam_x):
				valor=matriz[i][j]
				posicion_x=j
				posicion_y=i
				print valor
				if valor == 2:
					print "Entra a obstaculo"
					obstaculo=True
					peso=500
				else:
					obstaculo=False
				if (i==0 and j==0) or (i==self.tam_y-1 and j==self.tam_x-1 )or(i==0 and j==self.tam_x-1)or(i==self.tam_y-1 and j==0):
					typ="esquina"
				elif i==0 and j!= 0:
					typ="superior"
				elif i!=0 and j==0:
					typ="izquierda"
				elif i!=self.tam_y-1 and j== self.tam_x-1:
					typ="derecha"
				elif i==self.tam_y-1 and j!= self.tam_x-1:
					typ="inferior"
				else:
					typ="centro"
				cuadrito=Cuadro(typ,valor,posicion_x,posicion_y,obstaculo)
				self.cargarMatriz (self.lista,cuadrito)


	def cargarMatriz(self,lista,cuadrito):
		self.lista.append(cuadrito)

	def get_lista(self):
		return self.lista
	
	def get_tam_x(self):
		return self.tam_x

	def get_tam_y(self):
		return self.tam_y
		

		

					
		