import csv 
import pygame
import os
from tile import Tile


class TileMap:
    def __init__(
        self,
        file:str,
        tilesize:int,
        camera:None,
        window:pygame.Surface
        ):
        self.tile_size=tilesize
        self.camera=camera
        self.window=window
        self.tiles=self.load_tiles(file)
    def load_tiles(
        self,
        filename
        ):
        tiles=[]
        map=self.read_file(filename)
        x,y=0,0
        for row in map:
            x=0
            for tile in row:
                if tile=='0':
                    tiles.append(Tile(pygame.Surface((16,16)),"",x*self.tile_size,y*self.tile_size,self.window))
                if tile=='1':
                    tiles.append(Tile(pygame.Surface((16,16)),"",x*self.tile_size,y*self.tile_size,self.window))
                x+=1
            y+=1
        return tiles
    def load_tiles_camera(
        self,
        filename
        ):
        tiles=[]
        map=self.read_file(filename)
        x,y=0,0
        for row in map:
            x=0
            for tile in row:
                if tile=='0':
                    tiles.append(Tile(pygame.Surface((16,16)),"",x*self.tile_size-self.camera.scroll[0],y*self.tile_size-self.camera.scroll[1],self.window))
                if tile=='1':
                    tiles.append(Tile(pygame.Surface((16,16)),"",x*self.tile_size-self.camera.scroll[0],y*self.tile_size-self.camera.scroll[1],self.window))
                x+=1
            y+=1
        return tiles
    def render(
        self
        ):
        for tile in self.tiles:
            tile.draw()
    def read_file(
        self,
        filename
        ):
        map=[]
        with open(os.path.join(filename)) as data:
            data=csv.reader(data,delimiter=",")
            for row in data:
                map.append(list(row))
        return map
            
    
        
        
        
