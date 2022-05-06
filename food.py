import pygame,sys,random,time

class Food(object):
    def __init__(self,board,snake):
        self.foodxy = board.grid
        self.flag = True
        self.food_size=20
        
        self.food_position=(0,0)
    def randomize_position(self,snake):
        while self.flag:
            self.food_position= self.foodxy[random.randint(0,len(self.foodxy)-1)]
            for i in snake.snake_list:
                if self.food_position[0] != i[0] and self.food_position[1]!=i[1]:
                    self.flag =False
                    break
    def draw(self,surface):
        r = pygame.Rect(self.food_position[0],self.food_position[1],self.food_size,self.food_size)
        pygame.draw.rect(surface,"Red",r)


