import pygame

class Personaje():
    # inicializamos al pj, le damos las coordenadas
    def __init__(self,x,y):

        #(rectangulo) forma(ubicacion (x,y, ancho, alto))
        self.forma = pygame.Rect(0,0,20,40)
        self.forma.center = (x,y)
