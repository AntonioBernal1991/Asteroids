import  pygame
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_limit = 3
        self.points = 0.1

        self.ship_speed = 1.5
        # Alien settings.
        #  alien_frequency controls how often a new alien appear.s
        #    Higher values -> more frequent aliens. Max = 1.0.
        self.asteroid_frequency = 0.008
        self.asteroid_speed = 3
        self.speedup_scale = 0.00005
        self.speedup_asteroid_scale = 0.00000005

    def initialize_dynamic_settings(self):
        """initializes the settings that change during the game"""
        self.ship_speed = 1.5
        self.asteroid_frequency = 0.008
        self.asteroid_speed = 3

    def increase_speed(self):
        """increases speed-settings"""
        self.ship_speed += self.speedup_scale
        self.asteroid_speed += self.speedup_scale













