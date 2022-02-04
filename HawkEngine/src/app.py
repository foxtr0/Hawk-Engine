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
        self.window=Display(size,(600,600),title)
        self.clock=pygame.time.Clock()
        self.fps=fps
        self.dt=None
    def quit(
        self
        ):
        sys.exit()
    def start(
        self
        ):
        self.dt=self.clock.tick(self.fps)/1000
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.quit()
        self.window.display.fill((0,0,0))    
        pygame.display.update()
        self.window.update()
