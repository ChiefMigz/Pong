import pygame 
from paddle import Paddle
from ball import Ball
from random import choice

class Game:
    def __init__(self):
        # Intialize game variables
        pygame.init()
        pygame.display.set_caption("Pong") # Name window title to Pong
        # Set screen dimensions
        self.SCREEN_WIDTH = 700
        self.SCREEN_HEIGHT = 500
        # Set display resolution (w x h)
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT]) 
        
        # Initialize clock for game ticks
        self.clock = pygame.time.Clock() 
        
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

        # Left Paddle Score
        self.leftPaddleScore = 0
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.leftPaddleScoreText = self.font.render("Player 1: " + str(self.leftPaddleScore), True, "WHITE", "BLACK")
        self.leftPaddleScoreTextRect = self.leftPaddleScoreText.get_rect()
        self.leftPaddleScoreTextRect.center = (self.SCREEN_WIDTH / 4, 40)

        # Right Paddle Score
        self.rightPaddleScore = 0
        self.rightPaddleScoreText = self.font.render("Player 2: " + str(self.rightPaddleScore), True, "WHITE", "BLACK")
        self.rightPaddleScoreTextRect = self.rightPaddleScoreText.get_rect()
        self.rightPaddleScoreTextRect.center = (self.SCREEN_WIDTH / 1.3, 40)
        
        #Group and add sprites
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        self.all_sprites_list.add(self.ball)
        
        self.isRunning = True # Set isRunning state of the game to True
        self.MainLoop() # Start main loop
    
    def ProcessInput(self): # Responsible for game event such as input, prog
        for event in pygame.event.get():
            keys = pygame.key.get_pressed() # Get the key currently being pressed
            keys2 = pygame.key.get_pressed() # Get the key currently being pressed
            if event.type == pygame.QUIT: # Did the user exit the game?
                self.isRunning = False
            # Take keyboard input to control paddle
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
        # Move the ball every frame in regard to velocity
        self.ball.rect.x += -self.ball.xVelocity # Move ball on x-axis
        self.ball.rect.y += -self.ball.yVelocity # Move ball on y-axis

        # When ball goes out on either left or right side (out of bounds)
        if self.ball.rect.x > self.SCREEN_WIDTH: # When ball went out on right side, left paddle gains score
          # Reset the ball's position by placing the ball on the center of the scene
          self.ball.rect.x = self.SCREEN_WIDTH // 2
          self.ball.rect.y = self.SCREEN_HEIGHT // 2
          # Launch the ball in a random direction (makes it fun)
          self.ball.xVelocity *= choice((-1,1))
          # Increment the left paddle's score by 1
          self.leftPaddleScore += 1
          # Render left paddle score text
          self.leftPaddleScoreText = self.font.render("Player 1: " + str(self.leftPaddleScore), True, "WHITE", "BLACK")
          self.leftPaddleScoreTextRect = self.leftPaddleScoreText.get_rect()
          self.leftPaddleScoreTextRect.center = (self.SCREEN_WIDTH / 4, 40)
    
        if self.ball.rect.x < 0: # When ball went out on left side, right paddle gains score
          # Reset the ball's position by placing the ball on the center of the scene
          self.ball.rect.x = self.SCREEN_WIDTH // 2
          self.ball.rect.y = self.SCREEN_HEIGHT // 2
          # Launch the ball in a random direction (makes it fun)
          self.ball.xVelocity *= choice((-1,1))
          # Increment the right paddle's score by 1
          self.rightPaddleScore += 1
          # Render right paddle score text
          self.rightPaddleScoreText = self.font.render("Player 2: " + str(self.rightPaddleScore), True, "WHITE", "BLACK")
          self.rightPaddleScoreTextRect = self.rightPaddleScoreText.get_rect()
          self.rightPaddleScoreTextRect.center = (self.SCREEN_WIDTH / 1.3, 40)
        
        # Wall collisions
        if self.ball.rect.y > self.SCREEN_HEIGHT: # Bottom screen collision
            self.ball.yVelocity *= -1 # Shift vertical direction

        if self.ball.rect.y < 0: # Upper screen collision
            self.ball.yVelocity *= -1 # Shift vertical direction
        
        # When ball hits one of the paddles
        if self.paddleA.rect.y < self.ball.rect.y and self.paddleA.rect.y + self.paddleA.height > self.ball.rect.y and \
             self.paddleA.rect.x > self.ball.rect.x and self.paddleA.rect.x - self.paddleA.width < self.ball.rect.x: # Left paddle collision
            self.ball.xVelocity *= -1 # When left paddle collides with ball, shift x direction
            self.ball.yVelocity *= choice((-1,1))

        if self.paddleB.rect.y < self.ball.rect.y and self.paddleB.rect.y + self.paddleB.height > self.ball.rect.y and \
             self.paddleB.rect.x > self.ball.rect.x and self.paddleB.rect.x - self.paddleB.width < self.ball.rect.x: # Right paddle collision
            self.ball.xVelocity *= -1 # When left paddle collides with ball, shift x direction
            self.ball.yVelocity *= choice((-1,1))
        self.all_sprites_list.update() # Updates all sprites in list
        self.clock.tick(60) # Frame rate control

    def GenerateOutput(self): # Updates the graphics in the game
        self.screen.fill("BLACK") # Fill the background with black 
        # Render paddle score texts
        self.screen.blit(self.leftPaddleScoreText, self.leftPaddleScoreTextRect) # Render left paddle score
        self.screen.blit(self.rightPaddleScoreText, self.rightPaddleScoreTextRect) # Render right paddle score

        pygame.draw.line(self.screen, "WHITE", [349, 0], [349, 500], 5) # Draw the line that divides the two paddles
        self.all_sprites_list.draw(self.screen) # Render sprites in game
        
        pygame.display.flip() # Flip the display
        
    def MainLoop(self): #Runs in game processes in a loop
        while self.isRunning:
            self.ProcessInput()
            self.UpdateGame()
            self.GenerateOutput()
        pygame.quit()