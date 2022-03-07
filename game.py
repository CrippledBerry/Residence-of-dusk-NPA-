#residence of dusk (NPA game)
#7/3/22
#------------------------------------
import pygame
#------------------------------------
#initialise
pygame.init()

#draw window
screen = pygame.display.set_mode([1000,1000])

#variables
running = True

#sprites
#player image
playerImg = pygame.image.load('assets/sprites/sprite-placeholder.jpeg')
playerImg.convert()
playerRect = playerImg.get_rect()
playerRect.center = 500, 500
#------------------------------------
#game loop
while running:
    #--------------------------------
    #input
    for event in pygame.event.get():
        #close game
        if event.type == pygame.QUIT:
            running = False
        #---------------------------
    #-------------------------------
    #update
    #-------------------------------
    #Draw
    #colour background
    screen.fill((0,0,0))

    #draw sprites
    screen.blit(playerImg, playerRect)

    #flip the display
    pygame.display.flip()
    #--------------------------------


#END OF LOOP
#------------------------------------
pygame.quit()
