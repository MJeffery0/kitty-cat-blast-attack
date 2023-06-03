import pygame
import random
import Player
import Projectile



#VARIABLES ============================================
# Buff images
buff_heal = 'Assets/buff_heal.png'
buff_projectile_firerate = 'Assets/buff_projectile_firerate.png'
buff_projectile_speed = 'Assets/buff_projectile_speed.png'
buff_player_speed = 'Assets/buff_speed.png'

buff_IMAGES = [buff_heal, buff_projectile_firerate, buff_projectile_speed, buff_player_speed]
buff_SPEED = 0.8


#CLASS CONSTRUCTOR ==============================
# Defines buff as Sprite
class Buff(pygame.sprite.Sprite):
    def __init__(self, buff_x, buff_y):
        super().__init__()
        self.imagePath = random.choice(buff_IMAGES)
        self.image = pygame.image.load(self.imagePath) #Uses list to make random enemy
        self.rect = self.image.get_rect()
        self.x = buff_x
        self.y = buff_y
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = buff_SPEED

    # BUFF MOVEMENT
    def movement(self):
        self.x = self.x - self.speed #Moves self left based on speed
        self.rect.x = self.x
        self.rect.y = self.y

        # Destroys the sprite if it runs off the left side of the screen
        if (self.rect.right < 0):
            self.kill()

    def update(self):
        self.movement()




# BUFF EFFECTS ((CONTROLLER)) =============================================
 #This heals the player by 1 health
def healPlayer():
    if Player.player_HEALTH < 3:
        Player.player_HEALTH = Player.player_HEALTH + 1
        print("Health increased to " + str(Player.player_HEALTH))

def buffProjectileFirerate():
    if Projectile.projectile_FIRERATE > 300:
        Projectile.projectile_FIRERATE = Projectile.projectile_FIRERATE - 50
        print("Reducing time between shots by 50. Currently: " + str(Projectile.projectile_FIRERATE))
    if Projectile.projectile_FIRERATE <= 300:
        print("Max projectile speed reached.")
        
def buffProjectileSpeed():
    Projectile.projectile_SPEED = Projectile.projectile_SPEED + 0.25
    print("Current projectile speed: " + str(Projectile.projectile_SPEED))

def buffPlayerSpeed():
    Player.player_SPEED = Player.player_SPEED + 0.1
    print("Current player speed: " + str(Player.player_SPEED))

# Used to apply buff mechanics under one function
def applyBuff(image):
    if image == buff_heal:
        healPlayer()
    if image == buff_projectile_firerate:
        buffProjectileFirerate()
    if image == buff_projectile_speed:
        buffProjectileSpeed()
    if image == buff_player_speed:
        buffPlayerSpeed()
