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
skySurface = pygame.image.load('graphics/Sky.png').convert_alpha()
groundSurface = pygame.image.load('graphics/ground.png').convert_alpha()
textSurface = testFont.render('SCORE', False, 'blue')

snailSurface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snailRect =snailSurface.get_rect(midbottom = (-100,300))
snailXPos = 600

#Creating surface for player
playerSurface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
playerRect = playerSurface.get_rect(midbottom = (80,300))



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
    snailRect.left += -1
    if snailRect.left < -100: snailRect.left = 800
    screen.blit(snailSurface,snailRect)
    playerRect.left += 1
    screen.blit(playerSurface, playerRect)
    

    #Draw all our elements update everything
    pygame.display.update()
    clock.tick(60)