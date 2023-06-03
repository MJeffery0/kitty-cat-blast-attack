import pygame
import WindowControl
import Player

#VARIABLES ====================================
# Projectile Basics
projectile_IMAGE = 'Assets/projectile_fire.png'
projectile_WIDTH = 60
projectile_HEIGHT = 30

# Projectile Stats
projectile_SPEED = 2.5
projectile_POWER = 1
projectile_PIERCING = 1 # CAN BE USED TO PIERCE THROUGH MORE THAN ONE MOUSE
projectile_FIRERATE = 1000


#CLASS CONSTRUCTOR ============================
# Defines a Projectile object
class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(projectile_IMAGE)
        self.rect = self.image.get_rect()
        self.x = Player.player_positionX + 30
        self.rect.x = self.x
        self.rect.y = Player.player_positionY + 25
        self.speed = projectile_SPEED

    def update(self):
        self.x = self.x + self.speed #Moves the sprite automatically to the right once activated, based on SPEED
        self.rect.x = self.x 

        if self.rect.x > WindowControl.window_WIDTH: #This kills the projectile sprite once it flies off screen
            self.kill()