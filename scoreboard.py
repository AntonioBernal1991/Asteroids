import pygame.font
from pygame.sprite import Group
from Ship import Ship



class Scoreboard:
    """A class to show punctuation"""
    def __init__(self,ai_game):
        """initializes atributes form punctuation"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        #Set the font
        self.font = pygame.font.SysFont(None, 48)

        #Prepares the image of the final punctuation.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        """converts score on a renderized image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)

        self.score_image = self.font.render(score_str,True,
          (239,0,2), (1,25,48))

        #Shows punctuation at the right upper part of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draws score on the screen"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """converts highest score into an renderized image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
              (239,0,2),(1,25,48))
        #Center highest score on the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_highest_score(self):
        """looks for a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    def prep_level(self):
        """Converts the level on a renderized image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str,True,
             (239,0,2),(1,25,48))
        #Puts level below the scoreboard
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 1

    def prep_ships(self):
        """Shows how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game,"images/rocket_small_lifes.png")
            ship.rect.x = 10 + (ship_number * (ship.rect.width * 1.1))
            ship.rect.y = 10
            self.ships.add(ship)

