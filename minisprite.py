
 
import pygame
 
def main():
    pygame.init()
 
    screen_width, screen_height = 500, 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mini Sprite Adventure")
 
    x, y = 50, 50
    sprite_width, sprite_height = 60, 60
    speed = 4
 
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 125, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
 
    current_color = WHITE
 
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
        pressed = pygame.key.get_pressed()
 
        if pressed[pygame.K_LEFT]:
            x -= speed
        if pressed[pygame.K_RIGHT]:
            x += speed
        if pressed[pygame.K_UP]:
            y -= speed
        if pressed[pygame.K_DOWN]:
            y += speed
 
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)
 
        if x == 0:
            current_color = BLUE
        elif x == screen_width - sprite_width:
            current_color = YELLOW
        elif y == 0:
            current_color = RED
        elif y == screen_height - sprite_height:
            current_color = GREEN
        else:
            current_color = WHITE
 
        screen.fill(BLACK)
 
        pygame.draw.circle(screen, GREEN, (420, 320), 35)
        pygame.draw.circle(screen, BLUE, (80, 320), 35, 4)
 
        sprite_rect = pygame.Rect(x, y, sprite_width, sprite_height)
        pygame.draw.rect(screen, current_color, sprite_rect)
 
        pygame.display.flip()
        clock.tick(60)
 
    pygame.quit()