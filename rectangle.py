import pygame

pygame.init()

screen = pygame.display.set_mode((1920,1200))
running = False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
    pygame.draw.rect(screen, (254,253,252),pygame.Rect (100,100,100,100))
    pygame.display.flip()