import pygame
from pygame.locals import *
class Menu:	
	def __init__(self,width,height):
		self.opciones = []
		self.pos_x=0
		self.pos_y=0
		self.WIDHT=width
		self.HEIGHT=height
		self.OpcionActual=0

	def cargarImgMenu(self):
		self.opciones.append(pygame.image.load("Img/Menu/menu1.png"))#Nuevo Juego
		self.opciones.append(pygame.image.load("Img/Menu/menu2.png"))#Cargar Juego
		self.opciones.append(pygame.image.load("Img/Menu/menu3.png"))#Historia
		self.opciones.append(pygame.image.load("Img/Menu/menu4.png"))#Controles

	def flechaArriba(self):
		if self.OpcionActual == 0:
			self.OpcionActual = 3
		else:
			self.OpcionActual = self.OpcionActual - 1
	
	def flechaAbajo(self):
		if self.OpcionActual == 3:
			self.OpcionActual = 0
		else:
			self.OpcionActual=self.OpcionActual + 1
	
	def obtenerImg(self):
		return self.opciones[self.OpcionActual]

	
		
		