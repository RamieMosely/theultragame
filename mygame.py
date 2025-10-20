import pygame
from sys import exit

#Put Objects in variables
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('ULTRA')
clock = pygame.time.Clock()

#Create a surface and import image
testSurface = pygame.image.load('graphics/Sky.png')



#Main Gameplay Loop
while True:
    #Check if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(testSurface,(200,100))

    #draw all our elements update everything
    pygame.display.update()
    clock.tick(60)