import pygame
import sys
from display import Display

class App:
    def __init__(
        self,
        title,
        size,
        fps
        ):
        self.window=Display((800,800),(600,600))
        self.clock=pygame.time.Clock()
        self.fps=fps
        self.title=pygame.display.set_caption(title)
    def quit(
        self
        ):
        sys.exit()
    def start(
        self
        ):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        self.window.display.fill((0,0,0))    
        pygame.display.update()
        self.window.update()
        self.clock.tick(self.fps)
