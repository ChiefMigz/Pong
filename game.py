from paddle import Paddle
import pygame 

class Game:
    def __init__(self):
        # Intialize game variables
        pygame.init()
        pygame.display.set_caption("Pong", "Pong") # Name window title to Pong
        self.screen = pygame.display.set_mode([700, 500]) # Set display resolution (w x h)
        self.clock = pygame.time.Clock()
        
        #Left Paddle
        self.paddleA = Paddle("WHITE", 10, 100)
        self.paddleA.rect.x = 20
        self.paddleA.rect.y = 200
        
        #Right Paddle
        self.paddleB = Paddle("WHITE", 10, 100)
        self.paddleB.rect.x = 670
        self.paddleB.rect.y = 200
        
        #Group sprites
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        
        self.running = True # running state of the game
    
    def ProcessInput(self): # Responsible for game events
        for event in pygame.event.get():
            keys = pygame.key.get_pressed() # Get the key currently being pressed
            if event.type == pygame.QUIT:
                self.running = False
            #Paddle Controls
            if keys[pygame.K_w]:
                self.paddleA.moveUp(5)
            if keys[pygame.K_s]:
                self.paddleA.moveDown(5)
            if keys[pygame.K_UP]:
                self.paddleB.moveUp(5)
            if keys[pygame.K_DOWN]:
                self.paddleB.moveDown(5)
            
        
    def UpdateGame(self): # Updates game variables/conditions
        self.all_sprites_list.update()
        self.clock.tick(60)

    def GenerateOutput(self): # Updates the display
        self.screen.fill("BLACK") # Fill the background with black  

        pygame.draw.circle(self.screen, "YELLOW", (400, 250), 8)
        pygame.draw.line(self.screen, "WHITE", [349, 0], [349, 500], 5)
        self.all_sprites_list.draw(self.screen)
        
        # Flip the display
        pygame.display.flip()
        
    def RunLoop(self): #Runs in game processes in a loop
        while self.running:
            self.ProcessInput()
            self.UpdateGame()
            self.GenerateOutput()
        pygame.quit()

