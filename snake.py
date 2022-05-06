import pygame,sys

pygame.init()
class Snake(object):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGTH):
        self.x1=SCREEN_WIDTH/2
        self.y1=SCREEN_HEIGTH/2
        self.length =1
        self.snake_list =[(self.x1,self.y1)]
        self.direction ={"left":False,"down":False,"right":False,"up":False}
        self.snake_block = 20
        self.change = [0,0]
    def get_head_positon(self):
        return snake_list[0]
        # return True if the snake it in the vertical position and update the position
    def turn_left(self):
        if self.direction["up"] or self.direction["down"]:
            self.direction.update({"left":True,"down":False,"right":False,"up":False})
            self.move_left()
    def turn_down(self):
        if self.direction["right"] or self.direction["left"]:
            self.direction.update({"left":False,"down":True,"right":False,"up":False})
            self.move_down()
    def turn_right(self):
        if self.direction["up"] or self.direction["down"]:
            self.direction.update({"left":False,"down":False,"right":True,"up":False})
            self.move_right()
    def turn_up(self):
        if self.direction["right"] or self.direction["right"]:
            self.direction.update({"left":False,"down":False,"right":False,"up":True})
            self.move_up()
            
    def move_left(self):
        self.change[0] = -self.snake_block
        self.change[1] =0
    def move_right(self):
        self.change[0] = +self.snake_block
        self.change[1] =0
    def move_up(self):
        self.change[1] = -self.snake_block
        self.change[0] =0
    def move_down(self):
        self.change[1] = +self.snake_block
        self.change[0] =0
    def move_loop(self):
        self.x1 +=self.change[0]
        self.y1 +=self.change[1]

    
    def update_snake(self):
        self.snake_list.append((self.x1,self.y1))
       # if len(self.snake_list)> self.length:
    #        del snake_list[0]

    def reset(self):
        pass
    def draw(self,surface):
        for block in self.snake_list:
            
            r = pygame.Rect(block[0],block[1],self.snake_block,self.snake_block)
            pygame.draw.rect(surface,"Black",r)
            
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                 
                    self.move_up()
                   

                if event.key== pygame.K_DOWN:
                    self.move_down()
                if event.key== pygame.K_LEFT:
                    self.move_left()
                if event.key== pygame.K_RIGHT:
                    self.move_right()





              

