from player import Player
from levels import Level

class Builder:
    def __init__(self, level=Level):
        self.level = level()
    
    def build(self, screen, color):
        self.level.draw(screen, color)