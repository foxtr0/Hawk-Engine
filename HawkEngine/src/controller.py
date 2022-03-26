import pygame


class Controller:
    def __init__(
        self
        )->None:
        self.moving_right=False
        self.moving_left=False
        self.moving_down=False
        self.moving_up=False
        self.pressed_right=False
        self.pressed_left=False
        self.pressed_down=False
        self.pressed_up=False
        self.position=pygame.math.Vector2(0,0)
    def movement(
        self
        )->None:
        if self.moving_right==True:
           self.position.x=4
        else:
            self.position.x=0
        if self.moving_left==True:
            self.position.x=-4
        if self.moving_down==True:
            self.position.y=4
        else:
            self.position.y=0
        if self.moving_up==True:
            self.position.y=-4
        return self.position
    def friction(
        self
        ):
        self.moving_right=False
        self.moving_left=False
        self.moving_down=False
        self.moving_up=False
