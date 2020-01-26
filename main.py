import pygame, time
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

score = 0

pointsfont = pygame.font.SysFont(None, 72)

shipimg1 = pygame.image.load('Ship1.png')
shipimg1 = pygame.transform.scale(shipimg1, (100, 160))
shipimg2 = pygame.image.load('Ship2.png')
shipimg2 = pygame.transform.scale(shipimg2, (100, 160))
mineimg1 = pygame.image.load('mine1.png')
mineimg1 = pygame.transform.scale(mineimg1, (50, 50))
mineimg2 = pygame.image.load('mine2.png')
mineimg2 = pygame.transform.scale(mineimg2, (50, 50))




def game_loop():
  
  score = 0
  
  shiplocation1 = [450, 400]
  shiplocation2 = [250, 400]
  
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
    
    
    screen.blit(mineimg1, minelocation1)
    screen.blit(mineimg2, minelocation2)
    screen.blit(shipimg1, shiplocation1)
    screen.blit(shipimg2, shiplocation2)
    
    
    
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      if event.type == pygame.K_ESCAPE:
        exit()


    pygame.display.flip()
    clock.tick(70)

game_loop()
