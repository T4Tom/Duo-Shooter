import pygame, time, random
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

score = 0
shot = False

pointsfont = pygame.font.SysFont(None, 72)

shipimg1 = pygame.image.load('Ship1.png')
shipimg1 = pygame.transform.scale(shipimg1, (100, 160))
shipimg2 = pygame.image.load('Ship2.png')
shipimg2 = pygame.transform.scale(shipimg2, (100, 160))
mineimg1 = pygame.image.load('mine1.png')
mineimg1 = pygame.transform.scale(mineimg1, (50, 50))
mineimg2 = pygame.image.load('mine2.png')
mineimg2 = pygame.transform.scale(mineimg2, (50, 50))
explosionimg = pygame.image.load('explosion.png')




def game_loop():
  
  score = 0
  shot = False
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
  
  minelocation1 = [mine1x, mine1y]
  minelocation2 = [mine2x, mine2y]
  
  
  
  
  
  done = False
  while not done:
    
    screen.fill((0, 0, 0))
    
    pointstext = pointsfont.render('Points: {0}'.format(score), True, (255, 255, 255))
    pointstextRect = pointstext.get_rect()
    pointstextRect.center = (400, 50)
    screen.blit(pointstext, pointstextRect)
    
    ship1_rect = pygame.Rect(shiplocation1[0], shiplocation1[1], shipimg1.get_width(), shipimg1.get_height())
    ship2_rect = pygame.Rect(shiplocation2[0], shiplocation2[1], shipimg2.get_width(), shipimg2.get_height())
    mine1_rect = pygame.Rect(minelocation1[0], minelocation1[1], mineimg1.get_width(), mineimg1.get_height())
    mine2_rect = pygame.Rect(minelocation2[0], minelocation2[1], mineimg2.get_width(), mineimg2.get_height())

    laser1_rect = pygame.Rect(laserx, lasery, 5, 40)
    laser2_rect = pygame.Rect(laserx2, lasery2, 5, 40)    
    
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        shot = True
        
        
      
    if laser1_rect.colliderect(mine1_rect):
      hit1 = True
    if laser2_rect.colliderect(mine2_rect):
      hit2 = True
      
      
    
    if hit1:
      pass
    if hit2:
      pass
      
      
    if hit1 and hit2:
      pass
      
      
      
    if not shot:
      laserx = shiplocation1[0] + 48
      lasery = 480
      laserx2 = shiplocation2[0] + 48
      lasery2 = 480
    
        
    elif shot:
      lasery -= 5
      pygame.draw.rect(screen, (150, 0, 0), pygame.Rect(laserx, lasery, 5, 40))
      if lasery < -100:
        shot = False
      lasery2 -= 5
      pygame.draw.rect(screen, (178, 102, 255), pygame.Rect(laserx2, lasery2, 5, 40))
      if lasery2 < -100:
        shot = False
      
      
        
        
        
        
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and shiplocation1[0] + 100 <= 800:
      shiplocation1[0] += 3
    if pressed[pygame.K_LEFT] and shiplocation1[0] >= 0:
      shiplocation1[0] -= 3
      
    if pressed[pygame.K_d] and shiplocation2[0] + 100 <= 800:
      shiplocation2[0] += 3
    if pressed[pygame.K_a] and shiplocation2[0] >= 0:
      shiplocation2[0] -= 3

    screen.blit(mineimg1, minelocation1)
    screen.blit(mineimg2, minelocation2)
    screen.blit(shipimg1, shiplocation1)
    screen.blit(shipimg2, shiplocation2)
      
      
      

    pygame.display.flip()
    clock.tick(70)

game_loop()


# Ship 1 = red, right
# Ship 2 = purple, left
