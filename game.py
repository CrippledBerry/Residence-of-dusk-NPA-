#Residence of Dusk (MENU)
#Logan Shearer
#25/4/22
#-----------------
import pygame, os
running = True
pygame.init()
screen = pygame.display.set_mode([1200, 800])
pygame.display.set_caption('RESIDENCE of DUSK')

titleFont = pygame.font.SysFont(None, 84)
infoFont = pygame.font.SysFont(None, 24)

while running == True:
    screen.fill((0, 0, 0))
    title = titleFont.render("Resident of Dusk", False, [255, 0, 0], [0, 0, 0])
    screen.blit(title,[400, 100])

    story = infoFont.render("YOU are John Night, a boring man who has lived a boring life. one day however, he came across a", False, [255, 255, 255], [0, 0, 0])
    screen.blit(story,[200, 200])
    story2 = infoFont.render("mysterious book filled with eldritch knowledge, the ink printed promised him his every dream.", False, [255, 255, 255], [0, 0, 0])
    screen.blit(story2,[200, 230])
    story3 = infoFont.render("john set up one the rituals attempting to gain everything, but he failed a crucial step and", False, [255, 255, 255], [0, 0, 0])
    screen.blit(story3,[200, 260])
    story4 = infoFont.render("has promised the world one thing: imminent destruction. or as humans would comprehend.", False, [255, 255, 255], [0, 0, 0])
    screen.blit(story4,[200, 290])

    
    tutorial = infoFont.render("You have one goal: SURVIVE. there is no escape, only delaying the inevitable.", False, [255, 255, 255], [0, 0, 0])
    screen.blit(tutorial,[200, 390])
    tutorial2 = infoFont.render("Use W + S or THE UP AND DOWN ARROWS to move", False, [255, 255, 255], [0, 0, 0])
    screen.blit(tutorial2,[200, 420])
    tutorial3 = infoFont.render("collect the RED FRUIT to increase your score. ", False, [255, 255, 255], [0, 0, 0])
    screen.blit(tutorial3,[200, 450])
    tutorial4 = infoFont.render("AVOID OBSTACLES such as TRANSFORMED CHAIRS and TENTACLES BURSTING THROUGH THE WALLS.", False, [255, 255, 255], [0, 0, 0])
    screen.blit(tutorial4,[200, 480])
    tutorial5 = infoFont.render("when collecting FRUIT you will become BRIEFLY INVULNERABLE, use this to move through CHAIRS.", False, [255, 255, 255], [0, 0, 0])
    screen.blit(tutorial5,[200, 510])
    tutorial6 = infoFont.render("PRESS SPACE to start... GOODLUCK...", False, [255, 255, 255], [0, 0, 0])
    screen.blit(tutorial6,[200, 540])
    
    pygame.display.flip()

    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False

    if keys[pygame.K_SPACE]:
        os.system('residentdusk.py')
        running = False

    for event in pygame.event.get():               
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
