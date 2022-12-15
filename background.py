import pygame

class Background:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bgimage = pygame.image.load('images/space_seam.png').convert_alpha()
        self.rectBGimg = self.bgimage.get_rect()
        self.bgY1 = 0
        self.bgX1 = 0
        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width
        self.moving_speed = 1.5

    def move_background(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def blitme(self):
        self.screen.blit(self.bgimage, (self.bgX1, self.bgY1))
        self.screen.blit(self.bgimage, (self.bgX2, self.bgY2))


