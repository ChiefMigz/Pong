from paddle import Paddle
import pygame 

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong", "Pong")
        self.screen = pygame.display.set_mode([700, 500]) #set display resolution
        self.clock = pygame.time.Clock()
        
        self.paddleA = Paddle("WHITE", 10, 100)
        self.paddleA.rect.x = 20
        self.paddleA.rect.y = 200
        
        self.paddleB = Paddle("WHITE", 10, 100)
        self.paddleB.rect.x = 670
        self.paddleB.rect.y = 200
        
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        
        self.running = True
        
    def ProcessInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
    def UpdateGame(self):
        self.all_sprites_list.update()
        self.clock.tick(60)

    def GenerateOutput(self):
         # Fill the background with white   
        self.screen.fill("BLACK")

        pygame.draw.circle(self.screen, "YELLOW", (400, 250), 8)
        pygame.draw.line(self.screen, "WHITE", [349, 0], [349, 500], 5)
        self.all_sprites_list.draw(self.screen)
        
        # Flip the display
        pygame.display.flip()
        
    
    def RunLoop(self):
        while self.running:
            self.ProcessInput()
            self.UpdateGame()
            self.GenerateOutput()
        pygame.quit()

