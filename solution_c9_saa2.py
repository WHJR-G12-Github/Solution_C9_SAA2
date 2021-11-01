import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["cloud"] = pygame.image.load("cloud.png").convert_alpha()

bird=pygame.Rect(100,250,30,30)
groundx=0

# Creating a variable 'cloudx' and initialize it to 300
cloudx=300

while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-550:
      groundx=0
  screen.blit(images["ground"],[groundx,550]) 
  screen.blit(images["bird"],bird)
  
  # Decrementing 'cloudx' by 3
  cloudx-=3
  # Checking if 'cloudx' is less than -100
  if cloudx<-100:
      # Resetting the value 'cloudx' back to 300
      cloudx=300
  # Displaying the cloud image at [cloudx,150]
  screen.blit(images["cloud"],[cloudx,150])
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
