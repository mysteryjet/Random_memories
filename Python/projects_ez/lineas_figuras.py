import pygame
import sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("titulo de la ventana")

#colores
colorFondo = (1, 150, 70)
colorLinea = (255,128,0)
colorCirculo = (255,255,0)
colorFiguras = (255,0,155)
while True:
    ventana.fill(colorFondo)
    pygame.draw.line(ventana,colorLinea,(60,90),(200,100),40)
    pygame.draw.line(ventana,colorLinea,(80,190),(100,150),20)
    pygame.draw.line(ventana,colorLinea,(10,30),(250,100),10)

    #circulos
    pygame.draw.circle(ventana,colorCirculo, (400,100),100,30)
    #figuras
    pygame.draw.rect(ventana,colorFiguras,(400,200,500,250))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()