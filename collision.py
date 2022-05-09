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