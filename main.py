import pygame
import math
import random

#in terminal "pip install pygame"

pygame.init()

# constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GROUND_BLACK = (23, 24, 28)
BACK_BLACK = (5, 5, 5)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
SKY = (8, 37, 112)
FOG = (206, 209, 222)


PI = math.pi

SIZE = (1000, 800)
FPS = 60


# functions
class Tree:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw_tree(self):
        pygame.draw.polygon(screen, self.color,
                            [(self.x, self.y+75),
                             (self.x+75, self.y),
                             (self.x+150, self.y+75)])
        pygame.draw.polygon(screen, self.color,
                            [(self.x, self.y+125),
                             (self.x+75, self.y+50),
                             (self.x+150, self.y+125)])
        pygame.draw.polygon(screen, self.color,
                            [(self.x, self.y+175),
                             (self.x+75, self.y+100),
                             (self.x+150, self.y+175)])
        pygame.draw.polygon(screen, self.color,
                         [(self.x+50, self.y+175),
                          (self.x+100, self.y+175),
                          (self.x+100, self.y+675),
                          (self.x+50, self.y+675)])

class Fog:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw_fog(self):
        pygame.draw.arc(screen, self.color,
                        [self.x-150, self.y, self.x+250, self.y],
                        0, PI, 50)

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("The Forest")

clock = pygame.time.Clock()

running = True


trees = [Tree(random.randint(-100, 900), random.randint(0, 200), BLACK)
         for num in range(10)]

background_trees = [Tree(random.randint(-100, 900), random.randint(0, 100), BACK_BLACK)
         for num in range(10)]

fog = Fog(200, 300, FOG)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)
    pygame.draw.rect(screen, GROUND_BLACK, [0, 450, 1000, 800])

    for tree in background_trees:
        tree.draw_tree()
    for tree in trees:
        tree.draw_tree()

    fog.draw_fog()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
