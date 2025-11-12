import pygame

#inicializar
pygame.init()

#tamano(px), ancho - alto
width = 800
height = 600

#display, mostramos la ventana
ventana = pygame.display.set_mode((width,height))

#!loop de ejecucion
run = True
while run == True:
    #todo- event.get: entrega lista de todos los eventos que toma en el juego(ej. un click) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#todo| QUIT: cerrar la ventana o F4
            run = False  #!Cerramos ventana
pygame.quit()