import pygame 
from paddle import Paddle
from ball import Ball
from random import choice
import collision

class Game:
    def __init__(self):
        # Intialize game variables
        pygame.init()
        pygame.display.set_caption("Pong") # Name window title to Pong
        # Set screen dimensions
        self.SCREEN_WIDTH = 700
        self.SCREEN_HEIGHT = 500
        
        self.MainLoop() # Start main loop
    
    def ProcessInput(self): # Responsible for game event such as input, prog
        for event in pygame.event.get():
            keys = pygame.key.get_pressed() # Get the key currently being pressed
            if event.type == pygame.QUIT: # Did the user exit the game?
                self.isRunning = False
            
    def UpdateGame(self): # Updates game variables/conditions
       pass

    def GenerateOutput(self): # Updates the graphics in the game
        self.all_sprites_list.draw(self.screen) # Render sprites in game
        
        pygame.display.flip() # Flip the display
        
    def MainLoop(self): # Runs in game processes in a loop
        while self.isRunning: # Keep on doing these proccess until the game exits
            self.ProcessInput()
            self.UpdateGame()
            self.GenerateOutput()
        pygame.quit() # Close the game