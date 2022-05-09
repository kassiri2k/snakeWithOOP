import pygame,sys,random,time

class Food(object):
    def __init__(self,board,snake):
        self.foodxy = board.grid #the grid for the game
        self.flag = True   # a flag to break so that we go out of the loop we got the first collision
        self.food_size=20
        
        self.food_position=None #self.foodxy[random.randint(0,len(self.foodxy)-1)] # random position
        self.r =None# pygame.Rect(self.food_position[0],self.food_position[1],self.food_size,self.food_size) # the food

    # draw the food  after check if there is no part of the snake at that position        
    def draw(self,screen,snake):
        while self.flag:
            self.food_position= self.foodxy[random.randint(0,len(self.foodxy)-1)]
            self.r = pygame.Rect(self.food_position[0],self.food_position[1],self.food_size,self.food_size)
            for i in snake.snake_rect_list:
                #if self.food_position[0] != i[0] and self.food_position[1]!=i[1]:
                # if there is no collision then we keep our coordinates
                if not self.r.colliderect(i) :
                    self.flag =False
                    print("here")
                    break
        pygame.draw.rect(screen,"Red",self.r)
       
        self.flag =True
    
    


