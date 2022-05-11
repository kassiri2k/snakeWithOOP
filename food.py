import pygame,sys,random,time

class Food(object):
    def __init__(self,board,snake):
        self.foodxy = board.grid #the grid for the game
        self.flag = True   # a flag to break so that we go out of the loop we got the first collision
        self.food_size=20
        
        # coordinates of the food
        self.x1 = (self.foodxy[random.randint(0,len(self.foodxy)-1)])[0]
        self.y1 = (self.foodxy[random.randint(0,len(self.foodxy)-1)])[1]
        #self.r = pygame.Rect(self.x1,self.y1,self.food_size,self.food_size) # the food       
        self.cube = pygame.Rect(self.x1,self.y1,self.food_size,self.food_size) # the food       
        

    #def check_collision(self,snake):
     #   for i in snake.snake_rect_list:
            #if there is a collision snake eats the food
      #      if  self.r.colliderect(i):
       #         self.food_position=self.foodxy[random.randint(0,len(self.foodxy)-1)] # random position
        #        self.r = pygame.Rect(self.food_position[0],self.food_position[1],self.food_size,self.food_size) # the food
         #       break
    #def draw_at_beginning(self,screen,snake):
         #   self.check_collision(snake)
        #    pygame.draw.rect(screen,"Red",self.r)

    def randomize(self):
        self.x1 = (self.foodxy[random.randint(0,len(self.foodxy)-1)])[0]
        self.y1 = (self.foodxy[random.randint(0,len(self.foodxy)-1)])[1]
        

    # draw the food  after check if there is no part of the snake at that position        
    #def draw(self,screen,snake):
     #   self.check_collision(snake)
      #   pygame.draw.rect(screen,"Red",self.r)

    def draw(self,screen,snake):
        self.cube = pygame.Rect(self.x1,self.y1,self.food_size,self.food_size) # the food
        #while self.cube.colliderect(snake.snake_rect_list[0]):
       
    
        #self.randomize()
          #  self.cube = pygame.Rect(self.x1,self.y1,self.food_size,self.food_size) # the food
        pygame.draw.rect(screen,"Red",self.cube)

   
       
        
    
    


