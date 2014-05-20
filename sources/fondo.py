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
		self.NumSprites=969

	def cargarSprites(self,VectorImagenes):
				
		imagen=pygame.image.load(VectorImagenes).convert()
		listaSprites=[]
		for i in range(0,self.NumSprites):
			listaSprites.append(imagen.subsurface((i*self.AnchoTile,0,self.AnchoTile,self.AltoTile)))
		return listaSprites

	def cargarMatriz(self): #Aqui se va a cargar la matriz del archivo de texto
		archivo = csv.reader(open('mundo1.csv', 'rb'))
		matriz = []
		#creo una matrz de AnchoMatrizTiles X AltoMatrizTiles
		for i,row in enumerate(archivo):
			matriz.append(row)			
		return matriz
	def DrawMatriz(self,listasSprites):#aqui pinto mi matriz
		MatrizCaracteres=self.cargarMatriz()
		print "valor"+str(MatrizCaracteres[0][0])
		for i in range(0,self.AltoMatrizTiles):
			for j in range (0,self.AnchoMatrizTiles):
				valorVect=int(MatrizCaracteres[i][j])-1	
				#print 	MatrizCaracteres[i][j]		
				MatrizCaracteres[i][j]=listasSprites[int(valorVect)]
		return MatrizCaracteres


	def DrawPantalla(self,buffe,listasSprites):
		MatrizDraw=self.DrawMatriz(listasSprites)

		for i in range(0,self.AltoMatrizTiles):
			for j in range (0,self.AnchoMatrizTiles):
				buffe.blit(MatrizDraw[i][j],(j*self.AnchoTile,i*self.AltoTile))
				#pantalla.blit(listasSprites[j],(j*self.AnchoTile,0))
	
		


