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
        self.ball.rect.x = 350
        self.ball.rect.y = 250
        
        #Group sprites
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        self.all_sprites_list.add(self.ball)
        
        self.running = True # running state of the game
        self.MainLoop() #start main loop
    
    def ProcessInput(self): # Responsible for game event such as input, prog
        for event in pygame.event.get():
            keys = pygame.key.get_pressed() # Get the key currently being pressed
            keys2 = pygame.key.get_pressed() # Get the key currently being pressed
            if event.type == pygame.QUIT: # Did the user exit the game?
                self.running = False
            #Paddle Controls
            else:
                if keys[pygame.K_w]:
                    self.paddleA.moveUp(10)
                if keys[pygame.K_s]:
                    self.paddleA.moveDown(10)
                if keys2[pygame.K_UP]:
                    self.paddleB.moveUp(10)
                if keys2[pygame.K_DOWN]:
                    self.paddleB.moveDown(10)
            
        
    def UpdateGame(self): # Updates game variables/conditions
        # Move the ball every frame according to velocity
        self.ball.rect.x += -self.ball.xVelocity # Move ball on x-axis
        self.ball.rect.y += -self.ball.yVelocity # Move ball on y-axis

        # Wall collisions
        if self.ball.rect.y > self.SCREEN_HEIGHT: # Bottom screen collision
            self.ball.yVelocity *= -1
        if self.ball.rect.y < 0: # Upper screen collision
            self.ball.yVelocity *= -1
        
        # Paddle Collisions
        if self.paddleA.rect.y < self.ball.rect.y and self.paddleA.rect.y + self.paddleA.height > self.ball.rect.y and \
             self.paddleA.rect.x > self.ball.rect.x and self.paddleA.rect.x - self.paddleA.width < self.ball.rect.x:
            self.ball.xVelocity *= -1 # When left paddle collides with ball, shift x direction
        
        if self.paddleB.rect.y < self.ball.rect.y and self.paddleB.rect.y + self.paddleB.height > self.ball.rect.y and \
             self.paddleB.rect.x > self.ball.rect.x and self.paddleB.rect.x - self.paddleB.width < self.ball.rect.x:
            self.ball.xVelocity *= -1 # When left paddle collides with ball, shift x direction

        self.all_sprites_list.update() # Updates all sprites in list
        self.clock.tick(60) # Frame rate control

    def GenerateOutput(self): # Updates the display
        self.screen.fill("BLACK") # Fill the background with black  

        #pygame.draw.circle(self.screen, "YELLOW", (400, 250), 8)
        pygame.draw.line(self.screen, "WHITE", [349, 0], [349, 500], 5)
        self.all_sprites_list.draw(self.screen) # Render sprites in game
        
        pygame.display.flip() # Flip the display
        
    def MainLoop(self): #Runs in game processes in a loop
        while self.running:
            self.ProcessInput()
            self.UpdateGame()
            self.GenerateOutput()
        pygame.quit()

