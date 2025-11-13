import pygame
import constantes
from personaje import Personaje

#Traemos la clase PJ y le asiganmos la ubicacion
jugador = Personaje(250,350)

#!--- inicializar ---
pygame.init()

#! --- display, mostramos la ventana ---
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                    constantes.ALTO_VENTANA))# traemos variables de tamano del archivo "constante"

#! --- nombre ventana ---
pygame.display.set_caption("Jogo bonito")

#!--- loop de ejecucion ---
run = True
while run == True:

    jugador.dibujar(ventana)

    # event.get: entrega lista de todos los eventos que toma en el juego(ej. un click) 

    #todo --CIERRE DE JUEGO--
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#todo| QUIT: cerrar la ventana o F4
            run = False  #!Cerramos ventana

    #todo --TECLAS/movimientos--
    #KEYDOWN: reconocer cuando se oprime una tecla
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a: #Key_(Tecla "a")
            print("Izquierda")
        if event.key == pygame.K_d: 
            print("Derecha")
        if event.key == pygame.K_w: 
            print("Arriba")
        if event.key == pygame.K_s: 
            print("Abajo")



    #! --- Actualizacion de pantalla ---
    pygame.display.update()


pygame.quit()
