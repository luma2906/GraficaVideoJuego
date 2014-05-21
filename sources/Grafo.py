from Matriz import *
from collections import deque
class Grafo(object):
    def __init__(self):
        self.relaciones = {}
        self.pesos=0
    def __str__(self):
        return str(self.relaciones)
 
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2):
    relacionarUnilateral(grafo, elemento1, elemento2)
    relacionarUnilateral(grafo, elemento2, elemento1)
    print "Se relaciona "+str(elemento1.get_valor()) + " con "+str(elemento2.get_valor())
    
def relacionarUnilateral(grafo, origen, destino):
    grafo.relaciones[origen].append(destino)

def generarGrafo(mat):
	matriz = mat.get_lista()
	grafo = Grafo()
	filas = mat.tam_y
	columnas = mat.tam_x
	for i in range(0,filas):
		for j in range(0,columnas):
			pos = (i*columnas)+j 
			#print "Filas: "+str(filas) + " Columnas "+str(columnas)
			#print "El tamano de la lista es: "+str(len(matriz))+" y pos es: "+str(pos) + " i es: "+str(i) + " J es: "+str(j)
			cuadrito = matriz[pos]
			agregar(grafo,cuadrito)
	generarArcos(matriz,grafo,filas,columnas)
	return grafo

def generarArcos(matriz,grafo,filas,columnas):
	
	for i in range(0,filas):
		for j in range(0,columnas):
			#print " i: "+str(i) + "J : "+str(j) + "Matriz en 10 "+str(matriz[10].get_valor())
			pos = (i*columnas)+j
			posSig = (i*columnas)+(j+1)
			posAbajo = ((i+1)*columnas)+j 
			cuadroActual = matriz[pos]		
			#print "valorrrrr de iii"+str(i)
			
			if j!=columnas-1:
				cuadroSiguiente = matriz[posSig]
				relacionar(grafo,cuadroActual,cuadroSiguiente)
				#	print "SE CREO EL CUADRO SIGUIENTE"
			if i!=filas-1 and cuadroActual.typ!="inferior":
				#print "Cuadro Abajo con tipo"+ cuadroActual.typ
				cuadroAbajo = matriz[posAbajo]
				relacionar(grafo,cuadroActual,cuadroAbajo) 



def profundidadPrimero(grafo, elementoInicial, funcion, elementosRecorridos = []):
    if elementoInicial in elementosRecorridos:
        return
    funcion(elementoInicial)
    elementosRecorridos.append(elementoInicial)
    for vecino in grafo.relaciones[elementoInicial]:
        profundidadPrimero(grafo, vecino, funcion, elementosRecorridos)

def anchoPrimero(grafo, elementoInicial, funcion, cola = deque(), elementosRecorridos = []):
    if not elementoInicial in elementosRecorridos:
        funcion(elementoInicial)
        elementosRecorridos.append(elementoInicial)
        if(len(grafo.relaciones[elementoInicial]) > 0):
            cola.extend(grafo.relaciones[elementoInicial])
    if len(cola) != 0 :
        anchoPrimero(grafo, cola.popleft(), funcion, cola, elementosRecorridos) 

def imprimir (elemento):
    print elemento.get_valor()


# ------------------------------------------------BUSCAR EL MINIMO RECORRIDO CON dijkstra-----------------------------------------------------------
def caminoMinimo(grafo, origen, destino):
    etiquetas = {origen:(0,None)}
    dijkstra(grafo, destino, etiquetas, [])
    return construirCamino(etiquetas, origen, destino)

def construirCamino(etiquetas, origen, destino):	
	print "origen"+str(origen.get_valor()),"destio"+str(destino.get_valor())
	if origen == destino:
	    return [origen]
	return construirCamino(etiquetas, origen, anterior(etiquetas[destino])) + [destino]

    
def dijkstra(grafo, destino, etiquetas, procesados):	
	nodoActual = menorValorNoProcesado(etiquetas, procesados)	
	if nodoActual == destino: 	    return
	procesados.append(nodoActual)	
	for vecino in vecinoNoProcesado(grafo, nodoActual, procesados):		
		generarEtiqueta(grafo, vecino, nodoActual, etiquetas)	
	dijkstra(grafo, destino, etiquetas, procesados)



def generarEtiqueta(grafo, nodo, anterior, etiquetas):	
	etiquetaNodoAnterior = etiquetas[anterior]
	etiquetaPropuesta = peso(grafo, anterior, nodo) + acumulado(etiquetaNodoAnterior),anterior
	if (not(etiquetas.has_key(nodo)) or  acumulado(etiquetaPropuesta) < acumulado(etiquetas[nodo]) ):
	    etiquetas.update({nodo:etiquetaPropuesta})



def aristas(grafo, nodo):	
	return grafo.relaciones[nodo]
        
def vecinoNoProcesado(grafo, nodo, procesados):	
	aristasDeVecinosNoProcesados = filter(lambda x: not x in procesados, aristas(grafo,nodo))	
	return [arista for arista in aristasDeVecinosNoProcesados]


def peso(grafo, nodoOrigen, nodoDestino): 
    return reduce(lambda x,y: x if x == nodoDestino else y, grafo.relaciones[nodoOrigen]).peso 

def acumulado(etiqueta):
    return etiqueta[0]

def anterior(etiqueta):
    return etiqueta[1]
           
def menorValorNoProcesado(etiquetas, procesados):
    etiquetadosSinProcesar = filter(lambda (nodo,_):not nodo in procesados, etiquetas.iteritems())
    return min(etiquetadosSinProcesar, key=lambda (_, (acum, __)): acum)[0]    
#-----------------------------------------------------MAIN---------------------------------------------------------
def main():
	mat=[[1,16,3,4,5],[2,2,19,20,21],[6,2,2,9,10],[11,2,13,14,15]]
	matriz = Matriz(5,4,mat)
	
	grafo = generarGrafo(matriz)
	anchoPrimero(grafo,matriz.get_lista()[3],imprimir)
	listaa=caminoMinimo(grafo,matriz.get_lista()[7],matriz.get_lista()[10])	
	for elemento in listaa:	
		if(elemento.get_valor()!=2):
			print elemento.get_valor()
		else:
			print("el camino esta bloqueado ")

if __name__=='__main__':
	main()