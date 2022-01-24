import pygame
import sys

class App:
    def __init__(
        self,
        title,
        size,
        fps
        ):
        self.window=pygame.display.set_mode(size)
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
        self.window.fill((0,0,0))    
        pygame.display.update()
        self.clock.tick(self.fps)
