import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont(None, 48)
img = font.render('My first game screen', True, (255,255,255)) 
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    screen.fill((58,58,58))
    screen.blit(img, (100,250))
    pygame.display.flip()
pygame.quit()