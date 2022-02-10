import pygame
from display import Display
from camera import Camera
from entity import Entity
from scene import Scene
from app import App
from tilemap import TileMap
from controller import Controller

class ExampleGame(Scene):
    def __init__(self, window, clock, dt):
        super().__init__(window, clock, dt)
        
        self.camera=Camera([300,300],[10,10])
        self.player_sprite=pygame.Surface((16,16))
        self.player_sprite.fill((255,0,0))
        self.player=Entity("player",self.player_sprite,self.window.display,100,[0,0],Controller(),1,self.camera)
        self.map=TileMap("res/1.csv",16,self.camera,self.window.display,['1','0'])
        
    def update(self):
        self.window.display.fill((255,255,255))
        
        
        self.map.render()
        self.player.render()
        self.camera.follow(self.player.rect)
        self.player.move()
        self.player.collide(self.map.tiles)
        return super().update()
    
class Game(App):
    def __init__(self, title, size, fps):   
        super().__init__(title, size, fps)
        self.level=ExampleGame(self.window,self.clock, self.dt)
    def start(self):
        self.level.update()
        self.window.show_fps()
        self.window.update()
        return super().start()
    
    

game=Game("Example Game", (800,800),60)

while True:
    game.start()




