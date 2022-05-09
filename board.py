import pygame,sys,random,time

class Board(object):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT,GRIDSIZE):
        self.grid=[]
        self.grid_counter=0
        for i in list(range(0,800,20)):
            for j in list(range(0,600,20)):
                self.grid.append((i,j,self.grid_counter))
                self.grid_counter +=1

    def draw_grid(self,surface,SCREEN_WIDTH,SCREEN_HEIGHT,GRIDSIZE):
        
        for i,j,k in self.grid:
           
            if k%2 !=0:
                
                r= pygame.Rect(i,j,GRIDSIZE,GRIDSIZE)
                pygame.draw.rect(surface,(93,216,228),r)
                #pygame.draw.rect(surface,RandColor().color(),r)
               
            else:
              
                rr= pygame.Rect(i,j,GRIDSIZE,GRIDSIZE)
                pygame.draw.rect(surface,(84,196,205),rr)
                #pygame.draw.rect(surface,RandColor().color(),rr)
              


