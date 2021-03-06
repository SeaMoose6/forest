import pygame
import math
import random
##################################################
''''
At the beginning you will notice a 8-bit bat that you can control with your mouse. 
The goal of the game is to catch as many falling fireflies as possible while also avoiding
the poison berries that will fall along side and give -5 points. You will hear a crunch sound each time you 
eat a fly. And once 30 seconds are up, GAME OVER will be printed on the screen and 
your final score will be displayed. My best is 92.
Sometimes when run it will say "berry" is not defined but if you just try running it 
again it should work. 
'''
####################################################
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
BERRY = (169, 31, 173)
#pygame.Color.update(FOG, 206, 209, 222, 50)
x_left = 10
x_right = 10
y_up = 10
y_down = 10
font = pygame.font.SysFont('Times', 25, True, False)
font2 = pygame.font.SysFont('Times', 100, True, False)


PI = math.pi

display_width = 1000
display_height = 800

SIZE = (display_width, display_height)
FPS = 60


# functions
class Tree:
    def __init__(self, display, x, y, color, img, width=0):
        self.display = display
        self.x = x
        self.y = y
        self.color = color
        self.img = img
        self.bat_width = width

    def draw_tree(self):
        self.display.blit(self.img, [self.x, self.y])
        # pygame.draw.polygon(screen, self.color,
        #                     [(self.x, self.y+75),
        #                      (self.x+75, self.y),
        #                      (self.x+150, self.y+75)])
        # pygame.draw.polygon(screen, self.color,
        #                     [(self.x, self.y+125),
        #                      (self.x+75, self.y+50),
        #                      (self.x+150, self.y+125)])
        # pygame.draw.polygon(screen, self.color,
        #                     [(self.x, self.y+175),
        #                      (self.x+75, self.y+100),
        #                      (self.x+150, self.y+175)])
        # pygame.draw.polygon(screen, self.color,
        #                  [(self.x+50, self.y+175),
        #                   (self.x+100, self.y+175),
        #                   (self.x+100, self.y+675),
        #                   (self.x+50, self.y+675)])

class Bat:
    def __init__(self, display, x, y, width, score_add, score_sub, img, score=0):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.score_add = score_add
        self.score_sub = score_sub
        self.img = img
        self.score = score

    def draw_bat(self):
        self.display.blit(self.img, [self.x, self.y])
        # for num in range(10):
        #     pygame.draw.arc(screen, BLACK,
        #                 [self.x, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
        #                 0, PI-0.5, 5)
        #     pygame.draw.arc(screen, BLACK,
        #                 [self.x+25, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
        #                 0, PI, 5)
        #     pygame.draw.arc(screen, BLACK,
        #                 [self.x+50, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
        #                 0.5, PI, 5)
        #     pygame.draw.arc(screen, BLACK,
        #                 [self.x+100, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
        #                 0, PI-0.5, 5)
        #     pygame.draw.arc(screen, BLACK,
        #                 [self.x+125, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
        #                 0, PI, 5)
        #     pygame.draw.arc(screen, BLACK,
        #                 [self.x+150, self.y+(0.8 * num), self.x-self.x+30, self.y-self.y+30],
        #                 0.5, PI, 5)
        #
        # pygame.draw.circle(screen, BLACK,
        #                    (self.x+90, self.y), 25)
        # pygame.draw.circle(screen, BLACK,
        #                    (self.x+90, self.y-30), 20)
        # pygame.draw.polygon(screen, BLACK,
        #                     [(self.x, self.y+5), (self.x+50, self.y-20),
        #                     (self.x+100, self.y+5)])
        # pygame.draw.polygon(screen, BLACK,
        #                     [(self.x+100, self.y+5), (self.x+130, self.y-20),
        #                     (self.x+175, self.y+5)])
        # pygame.draw.polygon(screen, BLACK,
        #                     [(self.x+75, self.y-40),
        #                     (self.x+80, self.y-55),
        #                     (self.x+95, self.y-50)])
        # pygame.draw.polygon(screen, BLACK,
        #                     [(self.x+90, self.y-50),
        #                     (self.x+100, self.y-55),
        #                     (self.x+105, self.y-40)])
        # pygame.draw.circle(screen, RED,
        #                    (self.x+85, self.y-35), 4)
        # pygame.draw.circle(screen, RED,
        #                    (self.x+95, self.y-35), 4)
    def is_collided(self, other):
        if (self.x+20 <= other.x <= self.x+self.width-20) and \
        (self.y+20 <= other.y <= self.y + self.width-40):

            if other == fly:
                self.score += self.score_add
                crunch_sound.play()
                other.x = random.randint(0, 1000)
                other.y = 0
                print(self.score)
            if other == berry:
                self.score -= self.score_sub
                other.x = random.randint(0, 1000)
                other.y = random.randint(-2000, 0)

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
    def move_fly(self, other):
        if 0 < self.x < display_width:
            self.speed = random.randint(-5, 5)
        self.x += self.speed

        if 0 < self.y < display_height:
            self.speed = random.randint(-5, 12)
        self.y += self.speed
        if self.x < 0:
            self.x += 10
        if self.x > display_width:
            self.x -= 10
        if self.y < 0:
            self.y += 10
        if self.y > display_height:
            self.x = random.randint(0, 1000)
            self.y = 0
            other.score -= other.score_add

class Berry:
    def __init__(self, x, y, color, width, speed=0):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.speed = speed

    def draw_berry(self):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.width)
    def move_berry(self):
        if 0 < self.x < display_width:
            self.speed = random.randint(-5, 5)
        self.x += self.speed

        if 0 < self.y < display_height:
            self.speed = random.randint(-5, 12)
        self.y += self.speed
        if self.x < 0:
            self.x += 10
        if self.x > display_width:
            self.x -= 10
        if self.y < 0:
            self.y += 10
        if self.y > display_height:
            self.x = random.randint(0, 1000)
            self.y = random.randint(-2000, 0)

class Score:
    def __init__(self, time):
        self.time = time

    def draw_score(self, other):
        text = font.render(f"Score = {other.score}", True, WHITE)
        screen.blit(text, (50, 25))

    def draw_time(self):
        timer = font.render(f"Time = {self.time/1000}", True, WHITE)
        screen.blit(timer, (50, 50))

    def draw_game_over(self):
        screen.fill(SKY)
        game_over = font2.render("GAME OVER", True, RED)
        screen.blit(game_over, (150, 300))

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
bat_img = pygame.image.load("oie_mQ18gW90tuKu.png")
game_over_sound = pygame.mixer.Sound("game_over_bad_chest.wav")
background_img = pygame.image.load("oie_8153311knEW6vqY.png")
crunch_sound = pygame.mixer.Sound("crunch.1.ogg")
tree_img = pygame.image.load("oie_101454546xf2O7k6.png")

clock = pygame.time.Clock()

running = True


trees1 = [Tree(screen, random.randint(-100, 250), random.randint(0, 200), BLACK, tree_img)
         for num in range(5)]

trees2 = [Tree(screen, random.randint(600, 1000), random.randint(0, 200), BLACK, tree_img)
         for num in range(5)]

bat = Bat(screen, 400, 1000,175, 1, 5, bat_img)

moon = Moon(200, 300, 1)

fly_list = []
for i in range(10):
    x_cord = random.randrange(0, display_width, 5)
    random_y = random.randrange(100, 300, 5)
    fly_list.append(Fire_Fly(x_cord, random_y, FLY, 5))

berries_list = []
for i in range(3):
    x_cord = random.randrange(0, display_width, 5)
    random_y = random.randrange(100, 300, 5)
    berries_list.append(Berry(x_cord, random_y, BERRY, 5))

text = font.render(f"Score = {bat.score}", True, WHITE)




pygame.mouse.set_visible(False)

while running:

    pos = pygame.mouse.get_pos()
    bat.x = pos[0]-.5*bat.width
    bat.y = pos[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_img, [0, 0])
    score = Score(pygame.time.get_ticks())

    for tree in trees1:
        tree.draw_tree()

    for tree in trees2:
        tree.draw_tree()

    for fly in fly_list:
        fly.draw_fly()
        fly.move_fly(bat)
        bat.is_collided(fly)

    for berry in berries_list:
        berry.draw_berry()
        berry.move_berry()
        bat.is_collided(berry)


    bat.draw_bat()

    score.draw_score(bat)
    score.draw_time()
    if int(score.time) > 30000:
        game_over_sound.play()
        score.draw_game_over()
        score.draw_score(bat)
        timer = font.render(f"Time = {30000}", True, WHITE)
        screen.blit(timer, (50, 50))
        bat.score_add = 0
        bat.score_sub = 0
        score.time = 30000/1000


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
