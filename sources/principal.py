import pygame
from pygame.locals import *
import sys
import fondo
from fondo import *
import Jugador
from Jugador import *
from Menu import *
ALTO= 600   #Alto de la pantalla
ANCHO= 1000 #Ancho de la pantalla
V=1 #VELOCIDAD CON LA QUE SE VA MOVER ErN EL MAPA

def inicio(pantalla,X_Screen,Y_Screen):
	Inicio=pygame.image.load("Img/Intro/inicio5.png")
	pantalla.blit(Inicio,(X_Screen,Y_Screen))
	pygame.display.flip()

	while True:
		tecla = pygame.key.get_pressed()
		tecla = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if tecla[K_RETURN]:
				menu(pantalla,X_Screen,Y_Screen)
				break


def menu(pantalla,X_Screen,Y_Screen):
	opcionEscogida=False
	menuJuego = Menu(ANCHO,ALTO)
	menuJuego.cargarImgMenu()
	pantalla.blit(menuJuego.obtenerImg(),(X_Screen,Y_Screen))
	pygame.display.flip()
	while True:
		tecla = pygame.key.get_pressed()
		tecla = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if tecla[K_DOWN]:
				menuJuego.flechaAbajo()
				imagen=menuJuego.obtenerImg()
				pantalla.blit(imagen,(0,0))
				pygame.display.flip()
			if tecla[K_UP]:
				menuJuego.flechaArriba()
				imagen=menuJuego.obtenerImg()
				pantalla.blit(imagen,(0,0))
				pygame.display.flip()
			if tecla[K_RETURN]:
				if(menuJuego.OpcionActual==0):
					dibujarNuevoJuego(pantalla,X_Screen,Y_Screen)
					print"jfdgkhfdg"			
			#dibujarNuevoJuego(pantalla,X_Screen,Y_Screen)


	


def dibujarNuevoJuego(pantalla,X_Screen,Y_Screen):	
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
	#creo un objeto jugador
	jugadorP=Jugador()

	jug=jugadorP.cargarSprites();
	jugadorP.image = jug[0]

	
	while True:	
		tecla = pygame.key.get_pressed()
		tecla = pygame.key.get_pressed()
		pantalla.blit(buffe.subsurface(X_Screen,Y_Screen,ANCHO,ALTO),(0,0))
		pantalla.blit(jugadorP.image,(jugadorP.x,jugadorP.y))
		pygame.display.flip()
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if tecla[K_RIGHT]:
				jugadorP.moverDerecha(jug)				
				if X_Screen == 3000:
					print "fdgdsfh"
				else:
					X_Screen = X_Screen+V
						
				print "holaaa"
			if tecla[K_DOWN]:
				jugadorP.moverAbajo(jug)				
				if Y_Screen == 3000:
					print "fdgdsfh"
				else:
					Y_Screen = Y_Screen+V
						
				print "holaaa"
			if tecla[K_UP]:
				jugadorP.moverArriba(jug)
				if Y_Screen == 0:
					print "fdgdsfh"
				else:
					Y_Screen = Y_Screen-V
			if tecla[K_LEFT]:
				jugadorP.moverIzquierda(jug)
				if X_Screen == 0:
					print "fdgdsfh"
				else:
					X_Screen = X_Screen-V
			#obtener la posicion del mouse cuando se da click en la pantalla
				
			if event.type== pygame.MOUSEBUTTONDOWN:	
				print "posicion X e Y "+str(pygame.mouse.get_pos()) 
	


def main():
	X_Screen=0  #Variable de posicion x del subsurface a mostrar en la pantalla
	Y_Screen=0  #Variable de posicion y del subsurface a mostrar en la pantalla	
	#creamos la pantalla  mi screen	
	pygame.init()
	pantalla = pygame.display.set_mode((ANCHO,ALTO)) 
	inicio(pantalla,X_Screen,Y_Screen)
	
	


if __name__ == '__main__':
	main()