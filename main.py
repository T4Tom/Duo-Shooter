import pygame, time
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

score = 0

pointsfont = pygame.font.SysFont(None, 72)

shipimg1 = pygame.image.load('Ship1.png')
shipimg1 = pygame.transform.scale(shipimg1, (50, 80))
shipimg2 = pygame.image.load('Ship2.png')
shipimg2 = pygame.transform.scale(shipimg2, (50, 80))




def game_loop():
  
  score = 0
  
  shiplocation1 = [500, 500]
  shiplocation2 = [300, 500]
  
  done = False
  while not done:
    
    screen.fill((0, 0, 0))
    
    pointstext = pointsfont.render('Points: {0}'.format(score), True, (255, 255, 255))
    pointstextRect = pointstext.get_rect()
    pointtextRect.center = (400, 50)
    
    
    
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
