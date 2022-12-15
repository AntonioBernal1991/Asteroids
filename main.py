import sys
import  pygame
import json

from time import  sleep
from settings import Settings
from Ship import Ship
from asteroid import  Asteroid
from random import random
from background import Background
from gamestats import GameStats
from scoreboard import Scoreboard
from button import Button






class AsteroidGame:

    def __init__(self):
        pygame.init()
        #creates clock
        self.clock = pygame.time.Clock()
        self.starttime = 0
        self.currenttime = 0
        #enables sound and music effects
        pygame.mixer.init()
        pygame.mixer.music.load("images/Quarters_-8-bit (mp3cut.net) (1).mp3")
        self.music = pygame.mixer.music.play(-1)
        self.explosion2_fx = pygame.mixer.Sound("images/explosion2.wav")
        self.explosion2_fx.set_volume(10)
        #instances settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1500,1000))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_eight = self.screen.get_rect().height
        pygame.display.set_caption("Asteroid Aventure")

        self.stats = GameStats(self)
        self.ship = Ship(self,"images/rocket_small.png")
        self.sb = Scoreboard(self)
        self.bg = Background(self)
        self.asteroid = Asteroid(self)
        self.asteroids = pygame.sprite.Group()
        self.play_button = Button(self, "Play")


    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self._create_asteroid()
                self.asteroids.update()
                self._update_asteroids()
                self.ship.update()
                self.currenttime = pygame.time.get_ticks()
            self._update_screen()


    def _create_asteroid(self):
        """Create an alien, if conditions are right."""
        if random() < self.settings.asteroid_frequency:
            asteroid = Asteroid(self)
            self.asteroids.add(asteroid)


    def _update_asteroids(self):
        # Get rid of bullets that have disappeared.
        for asteroid in self.asteroids.copy():
            if asteroid.rect.right < self.screen.get_rect().left:
                self.asteroids.remove(asteroid)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_keydown_events(self,event):
        if event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._close_game()


    def _check_play_button(self, mouse_pos):
        """Inicialize a new game when the player  clics on Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Resets game statistics.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            #Gets rid of remaining bullets and aliens.
            self.asteroids.empty()
            #centers the ship.
            self.ship.center_ship()
            #Hides mouse.
            pygame.mouse.set_visible(False)


    def _check_keyup_events(self,event):
        if event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False
        elif event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False


    def _update_screen(self):
        if self.stats.game_active:
            self.bg.move_background()
            if self.starttime < self.currenttime:
                self.stats.score += self.settings.points
                self.sb.prep_score()
                self.sb.check_highest_score()
                self.settings.increase_speed()
                print(self.settings.asteroid_speed)

        self.asteroids.draw(self.screen)
        self.bg.blitme()
        self.sb.show_score()

        self.ship.blitme()
        if not self.stats.game_active:
            self.play_button.draw_button()

        self.asteroids.draw(self.screen)
        if pygame.sprite.spritecollideany(self.ship, self.asteroids):
            self._ship_hit()
        pygame.display.flip()


    def _ship_hit(self):
        """Respond to the impact of an alien to the ship"""
        if self.stats.game_active:
            self.explosion2_fx.play()
        if self.stats.ships_left > 0:
            # Decreses ships_left and actualizes scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # Get rid of the rest of aliens and bullets.
            self.asteroids.empty()
            # Creates a new fleet and centers the ship.
            self.ship.center_ship()
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _close_game(self):
        """Save high score and exit."""
        saved_high_score = self.stats.get_saved_high_score()
        if self.stats.high_score > saved_high_score:
            with open('high_score.json', 'w') as f:
                json.dump(self.stats.high_score, f)
        sys.exit()


if __name__=='__main__':
    asteroidgame = AsteroidGame()

    asteroidgame.run_game()

