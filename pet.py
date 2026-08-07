import pygame
import random


pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
FPS = 60
SPEED = 5
FONT_SIZE = 36

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")
clock = pygame.time.Clock()

background = pygame.image.load("pet.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("arial", FONT_SIZE)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.rect.x = max(0, min(SCREEN_WIDTH - self.rect.width, self.rect.x + dx))
        self.rect.y = max(0, min(SCREEN_HEIGHT - self.rect.height, self.rect.y + dy))

pet = GameSprite((0, 128, 255), 30, 30, 100, 200)   
food = GameSprite((255, 100, 0), 20, 20, 350, 200)  

all_sprites = pygame.sprite.Group()
all_sprites.add(pet)
all_sprites.add(food)

food_collected = False
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if keys[pygame.K_LEFT]:
        dx -= SPEED
    if keys[pygame.K_RIGHT]:
        dx += SPEED
    if keys[pygame.K_UP]:
        dy -= SPEED
    if keys[pygame.K_DOWN]:
        dy += SPEED

    pet.move(dx, dy)
    if not food_collected and pet.rect.colliderect(food.rect):
        food.kill()  
        food_collected = True

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    if food_collected:
        text_surface = font.render("Food Collected!", True, (255, 255, 255))
        text_x = (SCREEN_WIDTH - text_surface.get_width()) // 2
        text_y = (SCREEN_HEIGHT - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()