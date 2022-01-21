import pygame



class Scene:
    def __init__(
        self,
        window,
        clock,
        fps
        ):
        self.window=window
        self.clock=clock
        self.dt=self.clock.tick(fps)
        self.running=False
        self.paused=False
    def start(
        self
        ):
        pass
