import pygame
from pygame.locals import *
import sys
import pygame.locals
import csv
class fondo:
	#constructor
	def __init__(self):
		self.AnchoMatrizTiles=250
		self.AltoMatrizTiles=250
		self.AnchoTile=16
		self.AltoTile=16

	def cargarSprites(self,VectorImagenes):
				
		imagen=pygame.image.load(VectorImagenes).convert()
		listaSprites=[]
		for i in range(0,968):
			listaSprites.append(imagen.subsurface((i*16,0,16,16)))
		return listaSprites

	def cargarMatriz(self): #Aqui se va a cargar la matriz del archivo de texto
		archivo = csv.reader(open('mundo1.csv', 'rb'))
		matriz = []
		#creo una matrz de AnchoMatrizTiles X AltoMatrizTiles
		for i,row in enumerate(archivo):
			matriz.append(row)

			
		


