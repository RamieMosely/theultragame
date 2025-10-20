import pygame
from sys import exit

#Put Objects in variables
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('ULTRA')

#Control framerate for all computer types
clock = pygame.time.Clock()

#Create font
testFont = pygame.font.Font('font/Pixeltype.ttf', 50)

#Create sky and ground surface and text surface
skySurface = pygame.image.load('graphics/Sky.png')
groundSurface = pygame.image.load('graphics/ground.png')
textSurface = testFont.render('SCORE', False, 'blue')

snailSurface = pygame.image.load('graphics/snail/snail1.png')



#Main Gameplay Loop
while True:
    #Check if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Load sky and ground surface and text surface in game
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface,(0,300))
    screen.blit(textSurface, (10,10))
    screen.blit(snailSurface,(600,250))

    #Draw all our elements update everything
    pygame.display.update()
    clock.tick(60)