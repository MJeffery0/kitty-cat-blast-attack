import pygame

#VARIABLES ============================================
# Window Settings
pygame.display.set_caption("Kitty Cat Blast Attack!") #Sets the name of the window
window_WIDTH, window_HEIGHT = 900, 500
BACKGROUND = (232, 190, 142)
FPS = 60
WINDOW = pygame.display.set_mode((window_WIDTH, window_HEIGHT))
clock = pygame.time.Clock()

#FUNCTIONS ============================================
# General functions
def defineFPS():
    clock.tick(FPS)

# Setters
# -- This is used to fill the background with a solid RBG colour
def fillBackground(background):
    WINDOW.fill(background)

# -- This is used to fill the background with an image background (use 0,0 coordinates unless states otherwise)
def setBackground(background, x, y):
    WINDOW.blit(background, (x, y))

def setWidth(self, width):
    self.window_WIDTH = width

def setHeight(self, height):
    self.window_HEIGHT = height