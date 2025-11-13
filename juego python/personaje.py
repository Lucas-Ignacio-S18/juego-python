import pygame
import constantes

class Personaje():
    # inicializamos al pj, le damos las coordenadas
    def __init__(self,x,y, animacion):
        #todo flip = voltear, para que el pj se de vuelta/voltee
        self.flip =  False
        self.animaciones = animacion
        #imagen de la animacion
        self.frame_index = 0
        #se guarda la hora en la que se inicializo
        self.update_time = pygame.time.get_ticks()
        self.image = animacion[self.frame_index]

        #(rectangulo) forma(ubicacion (x,y, ancho, alto))
        self.forma = pygame.Rect(0,0, constantes.ANCHO_PJ, constantes.ALTO_PJ)
        self.forma.center = (x,y)

    #! Movimiento
    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True #se da vuelta
        if delta_x > 0:
            self.flip = False #no se da vuelta

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
    
    def update(self):
        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index +1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

    #! Forma
    def dibujar(self, interfaz):
        #creamos flip
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        #pygame.draw.rect(interfaz, constantes.COLOR_PJ, self.forma,1)

