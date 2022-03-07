#residence of dusk (NPA game)
#7/3/22
#------------------------------------
import pygame
#------------------------------------
#initialise
pygame.init()

#draw window
screen = pygame.display.set_mode([750,750])

#variables
running = True
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

    #draw circle
    pygame.draw.circle(screen, (255,0,255), (350,350), 75)

    #flip the display
    pygame.display.flip()
    #--------------------------------


#END OF LOOP
#------------------------------------
pygame.quit()
