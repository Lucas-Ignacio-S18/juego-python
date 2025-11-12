import pygame
import constantes

#!inicializar
pygame.init()


#!display, mostramos la ventana

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                    constantes.ALTO_VENTANA))# traemos variables de tamano del archivo "constante"

#!nombre ventana
pygame.display.set_caption("Jogo bonito")

#!loop de ejecucion
run = True
while run == True:
    #todo- event.get: entrega lista de todos los eventos que toma en el juego(ej. un click) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#todo| QUIT: cerrar la ventana o F4
            run = False  #!Cerramos ventana
pygame.quit()
