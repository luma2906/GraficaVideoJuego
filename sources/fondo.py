import pygame
from pygame.locals import *
import sys
import pygame.locals
class fondo:
	#constructor
	def __init__(self):
		self.x=0

	def cargarSprites(self,VectorImagenes):
				
		imagen=pygame.image.load(VectorImagenes).convert()
		listaSprites=[]
		for i in range(0,968):
			listaSprites.append(imagen.subsurface((i*16,0,16,16)))
		return listaSprites