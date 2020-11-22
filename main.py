import pygame, time, random, sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Duo Shooter")

score = 0
level = 1
gainedpoints = 100
shot1 = False
shot2 = False

normalfont = pygame.font.SysFont(None, 60)

deathfont = pygame.font.SysFont(None, 100)
deathtext = deathfont.render('GAME OVER', True, (255, 0, 0))
deathtextRect = deathtext.get_rect()
deathtextRect.center = (400, 300)



shipimg1 = pygame.image.load('Ship1.png')
shipimg1 = pygame.transform.scale(shipimg1, (100, 160))
shipimg2 = pygame.image.load('Ship2.png')
shipimg2 = pygame.transform.scale(shipimg2, (100, 160))
mineimg1 = pygame.image.load('mine1.png')
mineimg1 = pygame.transform.scale(mineimg1, (50, 50))
mineimg2 = pygame.image.load('mine2.png')
mineimg2 = pygame.transform.scale(mineimg2, (50, 50))
explosionimg = pygame.image.load('explosion.png')
explosionimg = pygame.transform.scale(explosionimg, (100, 100))


COUNTDOWN = pygame.USEREVENT
TIMER = pygame.USEREVENT + 1

    


def game_loop():

    seconds = 5
        
    level = 1
    gainedpoints = 100
    score = 0
    shot1 = False
    shot2 = False
    hit1 = False
    hit2 = False
    
    shiplocation1 = [450, 400]
    shiplocation2 = [250, 400]
    
    laserx = shiplocation1[0] + 48
    lasery = 480
    laserx2 = shiplocation2[0] + 48
    lasery2 = 480
    
    mine1y = random.randint(0, 300)
    mine1x = random.randint(0, 750)
    mine2y = random.randint(0, 300)
    mine2x = random.randint(0, 750)
    
    

    
    pygame.time.set_timer(COUNTDOWN, 5000)
    pygame.time.set_timer(TIMER, 1000)
    
    game_active = False
    while True:
        
        screen.fill((0, 0, 0))    
        

        minelocation1 = [mine1x, mine1y]
        minelocation2 = [mine2x, mine2y]
        
        
        ship1_rect = pygame.Rect(shiplocation1[0], shiplocation1[1], shipimg1.get_width(), shipimg1.get_height())
        ship2_rect = pygame.Rect(shiplocation2[0], shiplocation2[1], shipimg2.get_width(), shipimg2.get_height())
        mine1_rect = pygame.Rect(minelocation1[0], minelocation1[1], mineimg1.get_width(), mineimg1.get_height())
        mine2_rect = pygame.Rect(minelocation2[0], minelocation2[1], mineimg2.get_width(), mineimg2.get_height())

        explosionimgRect = explosionimg.get_rect()
        explosionimgRect.center = (minelocation1[0] + 25, minelocation1[1] + 25)
        explosionimgRect2 = explosionimg.get_rect()
        explosionimgRect2.center = (minelocation2[0] + 25, minelocation2[1] + 25)


        laser1_rect = pygame.Rect(laserx, lasery, 5, 40)
        laser2_rect = pygame.Rect(laserx2, lasery2, 5, 40)        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                shot1 = True
                shot2 = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_loop()
            if event.type == COUNTDOWN:
                game_active = False
                game_loop()
            if event.type == TIMER:
                seconds -= 1
                
                
            
        if laser1_rect.colliderect(mine1_rect):
            hit1 = True
        if laser2_rect.colliderect(mine2_rect):
            hit2 = True
            
            
        secondstext = normalfont.render("Seconds: {0}".format(seconds), True, (255, 255, 255))
        secondstextRect = secondstext.get_rect(center = (200, 200))
         
            
        if not shot1:
            laserx = shiplocation1[0] + 48
            lasery = 480
                
        elif shot1:
            lasery -= 10
            pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(laserx, lasery, 5, 40))
            if lasery < -100:
                game_active = False
        
        if not shot2:
            laserx2 = shiplocation2[0] + 48
            lasery2 = 480

        
        elif shot2:
            lasery2 -= 10
            pygame.draw.rect(screen, (178, 102, 255), pygame.Rect(laserx2, lasery2, 5, 40))
            if lasery2 < -100:
                game_active = False
            
                
                
                
                
                
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and shiplocation1[0] + 100 <= 800:
            shiplocation1[0] += 6
        if pressed[pygame.K_LEFT] and shiplocation1[0] >= 0:
            shiplocation1[0] -= 6
            
        if pressed[pygame.K_d] and shiplocation2[0] + 100 <= 800:
            shiplocation2[0] += 6
        if pressed[pygame.K_a] and shiplocation2[0] >= 0:
            shiplocation2[0] -= 6
                 
        
        pointstext = normalfont.render('Points: {0}'.format(score), True, (255, 255, 255))
        pointstextRect = pointstext.get_rect()
        pointstextRect.center = (600, 50)
        
        leveltext = normalfont.render('Level: {0}'.format(level), True, (255, 255, 255))
        leveltextRect = leveltext.get_rect()
        leveltextRect.center = (200, 50)
        
        if game_active:
            screen.blit(mineimg1, minelocation1)
            screen.blit(mineimg2, minelocation2)
            screen.blit(shipimg1, shiplocation1)
            screen.blit(shipimg2, shiplocation2)  
            screen.blit(pointstext, pointstextRect)        
            screen.blit(leveltext, leveltextRect)
            screen.blit(secondstext, secondstextRect)

        if hit1 and game_active:
            shot1 = False
            screen.blit(explosionimg, explosionimgRect)
        
        if hit2 and game_active:
            shot2 = False
            screen.blit(explosionimg, explosionimgRect2)
            
            
        if hit1 and hit2 and game_active:
            screen.blit(explosionimg, explosionimgRect)
            screen.blit(explosionimg, explosionimgRect2)
            screen.blit(shipimg1, shiplocation1)
            screen.blit(shipimg2, shiplocation2)
            screen.blit(leveltext, leveltextRect)
            screen.blit(pointstext, pointstextRect)
            pygame.display.flip()
            time.sleep(0.2)
            mine1y = random.randint(0, 300)
            mine1x = random.randint(0, 750)
            mine2y = random.randint(0, 300)
            mine2x = random.randint(0, 750)
            hit1 = False
            hit2 = False
            level += 1
            score += gainedpoints
            gainedpoints += 100
            pygame.time.set_timer(COUNTDOWN, 5000)
            pygame.time.set_timer(TIMER, 1000)
            seconds = 5  

        if not game_active:
            screen.fill((0, 0, 0))
            if pressed[pygame.K_UP]:
                game_active = True


        pygame.display.flip()
        clock.tick(70)

game_loop()


# Ship 1 = red, right
# Ship 2 = purple, left

