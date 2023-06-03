import pygame
import WindowControl
import Button
import Score

#VARIABLES =======================================
# General-use
pygame.font.init()
key_pressed = pygame.key.get_pressed()
menu_state = "start" #Used to declare the which menu game is on


# START menu
menus_startBackground = pygame.image.load("Assets/menu_start.png")
menus_buttonStart = Button.Button(pygame.image.load("Assets/button_play.png"), WindowControl.window_WIDTH/2, 320)
menus_buttonQuit_intro = Button.Button(pygame.image.load("Assets/button_quit.png"), WindowControl.window_WIDTH/2, 410)

menus_start_GROUP = pygame.sprite.Group() #Used to draw the button sprites
menus_start_GROUP.add(menus_buttonStart)
menus_start_GROUP.add(menus_buttonQuit_intro)


# HOW TO PLAY menu
menus_howtoplayBackground = pygame.image.load("Assets/menu_howtoplay.png")


# PAUSE menu
paused = "false" #Used globally to determine the in-game's paused state (swaps between true/false/null)
menus_optionsBackground = pygame.image.load("Assets/menu_background_normal.png")
menus_buttonResume = Button.Button(pygame.image.load("Assets/button_resume.png"), WindowControl.window_WIDTH/2, WindowControl.window_HEIGHT/2 - 50)
menus_buttonQuit_options = Button.Button(pygame.image.load("Assets/button_quit.png"), WindowControl.window_WIDTH/2, WindowControl.window_HEIGHT/2 + 50)

menus_options_GROUP = pygame.sprite.Group()
menus_options_GROUP.add(menus_buttonResume)
menus_options_GROUP.add(menus_buttonQuit_options)


# GAME OVER menu
menus_gameoverBackground = pygame.image.load("Assets/menu_gameover.png")
menus_buttonRetry = Button.Button(pygame.image.load("Assets/button_retry.png"), 270, 430)
menus_buttonQuit_gameover = Button.Button(pygame.image.load("Assets/button_quit.png"), WindowControl.window_WIDTH - 270, 430)

menus_gameover_GROUP = pygame.sprite.Group()
menus_gameover_GROUP.add(menus_buttonRetry)
menus_gameover_GROUP.add(menus_buttonQuit_gameover)




#FUNCTIONS =======================================
# START menu
def startMenu():
    WindowControl.setBackground(menus_startBackground, 0, 0)
    menus_start_GROUP.draw(WindowControl.WINDOW)
    menus_start_GROUP.update()
    pygame.display.update()


# HOW TO PLAY menu
def howToPlayMenu():
     WindowControl.setBackground(menus_howtoplayBackground, 0, 0)
     pygame.display.update()


# PAUSE menu
def pauseMenu():
    WindowControl.setBackground(menus_optionsBackground, 0, 0)
    menus_options_GROUP.draw(WindowControl.WINDOW)
    menus_options_GROUP.update()
    pygame.display.update()

# GAME OVER menu
def gameOverMenu():
    WindowControl.setBackground(menus_gameoverBackground, 0, 0)
    Score.displayFinalScore()
    menus_gameover_GROUP.draw(WindowControl.WINDOW)
    menus_gameover_GROUP.update()
    pygame.display.update()