#Residence of Dusk
#Logan Shearer
#14/3/22
#-----------------

import pygame, random, os

pygame.init()
screen = pygame.display.set_mode([1200, 800])
pygame.display.set_caption('RESIDENCE of DUSK')

#variables ---------------------------------
currentFrame = 0
startScreen = True
started = False
running = True
mainClock = pygame.time.Clock()
score = 0
timer = 10
dt = 0
clock = pygame.time.Clock()
deathcause = " "
combo = 0

#fonts
basicFont = pygame.font.SysFont(None, 48)
deathFont = pygame.font.SysFont(None, 78)
deathinfoFont = pygame.font.SysFont(None, 32)

  
#player
currentpos = [float(600), float(400)]
move_direction = "right"
MOVESPEED = 200
alive = True
invuln = 1

#monster
monsterpos = [float(0), float(0)]
monsterActive = False
monsterDistanceX = 0
monsterDistanceY = 0
inRange = False
patrolpos = [float(600),float(400)]

#sprite images/collision
player_image = pygame.image.load('assets/john.png').convert_alpha()
player_Rect = pygame.Rect(currentpos[0], currentpos[1], player_image.get_width(), player_image.get_height())

currentFrame = 0
tentacleFrames = [pygame.image.load('assets/tentacle_1.png'),
                  pygame.image.load('assets/tentacle_2.png'),
                  pygame.image.load('assets/tentacle_3.png'),
                  pygame.image.load('assets/tentacle_4.png')]

tentacle_image = tentacleFrames[currentFrame].convert_alpha()
tentacle_image2 = pygame.transform.rotate(tentacle_image, 180)

monster_image = pygame.image.load('assets/monster.png').convert_alpha()
monster_Rect = pygame.Rect(currentpos[0], currentpos[1], monster_image.get_width(), monster_image.get_height())

chair_image = pygame.image.load('assets/chair.png').convert_alpha()
chair_Rect = pygame.Rect(0, 0, chair_image.get_width(), chair_image.get_height())

#chair setup
chairPos_list = []
chaircount = 1

newChairx = random.randint(200,1000)
newChairy = random.randint(200,600)
chairPos_list.append([newChairx,newChairy])

#fruit setup
fruit_posx = random.randint(200, 1000)
fruit_posy = random.randint(200, 600)

#power setup
power_posx = random.randint(200, 1000)
power_posy = random.randint(200, 600)

screen.fill((0, 0, 0))
title = basicFont.render("Resident of Dusk", False, [255, 255, 255], [0, 0, 0])
screen.blit(title,[100, 730])
pygame.display.flip()

#game loop -----------------------------------
while running == True:
    fruit_Rect = pygame.Rect(fruit_posx, fruit_posy, 35, 35)
    power_Rect = pygame.Rect(power_posx, power_posy, 25, 25)

    if started == False:
            currentpos = [float(600), float(400)]
            started = True
            
    #screen
    if score <= 19:
        screen.fill((92, 46, 6))                                     
    pygame.draw.rect(screen, [0, 0, 0], [0, 0, 1200, 150], 0)
    pygame.draw.rect(screen, [0, 0, 0], [0, 0, 100, 800], 0)
    pygame.draw.rect(screen, [0, 0, 0], [1100, 0, 100, 800], 0)
    pygame.draw.rect(screen, [0, 0, 0], [0, 650, 1200, 150], 0)

    #sprites images
    screen.blit(player_image, currentpos)
    pygame.draw.rect(screen, [255, 0, 0], fruit_Rect, 0)
    pygame.draw.rect(screen, [144, 0, 255], power_Rect, 0)

    if monsterActive == True:
        screen.blit(monster_image, monsterpos)

    for chair in chairPos_list:
        screen.blit(chair_image, chair)

    #tentacle
    tentacle_image = tentacleFrames[currentFrame].convert_alpha()
    tentacle_image2 = pygame.transform.rotate(tentacle_image, 180)
    tentposx = 120
    for i in range(32):
        currentFrame = random.randint(0,3)
        tentacle_image = tentacleFrames[currentFrame].convert_alpha()
        screen.blit(tentacle_image, [tentposx, 150])
        tentposx += 30     
    tentposx = 120    
    for i in range(32):
        currentFrame = random.randint(0,3)
        screen.blit(tentacle_image2, [tentposx, 617])
        tentposx += 30

    
    #score label
    scoreDisplay = basicFont.render('Score: ' + str(score), False, [255, 255, 255], [0, 0, 0])
    screen.blit(scoreDisplay,[100, 680])
    comboDisplay = basicFont.render('combo: ' + str(combo) + "x", False, [255, 255, 255], [0, 0, 0])
    screen.blit(comboDisplay,[450, 680])
    if invuln > 0:
        invulnDisplay = basicFont.render('invulnerability left: ' + str(invuln), False, [255, 255, 255], [0, 0, 0])
    else:
        invulnDisplay = basicFont.render('invulnerability left: ' + str(invuln), False, [255, 0, 0], [0, 0, 0])
    screen.blit(invulnDisplay,[700, 680])
    timeDisplay = basicFont.render('time left: ' + str(int(timer)) + " second/s", False, [255, 255, 255], [0, 0, 0])
    screen.blit(timeDisplay,[100, 730])
    deathmessage = deathFont.render('You Died', False, [255, 0, 0], [0, 0, 0])
    deathinfo = deathinfoFont.render('Cause of Death: ' + deathcause, False, [255, 0, 0], [0, 0, 0])
    restart = deathinfoFont.render('press R to restart | ESC to exit', False, [255, 0, 0], [0, 0, 0])
    if alive == False:
        screen.fill((0, 0, 0))
        screen.blit(deathmessage,[500, 200])
        screen.blit(scoreDisplay,[550, 300])
        screen.blit(deathinfo,[420, 400])
        screen.blit(restart,[470, 500])


    #monster AI        
    if score >= 10:
        monsterActive = True
    if monsterActive == True:
        monsterDistanceX = monsterpos[0] - currentpos[0]
        monsterDistanceY = monsterpos[1] - currentpos[1]
        if monsterDistanceX <= 300 and monsterDistanceY <= 300 and monsterDistanceX >= -300 and monsterDistanceY >= -300:
            inRange = True
        else:
            inRange = False
        if inRange == True:
            if monsterpos[0] < currentpos[0]:
                monsterpos[0] += 3
            if monsterpos[0] > currentpos[0]:
                monsterpos[0] -= 3
            if monsterpos[1] < currentpos[1]:
                monsterpos[1] += 3
            if monsterpos[1] > currentpos[1]:
                monsterpos[1] -= 3
        elif inRange == False:            
            if monsterpos[0] < patrolpos[0]:
                monsterpos[0] += 5
            if monsterpos[0] > patrolpos[0]:
                monsterpos[0] -= 5
            if monsterpos[1] < patrolpos[1]:
                monsterpos[1] += 5
            if monsterpos[1] > patrolpos[1]:
                monsterpos[1] -= 5
            if monsterpos[0] == patrolpos[0] and monsterpos[1] == patrolpos[1]:
                if patrolpos[0] == 200 and patrolpos[1] == 400:
                    patrolpos = [float(200),float(400)]
                else:
                    patrolpos = [float(900),float(400)]

    #frame time ----------------
    frameMs = mainClock.tick(60)
    frameSec = frameMs / 1000
    
    #button events
    keys = pygame.key.get_pressed()

    #while player alive
    if alive:

        #chair spawn
        def chairSpawn():
            if chaircount < 8:
                chaircount + 1
                newChairx = random.randint(200,1000)
                newChairy = random.randint(200,600)
                chairPos_list.append([newChairx,newChairy])

        #score invuln
        if invuln > 0:
            invuln -= dt
        if invuln <0:
            invuln = 0
            combo = 0

        #PLAYER BOX
        player_Rect.left = currentpos[0]
        player_Rect.top = currentpos[1]

        #chair box
        for chair in chairPos_list:
            chair_Rect.left = chair[0]
            chair_Rect.top = chair[1]
            #chair collision
            if invuln <= 0:
                if pygame.Rect.colliderect(player_Rect,chair_Rect):
                    alive = False
                    deathcause = "CHAIRED TO DEATH"

        #MONSTER COLLISION
        monster_Rect.left = monsterpos[0]
        monster_Rect.top = monsterpos[1]
        if invuln <= 0:
                if pygame.Rect.colliderect(player_Rect,monster_Rect):
                    alive = False
                    deathcause = "???????????????????????????????????????????????????????????????????"

        #fruit collision
        if pygame.Rect.colliderect(player_Rect,fruit_Rect):
            fruit_posx = random.randint(200, 1000)
            fruit_posy = random.randint(190, 600)
            pygame.draw.rect(screen, [255, 0, 0], fruit_Rect, 0)
            combo += 1
            score += 1 * combo
            timer = 10
            invuln += 1.5
            chairSpawn()
            if score >= 10:
                screen.fill((random.randint(0,230),random.randint(0,255),random.randint(0,255)))
        if pygame.Rect.colliderect(player_Rect,power_Rect):
            power_posx = random.randint(200, 1000)
            power_posy = random.randint(190, 600)
            invuln += .7

        if pygame.Rect.colliderect(fruit_Rect ,chair_Rect):
            fruit_posx = random.randint(200, 1000)
            fruit_posy = random.randint(190, 600)
            pygame.draw.rect(screen, [255, 0, 0], fruit_Rect, 0)
        
        #movement
        if move_direction == "left":
                currentpos[0] -= (350 + (combo * 50))  * frameSec
        if move_direction == "right":
                currentpos[0] += (350 + (combo * 50)) * frameSec

        if currentpos[0] <= 100 or currentpos[0] >=1080:
            if move_direction == "left":
                move_direction = "right"
            else:
                move_direction = "left"

        if currentpos[1] <= 175 or currentpos[1] >= 600:
            deathcause = "TENTACLE BLENDER SLAP"
            alive = False
                
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            currentpos[1] -= (MOVESPEED * 1.6) * frameSec
            player_image = pygame.transform.rotate(player_image, 90)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            currentpos[1] += (MOVESPEED * 1.6) * frameSec
            player_image = pygame.transform.rotate(player_image, -90)

        #timer
        timer -= dt
        dt = clock.tick(30) / 1000
        if timer <= 0:
            timer = 0
            deathcause = "OUT OF TIME"
            alive = False
            
    #esc to close game
    if keys[pygame.K_ESCAPE]:
        running = False

    if keys[pygame.K_r]:
        if alive == False:
          os.system('residentdusk.py')
          running = False
        
    for event in pygame.event.get():               
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
