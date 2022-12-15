import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,asteroidgame,imagee):
        super().__init__()
        self.screen = asteroidgame.screen
        self.settings = asteroidgame.settings

        self.screen_rect = asteroidgame.screen.get_rect()

        self.image = pygame.image.load(imagee).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)


        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_up:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down:
            self.rect.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):

        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        """Centers the ship on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)


