import math
import random
import pygame

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1440

PLAYER_START_X = 370
PLAYER_START_Y = 600
PLAYER_SIZE = 64
PLAYER_SPEED = 5

ENEMY_SIZE = 64
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 5

BULLET_SIZE = 32
BULLET_SPEED_Y = 10

COLLISION_DISTANCE = 40
GAME_OVER_Y = 340
NUM_OF_ENEMIES = 6


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")


# Background
background = pygame.image.load("black.webp").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Player
player_img = pygame.image.load("player.webp").convert_alpha()
player_img = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))

player_x = PLAYER_START_X
player_y = PLAYER_START_Y
player_x_change = 0


# Enemies
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

for _ in range(NUM_OF_ENEMIES):
    img = pygame.image.load("enemy.webp").convert_alpha()
    img = pygame.transform.scale(img, (ENEMY_SIZE, ENEMY_SIZE))

    enemy_img.append(img)
    enemy_x.append(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE))
    enemy_y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_SPEED_Y)


# Bullet
bullet_img = pygame.image.load("bullet.webp").convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (BULLET_SIZE, BULLET_SIZE))

bullet_x = 0
bullet_y = PLAYER_START_Y
bullet_y_change = BULLET_SPEED_Y
bullet_state = "ready"


# Score
score_value = 0

font = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.Font("freesansbold.ttf", 64)

text_x = 10
text_y = 10


def show_score(x, y):
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))

    text_rect = over_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    )

    screen.blit(over_text, text_rect)


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state

    bullet_state = "fire"

    bullet_x_offset = (PLAYER_SIZE - BULLET_SIZE) // 2
    screen.blit(bullet_img, (x + bullet_x_offset, y))


def is_collision(enemy_x_pos, enemy_y_pos, bullet_x_pos, bullet_y_pos):
    enemy_center_x = enemy_x_pos + ENEMY_SIZE / 2
    enemy_center_y = enemy_y_pos + ENEMY_SIZE / 2

    bullet_center_x = bullet_x_pos + BULLET_SIZE / 2
    bullet_center_y = bullet_y_pos + BULLET_SIZE / 2

    distance = math.sqrt(
        (enemy_center_x - bullet_center_x) ** 2
        + (enemy_center_y - bullet_center_y) ** 2
    )

    return distance < COLLISION_DISTANCE


running = True
game_over = False

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -PLAYER_SPEED

            elif event.key == pygame.K_RIGHT:
                player_x_change = PLAYER_SPEED

            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                bullet_y = player_y
                bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_x_change = 0


    # Player movement
    player_x += player_x_change

    player_x = max(
        0,
        min(player_x, SCREEN_WIDTH - PLAYER_SIZE)
    )


    if not game_over:
        # Enemy movement and collision
        for i in range(NUM_OF_ENEMIES):

            if enemy_y[i] > GAME_OVER_Y:
                game_over = True
                break

            enemy_x[i] += enemy_x_change[i]

            if enemy_x[i] <= 0:
                enemy_x[i] = 0
                enemy_x_change[i] *= -1
                enemy_y[i] += enemy_y_change[i]

            elif enemy_x[i] >= SCREEN_WIDTH - ENEMY_SIZE:
                enemy_x[i] = SCREEN_WIDTH - ENEMY_SIZE
                enemy_x_change[i] *= -1
                enemy_y[i] += enemy_y_change[i]

            if (
                bullet_state == "fire"
                and is_collision(
                    enemy_x[i],
                    enemy_y[i],
                    bullet_x,
                    bullet_y,
                )
            ):
                bullet_y = PLAYER_START_Y
                bullet_state = "ready"

                score_value += 1

                enemy_x[i] = random.randint(
                    0,
                    SCREEN_WIDTH - ENEMY_SIZE,
                )

                enemy_y[i] = random.randint(
                    ENEMY_START_Y_MIN,
                    ENEMY_START_Y_MAX,
                )

            enemy(enemy_x[i], enemy_y[i], i)


        # Bullet movement
        if bullet_state == "fire":
            bullet_y -= bullet_y_change

            if bullet_y <= 0:
                bullet_y = PLAYER_START_Y
                bullet_state = "ready"
            else:
                fire_bullet(bullet_x, bullet_y)


    player(player_x, player_y)
    show_score(text_x, text_y)

    if game_over:
        game_over_text()

    pygame.display.update()
    clock.tick(140)

pygame.quit()