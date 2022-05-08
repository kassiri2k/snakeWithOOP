import pygame,sys,random,time
from food import*
from snake import*
from board import*


SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600


GRIDSIZE =20




def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
    surface = pygame.Surface(screen.get_size())
    surface.convert()
    b = Board(SCREEN_WIDTH,SCREEN_HEIGTH,GRIDSIZE)
    b.draw_grid(surface,SCREEN_WIDTH,SCREEN_HEIGTH,GRIDSIZE)

    snake = Snake(SCREEN_WIDTH,SCREEN_HEIGTH)
    food = Food(b,snake)
    
  
    while True:
        clock.tick(10)
        #events
       
       
        

        
        screen.blit(surface,(0,0))
        
        food.draw(surface)
        
        snake.draw(screen)
        print(len(snake.snake_rect_list))
        sys.exit()
        
        
        snake.move_loop()
        
       
        snake.handle_keys()
      
      
        
        
        pygame.display.update()

main()
    