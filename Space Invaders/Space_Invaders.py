import sys
import pygame

from Settings import Settings
from Ship import Ship

def runGame():
    #initialize pygame, screen and screen object
    pygame.init()
    aiSettings = Settings() #store the settings methods in the aiSettings to access them through this variable
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption(aiSettings.caption)

    #make a ship
    ship = Ship(screen)

    #start the main loop for the game
    while True:
        #Watch for keyboard/mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the screen during each pass through the loop
        screen.fill(aiSettings.bgColor)
        ship.blitme()

        #make the most recently drawn screen visible
        pygame.display.flip()
runGame()
