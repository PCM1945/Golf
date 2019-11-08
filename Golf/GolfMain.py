
import sys
import os
import time
import pygame


class Background(object):
    def __init__(self):
        self.image = pygame.image.load(r'assets\background 1279 x 720.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]

    def draw(self, window):
        window.fill([255, 255, 255])
        window.blit(self.image, self.rect)


class Ball(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.center = (self.x/2, self.y/2)
        self.image = pygame.image.load(r'assets\asteroid1.png')
        self.hitbox = (self.x, self.y + self.width, self.height, 60)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.height, self.width - 7)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        self.center = (self.x/2, self.y/2)

    def move(self):
        if self.x > -110 and self.speed > 0:
            self.x -= self.speed


# -------------player props-----------
player_init_X = 1279
player_init_y = 720
player_height = 30
player_width = 31
player_speed = 5

# ------------- ball props---------------
ball_init_X = 150
ball_init_y = 150
ball_height = 70
ball_width = 60
ball_speed = 50

# -------------- inicializando objetos-------------------------------
screen_width, screen_height = 750, 750
ball = Ball(ball_init_X, ball_init_y, ball_height, ball_width, ball_speed)
background = Background()
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

while 1:
    # *********updates the screen*************
    # clear the screen before drawing again
    pygame.time.delay(100)
    screen.fill(1)
    background.draw(screen)
    # update the screen
    # screen.blit(heroShip.image, (heroShip.x, heroShip.y))
    ball.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():  # Loop through a list of events
        if event.type == pygame.QUIT:  # See if the user clicks the red x
            run = False  # End the loop
            pygame.quit()  # Quit the game
            quit()
