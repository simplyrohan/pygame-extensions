import pygame
import features

class GameSurface:
    def __init__(self, size:tuple, pos:tuple, color:tuple=None, animation:object=None):
        self.size = size
        self.width = size[0]
        self.height = size[1]

        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]

        self.surf = pygame.Surface(self.size)

        self.rect = self.surf.get_rect()
        self.rect.move(self.x, self.y)

        self.color = color
        self.surf.fill(self.color)

        self.animation = animation
        self.animation_frame = 0


    def get_surf(self):
        return self.animation.get_frame(self.animation_frame)


