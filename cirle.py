import pygame
pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill((230,225,211))
pygame.draw.circle(screen, (255,255,255), (500,500), 250)
pygame.draw.circle(screen, (255,255,255), (500,150), 100, 3)
pygame.display.update()
running = False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
pygame.quit()