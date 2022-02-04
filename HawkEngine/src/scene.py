import pygame

class Scene:
    def __init__(
        self,
        window,
        clock,
        dt
        ):
        self.window=window
        self.clock=clock
        self.dt=dt
        self.running=False
        self.paused=False
    def pause(
        self
        )->bool:
        self.paused=True
        return self.paused
    def update(
        self
        ):
        """Update function"""
        if not self.pause:
            self.update()
        
