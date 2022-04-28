import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height, radius):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width + radius, height + radius])
        self.image.fill("BLACK")
        self.image.set_colorkey("BLACK")
        self.xVelocity = 1
        self.yVelocity = 1

        # Draw the paddle (a rectangle!)
        pygame.draw.circle(self.image, color, [width, height], radius)

        # Fetch the circle object that has the dimensions of the image
        self.rect = self.image.get_rect()