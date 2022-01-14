import pygame


class Controller:
    def __init__(
        self
        )->None:
        self.moving_right=False
        self.moving_left=False
        self.moving_down=False
        self.moving_up=False
    def movement(
        self
        )->None:
        position=[0,0]
        if self.moving_right==True:
            position[0]=4
        if self.moving_left==True:
            position[0]=-4
        if self.moving_down==True:
            position[1]=4
        if self.moving_up==True:
            position[1]=-4
        return position
    def stop(
        self
        ):
        pass