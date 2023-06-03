import pygame
import WindowControl
import os.path

#VARIABLES =======================================
# Scoreboard scores ---------
score_CURRENT = 0
score_HIGH = 0
score_RANGE = 10

# Reset value
score_RANGE_START = 10 #Score range used to determine game difficulty

# Text values
pygame.font.init()

score_font = pygame.font.SysFont("verdana", 50, bold=True) #Font style for in-game score
score_font_endTitle = pygame.font.SysFont("verdana", 32, bold=True) #Font style for post-game titles ("score", "highscore")
score_font_endScore = pygame.font.SysFont("verdana", 28) #Font style for post-game scores

# Highscore file namesake
score_file = "highscore.txt"



#FUNCTIONS ======================================
# Increases the score
def addScore():
    global score_CURRENT
    score_CURRENT = score_CURRENT + 1
    print("Current Score: " + str(score_CURRENT))

# Replace new highest score
def setHighScore():
    global score_CURRENT
    global score_HIGH

    #Grabbing a previous highscore, if it exists
    if os.path.isfile(score_file):
        with open(score_file, "r") as checkHighscore:
            for line in checkHighscore: #Reading each line (should only be one line though)
                score_HIGH = int(line) #Sets the current high score as the text file integer value

    #If the newest score is higher than the file's high score, set and overwrite the high score value
    if score_CURRENT > score_HIGH:
        score_HIGH = score_CURRENT

        with open(score_file, "w") as highscoreFile:
            highscoreFile.write(str(score_HIGH))

        print("New High Score: " + str(score_HIGH))

# Displays score while playing the game
def displayScore():
    scoreText = score_font.render(str(score_CURRENT), 40, (0,0,0))
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.right = (WindowControl.window_WIDTH - 20)
    WindowControl.WINDOW.blit(scoreText, scoreTextRect)

def displayFinalScore():
    #Getting titles (Score, Highscore)
    # -- Prints "SCORE:" on game over screen
    scoreText = score_font_endTitle.render("Score: ", 32, (0,0,0))
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (WindowControl.window_WIDTH/2-50, WindowControl.window_HEIGHT/2+80)

    # -- Prints "HIGHSCORE:" on gameover screen
    scoreTextHigh = score_font_endTitle.render("Highscore: ", 32, (0,0,0))
    scoreTextHighRect = scoreTextHigh.get_rect()
    scoreTextHighRect.right = scoreTextRect.right
    scoreTextHighRect.top = scoreTextRect.bottom

    #Getting scores (Current, High)
    # -- Print the final player score on game over screen
    scoreText_score = score_font_endScore.render(str(score_CURRENT), 28, (0,0,0))
    scoreText_scoreRect = scoreText_score.get_rect()
    scoreText_scoreRect.left = scoreTextRect.right
    scoreText_scoreRect.bottom = scoreTextRect.bottom

    # -- Print the high score on game over screen
    scoreText_highscore = score_font_endScore.render(str(score_HIGH), 28, (0,0,0))
    scoreText_highscoreRect = scoreText_highscore.get_rect()
    scoreText_highscoreRect.left = scoreTextHighRect.right
    scoreText_highscoreRect.bottom = scoreTextHighRect.bottom

    #Draws all text
    WindowControl.WINDOW.blit(scoreText, scoreTextRect)
    WindowControl.WINDOW.blit(scoreTextHigh, scoreTextHighRect)
    WindowControl.WINDOW.blit(scoreText_score, scoreText_scoreRect)
    WindowControl.WINDOW.blit(scoreText_highscore, scoreText_highscoreRect)
