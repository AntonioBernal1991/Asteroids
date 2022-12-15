import json
class GameStats:
    """Follows stadistics from Alien Invasion"""

    def __init__(self,ai_game):
        """ Iniciates the stadistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        #Inicializes Alien invasion in active state
        self.game_active = True
        #Inicializes the game inactive state
        self.game_active = False
        #Highest score never should reset
        self.high_score = self.get_saved_high_score()
        self.level = 1

    def reset_stats(self):
        """Iniciates the stadistics that may change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_saved_high_score(self):
        """Gets high score from file, if it exists."""
        try:
            with open('high_score.json','r') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0

