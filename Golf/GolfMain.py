
import sys
import os
import time
import pygame


class Scenario(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.image.load(r'assets\cenario.jfif')


class Player(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.life = 100
        self.image = pygame.image.load(r'assets\player.png')
        self.hitbox = (self.x, self.y, self.height, 30)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.height, 30)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class Ball(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.center = (self.x/2, self.y/2)
        self.image = pygame.image.load(r'assets\ball.jpg')
        self.hitbox = (self.x, self.y - 30 + self.width, self.height, 100)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y - 100 + self.width - 20, self.height, 110)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        self.center = (self.x/2, self.y/2)

    def move(self):
        if self.x > -110 and self.speed > 0:
            self.x -= self.speed

    def hit(self):
        print("enemy hit")
        return 1


# -------------player props-----------
player_init_X = 100
player_init_y = 100
player_height = 30
player_width = 31
player_speed = 5

# ------------- ball props---------------
ball_init_X = 150
ball_init_y = 150
ball_height = 10
ball_width = 10
ball_speed = 50

#-------------- inicializando objetos-------------------------------
player = Player(player_init_X, player_init_y, player_height, player_width, player_speed)
ball = Ball(ball_init_X, ball_init_y, ball_height, ball_width, ball_speed)

pygame.init()
screen_width, screen_height = 750, 750
screen = pygame.display.set_mode((screen_width, screen_height))

while 1:
    while 1:
        # *********updates the screen*************
        # clear the screen before drawing again
        pygame.time.delay(100)
        screen.fill(1)
        # update the screen
        # screen.blit(heroShip.image, (heroShip.x, heroShip.y))
        player.draw(screen)
        pygame.display.update()