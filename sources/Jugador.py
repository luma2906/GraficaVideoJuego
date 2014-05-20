import pygame
from pygame.locals import *
import sys
tamSpriteX=32
tamSpriteY=32	
class Jugador(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((32,32))
		self.rect = self.image.get_rect()
		self.x=395
		self.y=412
		self.Vel=5
		self.iterIzq=3
		self.iterDer=6
		self.iterArriba=9
		self.iterAbajo=0

	def cargarSprites(self):
		SpritesJugador=pygame.image.load("spriteadom.png")
		listaSpritesJugador=[]
		for i in range(0,13):
			listaSpritesJugador.append(SpritesJugador.subsurface(i*tamSpriteX,0,tamSpriteX,tamSpriteY))
		return listaSpritesJugador

	def moverIzquierda(self,sprites):
		self.x-=self.Vel
		self.image=sprites[self.iterIzq]
		if self.iterIzq ==5:
			self.iterIzq=3
		else:
			self.iterIzq+=1

	def moverDerecha(self,sprites):
		self.x+=self.Vel
		self.image=sprites[self.iterDer]
		if self.iterDer ==8:
			self.iterDer=6
		else:
			self.iterDer+=1
	def moverArriba(self,sprites):
		self.y-=self.Vel
		self.image=sprites[self.iterArriba]
		if self.iterArriba ==12: # Esta animacion consta de 4 sprites
			self.iterArriba=9
		else:
			self.iterArriba+=1
		
	def moverAbajo(self,sprites):
		self.y+=self.Vel
		self.image=sprites[self.iterAbajo]
		if self.iterAbajo ==2:
			self.iterAbajo=0
		else:
			self.iterAbajo+=1



		
		
	
		