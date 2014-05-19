import pygame
from pygame.locals import *
import sys
import fondo
from fondo import *
ALTO= 600
ANCHO= 600

def main():
	pygame.init()
	#creamos la pantalla
	pantalla = pygame.display.set_mode((ANCHO,ALTO)) 
	pygame.display.set_caption("PUBLO DE KIBRA")	
	fondito=fondo()
	sprites=fondito.cargarSprites("final3.png")	
	fondito.cargarMatriz()
	pantalla.blit(sprites[11],(30,10))
	pygame.display.flip()
	for imagen in sprites:
			pantalla.blit(imagen,(0,0))
	pygame.display.flip()
	while True:		
		pygame.display.flip()	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		




if __name__ == '__main__':
	main()