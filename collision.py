def isTouchingRightWall(self):
    if self.ball.rect.x > self.SCREEN_WIDTH:
        return True
    return False
  
def isTouchingLeftWall(self):
  if self.ball.rect.x < 0:
    return True
  return False

def isTouchingBottomWall(self):
  if self.ball.rect.y > self.SCREEN_HEIGHT:
    return True
  return False

def isTouchingTopWall(self):
    if self.ball.rect.y < 0:
        return True
    return False

def isTouchingLeftPaddle(self):
    if self.paddleA.rect.y < self.ball.rect.y and self.paddleA.rect.y + self.paddleA.height > self.ball.rect.y and \
        self.paddleA.rect.x > self.ball.rect.x and self.paddleA.rect.x - self.paddleA.width < self.ball.rect.x: # Left paddle collision
            return True
    return False

def isTouchingRightPaddle(self):
    if self.paddleB.rect.y < self.ball.rect.y and self.paddleB.rect.y + self.paddleB.height > self.ball.rect.y and \
        self.paddleB.rect.x > self.ball.rect.x and self.paddleB.rect.x - self.paddleB.width < self.ball.rect.x: # Left paddle collision
            return True
    return False