import pygame
import math
import random

#in terminal "pip install pygame"

pygame.init()

# constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GROUND_BLACK = (13, 14, 20)
BACK_BLACK = (5, 5, 5)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
SKY = (5, 5, 36)
FOG = pygame.Color(206, 209, 222, 50)
FLY = (242, 198, 0)
#pygame.Color.update(FOG, 206, 209, 222, 50)
x_left = 10
x_right = 10
y_up = 10
y_down = 10
font = pygame.font.SysFont('Times', 25, True, False)

PI = math.pi

display_width = 1000
display_height = 800

SIZE = (display_width, display_height)
FPS = 60


# functions
class Tree:
    def __init__(self, x, y, color, width=0):
        self.x = x
        self.y = y
        self.color = color
        self.bat_width = width

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
    def __init__(self, x, y, width, score=0):
        self.x = x
        self.y = y
        self.width = width
        self.score = score

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
    # def move_bat(self):
    #     self.y-=5
    #     if self.y <= -1000:
    #         self.y = 1000
    def is_collided(self, other):
        if (self.x <= other.x <= self.x+self.width) and \
        (self.y-60 <= other.y <= self.y-140+ self.width):

            self.score += 1
            other.x = random.randint(0, 1000)
            other.y = 0
            print(self.score)

class Fire_Fly:
    def __init__(self, x, y, color, width, speed=0):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.speed = speed

    def draw_fly(self):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.width)
    def move_fly(self):
        if 0 < self.x < display_width:
            self.speed = random.randint(-5, 5)
        self.x += self.speed

        if 0 < self.y < display_height:
            self.speed = random.randint(-5, 7)
        self.y += self.speed
        if self.x < 0:
            self.x += 10
        if self.x > display_width:
            self.x -= 10
        if self.y < 0:
            self.y += 10
        if self.y > display_height:
            self.y -= 10

class Score:
    def __init__(self):
        pass
    def draw_score(self, other):
        font.render(f"Score = {other.score}", True, WHITE)
        screen.blit(text, (50, 25))



class Moon:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def draw_moon(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 50)

    def move_moon(self):
        self.y -= self.speed
        self.x += self.speed/2
        if self.y <= 50:
            self.speed = 0





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

bat = Bat(400, 1000,175)

moon = Moon(200, 300, 1)

fly_list = []
for i in range(10):
    x_cord = random.randrange(0, display_width, 5)
    random_y = random.randrange(100, 300, 5)
    fly_list.append(Fire_Fly(x_cord, random_y, FLY, 5))

score = Score()

text = font.render(f"Score = {bat.score}", True, WHITE)




pygame.mouse.set_visible(False)

while running:

    pos = pygame.mouse.get_pos()
    bat.x = pos[0]-.5*bat.width
    bat.y = pos[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)
    pygame.draw.rect(screen, GROUND_BLACK, [0, 450, 1000, 800])

    #eyes.draw_eyes()
    #eyes.move_eyes_right()

    moon.draw_moon()
    moon.move_moon()

    for tree in background_trees1:
        tree.draw_tree()
    for tree in trees1:
        tree.draw_tree()

    for tree in background_trees2:
        tree.draw_tree()
    for tree in trees2:
        tree.draw_tree()

    for fly in fly_list:
        fly.draw_fly()
        fly.move_fly()
        bat.is_collided(fly)


    bat.draw_bat()

    score.draw_score(bat)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
