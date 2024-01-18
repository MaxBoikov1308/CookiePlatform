from player import Player
from levels import Level1

class Builder:
    def __init__(self, level=Level1):
        self.level = level()
    
    def build(self, screen, color):
        self.level.draw(screen, color)