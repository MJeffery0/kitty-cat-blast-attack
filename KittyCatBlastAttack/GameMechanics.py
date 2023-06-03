import pygame
import Player
import Projectile
import Enemy
import WindowControl
import Score
import Button
import Menus
import Buff
import random

#VARIABLES =======================================
# Character Groups ---------
# Player Sprite Group
player = Player.Player(pygame.image.load(Player.player_CHARACTER))
player_GROUP = pygame.sprite.GroupSingle()
player_GROUP.add(player)

#Player Health display
health_1 = Button.Button(pygame.image.load("Assets/health_visible.png"), 50, 40)
health_2 = Button.Button(pygame.image.load("Assets/health_visible.png"), 110, 40)
health_3 = Button.Button(pygame.image.load("Assets/health_visible.png"), 170, 40)
health_GROUP = pygame.sprite.Group()
health_GROUP.add(health_1)
health_GROUP.add(health_2)
health_GROUP.add(health_3)

# Enemy Sprite Group
enemy_GROUP = pygame.sprite.Group()

# Projectile Sprite Group
projectile_GROUP = pygame.sprite.Group()

# Buff Sprite Group
buff_GROUP = pygame.sprite.Group()

# Time Keeping
# --- Used to help define sprite spawn timings
time_projectile_OLD = 0
time_enemy_OLD = 0

# Game difficulty
# --- Used to determine what level of difficulty the game is at
gameDifficulty = 0


#MECHANICS =======================================
# Colliding with the enemy mouse will remove 1HP from the player and remove the enemy
def collideWithMouse():
    collision = pygame.sprite.groupcollide(player_GROUP, enemy_GROUP, False, True)
    if collision:
        Player.player_HEALTH = Player.player_HEALTH - 1
        print('Current Health: ' + str(Player.player_HEALTH))

# When a projectile collides with an enemy, the player is awarded a point to their score
def killMouse():
    collision = pygame.sprite.groupcollide(projectile_GROUP, enemy_GROUP, True, True) #Checking for collision between a projectile and an enemy
    if collision:
        Score.addScore()
        for enemy_sprite in collision.values(): #This is used to get and return the enemy X and Y values of the collision enemy
            for enemy in enemy_sprite:
                #print(f"Enemy position: ({enemy.rect.x}, {enemy.rect.y})")
                if random.random() < 0.2:
                    spawnBuff(enemy.rect.x, enemy.rect.y) #Spawns a buff using the X/Y of enemy

# Firing the Player projectile
# -- This function uses TICKS to test how long until a new projectile can be fired
def fireProjectile():
    keys = pygame.key.get_pressed()
    clicked = pygame.mouse.get_pressed()
    global time_projectile_OLD

    if keys[pygame.K_SPACE] or clicked[0]: #Checking if SPACEBAR or LEFT-CLICK are pressed
        time_projectile_NEW = pygame.time.get_ticks()
        if time_projectile_NEW - time_projectile_OLD > Projectile.projectile_FIRERATE:
            time_projectile_OLD = time_projectile_NEW
            projectile = Projectile.Projectile()
            projectile_GROUP.add(projectile)  

# Enemy Spawning
def spawnEnemy():
    global time_enemy_OLD #Recorded static number; used to compare against the NEW timer and spawn rate
    time_enemy_NEW = pygame.time.get_ticks() #Regularly ticking number
    
    if  time_enemy_NEW - time_enemy_OLD > Enemy.enemy_SPAWNRATE:
        if len(enemy_GROUP.sprites()) < Enemy.enemy_maxSpawned:
            time_enemy_OLD = time_enemy_NEW
            enemy = Enemy.Enemy()
            enemy_GROUP.add(enemy)
            if gameDifficulty >= 5: #Adds a second spawn after reaching Rank 5 difficulty (Achieved at score of 50)
                enemy2 = Enemy.Enemy()
                enemy_GROUP.add(enemy2)
                print("Spawning second enemy")
                if gameDifficulty >= 10: #Adds a third spawn after reaching Rank 10 difficulty (Achieved at score of 100)
                    enemy3 = Enemy.Enemy()
                    enemy_GROUP.add(enemy3)
                    print("Spawning a third enemy")

# Difficulty changes
# --- Increases difficulty based on Player score (MAX RANK 20)
def increaseDifficulty():
    global gameDifficulty
    if Score.score_CURRENT == Score.score_RANGE: #Takes the current score and compares it with the current score range (multiple of 10)
        if Score.score_CURRENT <= 200: #Determines how high of a score it scales with
            gameDifficulty = gameDifficulty + 1
            if Enemy.enemy_maxSpeed < 3.5: #Only increase the speed if it hasn't gone beyond 0.8
                Enemy.enemy_maxSpeed = Enemy.enemy_maxSpeed + 0.2
            Enemy.enemy_SPAWNRATE = Enemy.enemy_SPAWNRATE - 50 #Lowering the spawnrate makes the spawns happen faster (more difficult)
            Score.score_RANGE = Score.score_RANGE + 10 #Increases the score range by 10, increasing difficulty at next 10 score value
            print("Difficulty increased: Rank " + str(gameDifficulty))
            print("Enemy spawnrate: " + str(Enemy.enemy_SPAWNRATE))
            print("Enemy max speed: " + str(Enemy.enemy_maxSpeed))

# Updates the health images in the top-left
def updateHealth():
    if Player.player_HEALTH == 3:
        health_3.setImage(pygame.image.load("Assets/health_visible.png"))
    if Player.player_HEALTH == 2:
        health_2.setImage(pygame.image.load("Assets/health_visible.png"))
        health_3.setImage(pygame.image.load("Assets/health_invisible.png"))
    if Player.player_HEALTH == 1:
        health_2.setImage(pygame.image.load("Assets/health_invisible.png"))

# Spawns buffs
def spawnBuff(x, y):
    buff = Buff.Buff(x, y)
    buff_GROUP.add(buff)

# Check if the player collides with a buff, and applies buff if so
def pickupBuff():
    collision = pygame.sprite.groupcollide(player_GROUP, buff_GROUP, False, True)
    if collision:
        print("Picked up buff")
        for buff_sprite in collision.values(): #This is used to get and return the enemy X and Y values of the collision enemy
            for buff in buff_sprite:
                print(f"Image: ({buff.imagePath})")
                buffType = buff.imagePath #Grabbing the buff image to test what buff to give upon pickup
                Buff.applyBuff(buffType)


def resetGame():
    #Resetting player stats and position
    Player.player_HEALTH = 3
    Player.player_positionX = Player.player_START_positionX
    Player.player_positionY = Player.player_START_positionY
    health_3.setImage(pygame.image.load("Assets/health_visible.png"))
    health_2.setImage(pygame.image.load("Assets/health_visible.png"))

    #Resetting enemy group and values
    enemy_GROUP.empty()
    Enemy.enemy_maxSpeed = Enemy.enemy_maxSpeed_START
    Enemy.enemy_SPAWNRATE = Enemy.enemy_SPAWNRATE_START

    #Restting projectile group
    projectile_GROUP.empty()

    #Resetting game difficulty
    global gameDifficulty
    gameDifficulty = 0

    #Resetting score
    Score.score_CURRENT = 0

    #Resetting menu variables
    Menus.menu_state = "game"
    Menus.paused = "false"

    print("Resetting game...")


# For group drawing
# -- Draws and Updates specified groups in the game
def drawPlayer():
    player_GROUP.draw(WindowControl.WINDOW)
    player_GROUP.update()

def drawHealth():
    health_GROUP.draw(WindowControl.WINDOW)
    health_GROUP.update()

def drawEnemies():
    enemy_GROUP.draw(WindowControl.WINDOW)
    enemy_GROUP.update()

def drawProjectiles():
      #Added this here, since projectile can only exist if player fires them
     projectile_GROUP.draw(WindowControl.WINDOW)
     projectile_GROUP.update()

def drawBuffs():
    buff_GROUP.draw(WindowControl.WINDOW)
    buff_GROUP.update()

# Used to draw all sprites
def drawSprites():
    drawPlayer()
    drawHealth()
    drawEnemies()
    drawProjectiles()
    drawBuffs()

# Used to implement all mechanics in one function
def implementMechanics():
    fireProjectile()
    collideWithMouse()
    killMouse()
    spawnEnemy()
    increaseDifficulty()
    updateHealth()
    pickupBuff()