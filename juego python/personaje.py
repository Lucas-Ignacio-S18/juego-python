import pygame
import constantes

class Personaje():
    # inicializamos al pj, le damos las coordenadas
    def __init__(self,x,y):

        #(rectangulo) forma(ubicacion (x,y, ancho, alto))
        self.forma = pygame.Rect(0,0, constantes.ANCHO_PJ, constantes.ALTO_PJ)

        self.forma.center = (x,y)
    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constantes.COLOR_PJ, self.forma)