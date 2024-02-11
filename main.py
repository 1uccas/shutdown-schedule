import pygame

pygame.init()

display = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shutdown')
 
run = True
# e aqui nós entramos no loop do game
while run:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
          run = False
          
    pygame.display.update()
    
pygame.quit()
exit()