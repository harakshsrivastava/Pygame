import pygame
import random
 
pygame.init()
 
CAR_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
SIGNAL_CHANGE_EVENT = pygame.USEREVENT + 2
 
ROAD = pygame.Color("darkgray")
WHITE = pygame.Color("white")
YELLOW = pygame.Color("yellow")
BLUE = pygame.Color("blue")
ORANGE = pygame.Color("orange")
 
RED = pygame.Color("red")
GREEN = pygame.Color("green")
 
 
class Car(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
        self.velocity = [3, 0]
 
    def update(self):
        self.rect.move_ip(self.velocity)
 
        sensor_triggered = False
 
        if self.rect.left <= 0 or self.rect.right >= 600:
            self.velocity[0] = -self.velocity[0]
 
            sensor_triggered = True
 
        if sensor_triggered:
            pygame.event.post(
                pygame.event.Event(CAR_COLOR_CHANGE_EVENT)
            )
 
            pygame.event.post(
                pygame.event.Event(SIGNAL_CHANGE_EVENT)
            )
 
    def change_color(self):
        self.image.fill(
            random.choice([WHITE, YELLOW, BLUE, ORANGE])
        )
 
 
def change_signal():
    global signal_color
 
    if signal_color == RED:
        signal_color = GREEN
    else:
        signal_color = RED
 
 
all_sprites = pygame.sprite.Group()
 
car = Car(WHITE, 70, 35)
 
car.rect.x = 50
car.rect.y = 300
 
all_sprites.add(car)
 
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Smart Traffic Signal Simulator")
 
signal_color = RED
 
clock = pygame.time.Clock()
 
running = True
 
while running:
 
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            running = False
 
        elif event.type == CAR_COLOR_CHANGE_EVENT:
            car.change_color()
 
        elif event.type == SIGNAL_CHANGE_EVENT:
            change_signal()
 
    all_sprites.update()
 
    screen.fill(ROAD)
 
    for x in range(0, 600, 80):
        pygame.draw.rect(
            screen,
            WHITE,
            (x, 345, 45, 5)
        )
 
    pygame.draw.rect(
        screen,
        pygame.Color("black"),
        (275, 40, 50, 90)
    )
 
    pygame.draw.circle(
        screen,
        signal_color,
        (300, 85),
        20
    )
 
    all_sprites.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
