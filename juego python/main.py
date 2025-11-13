import os
import pygame
import constantes
from personaje import Personaje


#!--- inicializar ---
pygame.init()
#! --- display, mostramos la ventana ---
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                    constantes.ALTO_VENTANA))# traemos variables de tamano del archivo "constante"
#todo -- nombre ventana --
pygame.display.set_caption("Jogo bonito")


#todo -Animacion-

def escalar_img(image,scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image,(w*scale, h*scale))
    return nueva_imagen

animacion = []
for i in range(9):
    #Cambiamos el numero de imagen por i del For
    img = pygame.image.load(f"juego python//assets//img//personajes//player_main//caminata0{i}.png") 
    img = escalar_img(img, constantes.ESCALA_PJ)
    animacion.append(img)

#todo --imagen--
# player_image = pygame.image.load("juego python//assets//img///personajes//player_main//caminata00.png")
# #escala del tamaño del pj en %
# player_image = escalar_img(player_image, constantes.ESCALA_PJ)


#!Traemos la clase PJ y le asiganmos la ubicacion
jugador = Personaje(100,200, animacion)


#variables de movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#todo --fps--
fps = pygame.time.Clock()

#!--- loop de ejecucion ---
run = True
while run == True:

    #todo -- FPS --
    fps.tick(constantes.FPS)

    #todo -- Color de fondo --
    ventana.fill(constantes.COLOR_BG)

    #todo -- Movimiento del jugador --
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD  
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD 
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD 
    
    #todo --mover jugador--
    jugador.movimiento(delta_x, delta_y)
    jugador.update()


    #todo --llamamos a la funcion jugador--
    jugador.dibujar(ventana)

    #? event.get: entrega lista de todos los eventos que toma en el juego(ej. un click) 

    #todo --CIERRE DE JUEGO--
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#todo| QUIT: cerrar la ventana o F4
            run = False  #!Cerramos ventana

    #todo --TECLAS/movimientos--
        #KEYDOWN: reconocer cuando se oprime una tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: #Key_(Tecla "a")
                mover_izquierda = True
            if event.key == pygame.K_d: 
                mover_derecha = True
            if event.key == pygame.K_w: 
                mover_arriba = True
            if event.key == pygame.K_s: 
                mover_abajo = True

        #KEYDOWN: reconocer cuando se suelta una tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: #Key_(Tecla "a")
                mover_izquierda = False
            if event.key == pygame.K_d: 
                mover_derecha = False
            if event.key == pygame.K_w: 
                mover_arriba = False
            if event.key == pygame.K_s: 
                mover_abajo = False



    #! --- Actualizacion de pantalla ---
    pygame.display.update()


pygame.quit()
