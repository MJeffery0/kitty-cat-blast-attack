import pygame

#VARIABLES =====================================
# insert here



#CLASS CONSTRUCTOR =================================
# Defines Button as a Sprite
class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    #Used to change button image
    def setImage(self, image):
        self.image = image