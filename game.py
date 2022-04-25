from paddle import Paddle
from ball import Ball
import pygame 

class Game:
    def __init__(self):
        # Intialize game variables
        pygame.init()
        pygame.display.set_caption("Pong", "Pong") # Name window title to Pong
        self.SCREEN_WIDTH = 700
        self.SCREEN_HEIGHT = 500
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT]) # Set display resolution (w x h)
        self.clock = pygame.time.Clock()

        #paddle dimension
        #self.paddle
        
        #Left Paddle
        self.paddleA = Paddle("WHITE", 10, 100)
        self.paddleA.rect.x = 20
        self.paddleA.rect.y = 200
        
        #Right Paddle
        self.paddleB = Paddle("WHITE", 10, 100)
        self.paddleB.rect.x = 670
        self.paddleB.rect.y = 200

        # Ball
        self.ball = Ball("YELLOW", 8, 8, 8)
        self.ball.rect.x = 400
        self.ball.rect.y = 250
        
        #Group sprites
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        self.all_sprites_list.add(self.ball)
        
        self.running = True # running state of the game
    
    def ProcessInput(self): # Responsible for game events
        for event in pygame.event.get():
            keys = pygame.key.get_pressed() # Get the key currently being pressed
            keys2 = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                self.running = False
            #Paddle Controls
            else:
                if keys[pygame.K_w]:
                    self.paddleA.moveUp(5)
                if keys[pygame.K_s]:
                    self.paddleA.moveDown(5)
                if keys2[pygame.K_UP]:
                    self.paddleB.moveUp(5)
                if keys2[pygame.K_DOWN]:
                    self.paddleB.moveDown(5)
            
        
    def UpdateGame(self): # Updates game variables/conditions
        #if (self.paddleA.rect.x > )
        self.all_sprites_list.update()
        self.clock.tick(60)

    def GenerateOutput(self): # Updates the display
        self.screen.fill("BLACK") # Fill the background with black  

        #pygame.draw.circle(self.screen, "YELLOW", (400, 250), 8)
        pygame.draw.line(self.screen, "WHITE", [349, 0], [349, 500], 5)
        self.all_sprites_list.draw(self.screen)
        
        # Flip the display
        pygame.display.flip()
        
    def MainLoop(self): #Runs in game processes in a loop
        while self.running:
            self.ProcessInput()
            self.UpdateGame()
            self.GenerateOutput()
        pygame.quit()

