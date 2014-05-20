import pygame
from pygame.locals import *
import sys
import fondo
from fondo import *
ALTO= 1000
ANCHO= 1000

def main():
	pygame.init()
	#creamos la pantalla  mi screen	
	pantalla = pygame.display.set_mode((ANCHO,ALTO)) 
	pygame.display.set_caption("PUBLO DE KIBRA")	
	#creo un objeto de tipo fondo
	fondito=fondo()
	#creo un buffer  que va contener mi mapa 
	buffe=pygame.Surface((2000,2000))
	#creo una lista imagenes que va contener mis sprites
	sprites=fondito.cargarSprites("final3.png")	
	# dibujo mi buffer
	fondito.DrawPantalla(buffe,sprites)
	pantalla.blit(buffe.subsurface(400,0,800,800),(0,0))
	pygame.display.flip()
	while True:		
		pygame.display.flip()	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
	



if __name__ == '__main__':
	main()