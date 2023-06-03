import pygame
import WindowControl

#VARIABLES =====================================
# Player Character
player_CHARACTER = 'Assets/player_cat_orange.png'
player_WIDTH = 100
player_HEIGHT = 100

# Player Positioning
player_positionX = 30 #Used to determine general player position
player_positionY = 200
player_START_positionX = 30 #Used to reset player to starting position
player_START_positionY = 200

# Player Stats
player_HEALTH = 3
player_POWER = 1
player_SPEED = 2.0


#CLASS CONSTRUCTOR =================================
# Defines player as a Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, player_IMAGE):
        super().__init__()
        self.image = player_IMAGE #Sets player image
        self.x = player_positionX #Sets the sprite's X and Y coordinates
        self.y = player_positionY
        self.rect = self.image.get_rect()

    # Defines player movement and boundaries
    def movement(self):
        global player_positionX, player_positionY #Defined as a global variable to prevent errors
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #Key Pressed
            if player_positionX > 0:                #Boundary it can't exceed (SAME PATTERN FOR EACH KEY)
                player_positionX = player_positionX - player_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if player_positionX < WindowControl.window_WIDTH - player_WIDTH:
                player_positionX = player_positionX + player_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if player_positionY > 0: 
                player_positionY = player_positionY - player_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if player_positionY < WindowControl.window_HEIGHT - player_HEIGHT:
                player_positionY = player_positionY + player_SPEED


    def update(self):
        self.rect.x = player_positionX #Updates position based on movement inputs
        self.rect.y = player_positionY
        self.movement() #Performs movement on update