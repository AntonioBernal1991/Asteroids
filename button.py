import pygame.font

class Button:
    def __init__(self,ai_game,msg):
        """iniciates the atriubutes of the button"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        #Configurates the dimensions and properties of the button
        self.width, self.height = 200,50
        self.button_color = (248,8,8)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #Creates the object rect of the button and centers it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center =self.screen_rect.center

        #only you have to prepare once the message in on the button
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """converts msg into a renderized image and centers the text in the button """
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draws a button in blank and after the message.
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
