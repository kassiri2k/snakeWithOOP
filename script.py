import pygame,sys,random,time


class Snake(object):
    def __init__(self):
        self.x1=SCREEN_WIDTH/2
        self.y1=SCREEN_HEIGTH/2
        self.length =1
        self.snake_list =[]
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
        if len(self.snake_list)> self.length:
            del snake_list[0]

    def reset(self):
        pass
    def draw(self,surface):
        for block in self.snake_list:
            r = pygame.Rect(block[0],block[1],snake_block,snake_block)
            pygame.draw.rect(surface,(93,216,228),r,1)
    def handle_keys(self):
        for event in pygame.event.get():
            if pygame.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.type == pygame.KEYDOWN:
                if pygame.type == pygame.K_UP:
                    self.move_up()
                if pygame.type == pygame.K_DOWN:
                    self.move_down()
                if pygame.type == pygame.K_LEFT:
                    self.move_left()
                if pygame.type == pygame.K_RIGHT:
                    self.move_left()


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
                    r
                    break
    def draw(self,surface):
        r = pygame.Rect(self.food_position[0],self.food_position[1],self.food_size,self.food_size)
        pygame.draw.rect(surface,"Red",r)

class Board(object):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT,GRIDSIZE):
        self.grid=[]
        self.grid_counter=0
        for i in list(range(0,800,20)):
            for j in list(range(0,600,20)):
                self.grid.append((i,j,self.grid_counter))
                self.grid_counter +=1
    
    def draw_grid(self,surface):
        for i,j,k in self.grid:
           
            if k%2 !=0:
                
                r= pygame.Rect(i,j,GRIDSIZE,GRIDSIZE)
                pygame.draw.rect(surface,(93,216,228),r)
                #pygame.draw.rect(surface,RandColor().color(),r)
            else:
              
                rr= pygame.Rect(i,j,GRIDSIZE,GRIDSIZE)
                pygame.draw.rect(surface,(84,196,205),rr)
                #pygame.draw.rect(surface,RandColor().color(),rr)




SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600


GRIDSIZE =20





def main():
    pygame.init()
    clock = pygame.time.Clock()
    global screen 
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
    surface = pygame.Surface(screen.get_size())
    b = Board(SCREEN_WIDTH,SCREEN_HEIGTH,GRIDSIZE)
    b.draw_grid(surface)

    snake = Snake()
    food = Food(b,snake)

    while True:
        clock.tick(10)
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
        screen.blit(surface,(0,0))
        food.draw(surface)
        
        pygame.display.update()

main()
    