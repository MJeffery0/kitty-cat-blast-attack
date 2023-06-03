import pygame
import random
import time
import WindowControl

#VARIABLES =======================================
# Enemy Values
enemy_WIDTH = 65
enemy_HEIGHT = 65 
enemy_IMAGES = ['Assets/enemy_mouse_brown.png', 'Assets/enemy_mouse_grey.png', 'Assets/enemy_mouse_white.png']
enemy_minSpeed = 0.5
enemy_maxSpeed = 1.2
enemy_maxSpawned = 10
enemy_SPAWNRATE = 1500

#Used to reset enemy stats
enemy_maxSpeed_START = 1.2
enemy_SPAWNRATE_START = 1500

#CLASS CONSTRUCTOR ==============================
# Defines enemy as a Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(random.choice(enemy_IMAGES)) #Uses list to make random enemy
        self.rect = self.image.get_rect()
        self.x = WindowControl.window_WIDTH - 30
        self.y = random.randint(0, WindowControl.window_HEIGHT)
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = random.uniform(enemy_minSpeed, enemy_maxSpeed) #Sets a random speed between minSpeed value and maxSpeed value

    # Reusable code to reset enemy values (based on section)
    def resetPosition(self):
        self.x = WindowControl.window_WIDTH
        self.y = random.randint(0, WindowControl.window_HEIGHT)

    def resetImage(self):
        self.image = self.image = pygame.image.load(random.choice(enemy_IMAGES))
        self.rect = self.image.get_rect()
    
    def resetSpeed(self):
        self.speed = random.uniform(enemy_minSpeed, enemy_maxSpeed)

    # Functions used to return enemy position values
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    # Used to define enemy movement
    def movement(self):
        self.x = self.x - self.speed #Moves self left based on speed
        self.rect.x = self.x
        self.rect.y = self.y

        # Destroys the sprite if it runs off the left side of the screen
        if (self.rect.right < 0):
            self.kill()

        # Ensures that the enemy does not spawn itself below the max window height
        if(self.rect.bottom > WindowControl.window_HEIGHT):
            self.y = self.y - enemy_HEIGHT


    def update(self):
        self.movement()