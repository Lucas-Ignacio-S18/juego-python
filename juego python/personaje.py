import pygame
import constantes

class Personaje():
    # inicializamos al pj, le damos las coordenadas
    def __init__(self,x,y, image):
        
        #todo --imagen/dibujo del pj--
        self.image = image

        #(rectangulo) forma(ubicacion (x,y, ancho, alto))
        self.forma = pygame.Rect(0,0, constantes.ANCHO_PJ, constantes.ALTO_PJ)
        self.forma.center = (x,y)

    #! Movimiento
    def movimiento(self, delta_x, delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    #! Forma
    def dibujar(self, interfaz):
        interfaz.blit(self.image, self.forma)
        pygame.draw.rect(interfaz, constantes.COLOR_PJ, self.forma)

