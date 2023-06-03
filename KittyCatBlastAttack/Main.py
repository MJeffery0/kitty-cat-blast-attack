import pygame
import WindowControl
import GameMechanics
import Menus
import Score
import Player


#VARIABLES ============================================
# insert variables here if needed


#FUNCTIONS ============================================
def main():
    running = True #Determines running game
    WindowControl.defineFPS()

    while running:
    #START MENU
        while Menus.menu_state == "start":

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN: #Checking if the user clicks their mouse
                    mouse_position = pygame.mouse.get_pos() #Getting the position of the mouse when clicked
                    if Menus.menus_buttonStart.rect.collidepoint(mouse_position) == True: #If the mouse is clicked on the "Start" button...
                        Menus.menu_state = "how to play"
                        print("Game state: " + str(Menus.menu_state))
                    if Menus.menus_buttonQuit_intro.rect.collidepoint(mouse_position) == True: #If the mouse is clicked on the "Quit" button...
                        pygame.quit()

            Menus.startMenu()
            

    #HOW-TO-PLAY MENU
        while Menus.menu_state == "how to play":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN: #Pressing any key will continue to the game
                    Menus.menu_state = "game"
                    print("Game state: " + str(Menus.menu_state))
            
            Menus.howToPlayMenu()


    #GAME MENU
        while Menus.menu_state == "game":

            #PAUSE MENU
            while Menus.paused == "true":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Pressing ESC unpauses the game
                        Menus.paused = "false"
                        print("Paused: " + str(Menus.paused))
                    if event.type == pygame.MOUSEBUTTONDOWN: #Checking for which menu button is clicked
                            mouse_position = pygame.mouse.get_pos() #Getting the mouse position when clicking
                            if Menus.menus_buttonResume.rect.collidepoint(mouse_position) == True:
                                Menus.paused = "false"
                                print("Paused: " + str(Menus.paused))
                            if Menus.menus_buttonQuit_options.rect.collidepoint(mouse_position) == True:
                                pygame.quit()

                Menus.pauseMenu()

            #Runs the game when not paused
            while Menus.paused == "false":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Pressing ESC in-game pauses the game
                        Menus.paused = "true"
                        print("Paused: " + str(Menus.paused))
                
                WindowControl.setBackground(pygame.image.load("Assets/menu_background_light.png"), 0, 0)
                GameMechanics.drawSprites()
                GameMechanics.implementMechanics()
                Score.displayScore()
                pygame.display.update()

                #Checking if the player's health points reach 0. If so, redirect to the "Game Over" menu
                if Player.player_HEALTH == 0:
                    Menus.menu_state = "game over"
                    Menus.paused = "null" #Need to set this to neither true or false, or else the game would keep looking for the paused or unpaused "while" loops
                    Score.setHighScore()
                    print("Game state: " + str(Menus.menu_state))
                    print("Paused: " + str(Menus.paused))


    #GAME OVER MENU
        while Menus.menu_state == "game over":

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN: #Checking if the user is clicked their mouse
                        mouse_position = pygame.mouse.get_pos() #Getting the mouse position
                        if Menus.menus_buttonRetry.rect.collidepoint(mouse_position) == True: #If the mouse is clicked on the "Retry" button...
                            print("Retry!")
                            GameMechanics.resetGame()
                            main() #Replaying the main() method here so the while loop resets from the top. Checks what menu state to play.
                        if Menus.menus_buttonQuit_gameover.rect.collidepoint(mouse_position) == True: #If the mouse is clicked on the "Quit" button...
                            pygame.quit()

            Menus.gameOverMenu()



        
    print("We got here. ... we shouldn't be here.")
    pygame.quit() #Quits the program when the Main "while" (while running:) finishes


# ONLY OPEN FROM MAIN (Keep on bottom) ===================
if __name__ == "__main__":
    main()