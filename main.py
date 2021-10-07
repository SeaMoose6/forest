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
FOG = pygame.Color(206, 209, 222, 50)
#pygame.Color.update(FOG, 206, 209, 222, 50)


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

class Bat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_bat(self):
        for num in range(10):
            pygame.draw.arc(screen, BLACK,
                        [self.x, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
                        0, PI-0.5, 5)
            pygame.draw.arc(screen, BLACK,
                        [self.x+25, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
                        0, PI, 5)
            pygame.draw.arc(screen, BLACK,
                        [self.x+50, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
                        0.5, PI, 5)
            pygame.draw.arc(screen, BLACK,
                        [self.x+100, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
                        0, PI-0.5, 5)
            pygame.draw.arc(screen, BLACK,
                        [self.x+125, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
                        0, PI, 5)
            pygame.draw.arc(screen, BLACK,
                        [self.x+150, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
                        0.5, PI, 5)

        pygame.draw.circle(screen, BLACK,
                           (self.x+90, self.y), 25)
        pygame.draw.circle(screen, BLACK,
                           (self.x+90, self.y-30), 20)
        pygame.draw.polygon(screen, BLACK,
                            [(self.x, self.y+5), (self.x+50, self.y-20),
                            (self.x+100, self.y+5)])
        pygame.draw.polygon(screen, BLACK,
                            [(self.x+100, self.y+5), (self.x+130, self.y-20),
                            (self.x+175, self.y+5)])
        pygame.draw.polygon(screen, BLACK,
                            [(self.x+75, self.y-40),
                            (self.x+80, self.y-55),
                            (self.x+95, self.y-50)])
        pygame.draw.polygon(screen, BLACK,
                            [(self.x+90, self.y-50),
                            (self.x+100, self.y-55),
                            (self.x+105, self.y-40)])
        pygame.draw.circle(screen, RED,
                           (self.x+85, self.y-35), 4)
        pygame.draw.circle(screen, RED,
                           (self.x+95, self.y-35), 4)
    def move_bat(self):
        self.y-=3
        if self.y <= 0:
            self.y = 1000
pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("The Forest")

clock = pygame.time.Clock()

running = True


trees1 = [Tree(random.randint(-100, 250), random.randint(0, 200), BLACK)
         for num in range(5)]

background_trees1 = [Tree(random.randint(-100, 250), random.randint(0, 100), BACK_BLACK)
         for num in range(5)]

trees2 = [Tree(random.randint(600, 1000), random.randint(0, 200), BLACK)
         for num in range(5)]

background_trees2 = [Tree(random.randint(600, 1000), random.randint(0, 100), BACK_BLACK)
         for num in range(5)]

fog = Fog(200, 300, FOG)

bat = Bat(400, 1000)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)
    pygame.draw.rect(screen, GROUND_BLACK, [0, 450, 1000, 800])

    for tree in background_trees1:
        tree.draw_tree()
    for tree in trees1:
        tree.draw_tree()

    for tree in background_trees2:
        tree.draw_tree()
    for tree in trees2:
        tree.draw_tree()

    #fog.draw_fog()



    bat.draw_bat()
    bat.move_bat()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
