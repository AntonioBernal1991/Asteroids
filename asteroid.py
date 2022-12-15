from random import randint

import pygame
from pygame.sprite import Sprite


class Asteroid(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, asteroidgame):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = asteroidgame.screen
        self.settings = asteroidgame.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/asteroid2.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Start each new alien at a random position on the right side
        #   of the screen.
        self.rect.left = self.screen.get_rect().right
        # The farthest down the screen we'll place the alien is the height
        #   of the screen, minus the height of the alien.

        self.rect.top = randint(0, 1000)

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien steadily to the left."""
        self.x -= self.settings.asteroid_speed
        self.rect.x = self.x