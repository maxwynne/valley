import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # general set up
        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)

        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        # decide how fast the player is
        self.speed = 200

    def input(self):
        # check which key is getting pressed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        # if we are pressing no buttons, not moving on vertical axis
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self,dt):

        # normalising a vector - make sure direction of vector is always 1
        # check if vector has length
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement

        # vertical movement

        # lines important for collision mechanics
        self.pos.x += self.direction * self.speed * dt
        self.rect.center = self.pos

    # when to call input method
    def update(self, dt):
        self.input()
        self.move(dt)
