import pygame
from pygame.locals import *
import sys
import fondo
from fondo import *
ALTO= 600   #Alto de la pantalla
ANCHO= 1000 #Ancho de la pantalla
V=30 #VELOCIDAD CON LA QUE SE VA MOVER EN EL MAPA


def main():
	X_Screen=0  #Variable de posicion x del subsurface a mostrar en la pantalla
	Y_Screen=0  #Variable de posicion y del subsurface a mostrar en la pantalla
	pygame.init()
	#creamos la pantalla  mi screen	
	pantalla = pygame.display.set_mode((ANCHO,ALTO)) 
	pygame.display.set_caption("PUBLO DE KIBRA")	
	#creo un objeto de tipo fondo
	fondito=fondo()
	#creo un buffer  que va contener mi mapa 
	buffe=pygame.Surface((4000,4000))
	#creo una lista imagenes que va contener mis sprites
	sprites=fondito.cargarSprites("final3.png")	
	# dibujo mi buffer
	fondito.DrawPantalla(buffe,sprites)
	pantalla.blit(buffe.subsurface(X_Screen,Y_Screen,ANCHO,ALTO),(0,0))
	pygame.display.flip()
	
	while True:	
		tecla = pygame.key.get_pressed()
		tecla = pygame.key.get_pressed()
		pantalla.blit(buffe.subsurface(X_Screen,Y_Screen,ANCHO,ALTO),(0,0))
		pygame.display.flip()	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if tecla[K_RIGHT]:				
				if X_Screen == 3000:
					print "fdgdsfh"
				else:
					X_Screen = X_Screen+V
						
				print "holaaa"
			if tecla[K_DOWN]:				
				if Y_Screen == 3000:
					print "fdgdsfh"
				else:
					Y_Screen = Y_Screen+V
						
				print "holaaa"
			if tecla[K_UP]:
				if Y_Screen == 0:
					print "fdgdsfh"
				else:
					Y_Screen = Y_Screen-V
			if tecla[K_LEFT]:
				if X_Screen == 0:
					print "fdgdsfh"
				else:
					X_Screen = X_Screen-V
		
	



if __name__ == '__main__':
	main()