import pygame

class Display:
    def __init__(
        self,
        screen_size,
        display_size,
        title=""
        ):
        self.screen_size=screen_size
        self.display_size=display_size
        self.window=pygame.display.set_mode(self.screen_size)
        self.display=pygame.Surface(self.display_size)
        self.title=pygame.display.set_caption(title)
        self.offset=[0,0]
    def update(
        self
        ):
        self.window.blit(pygame.transform.scale(self.display,self.screen_size),self.offset)
    def set_title(
        self,
        title
        ):
        self.title=pygame.display.set_caption(title)
    def show_fps(
        self,
        clock
        ):
        fps=clock.get_fps()
        self.title=pygame.display.set_caption(str(int(fps)))
    def get_title(
        self
        ):
        return str(self.title)
    def get_size(
        self
        ):
        return self.screen_size
    
