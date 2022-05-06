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
    global screen 
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
    surface = pygame.Surface(screen.get_size())
    b = Board(SCREEN_WIDTH,SCREEN_HEIGTH,GRIDSIZE)
    b.draw_grid(surface,SCREEN_WIDTH,SCREEN_HEIGTH,GRIDSIZE)

    snake = Snake(SCREEN_WIDTH,SCREEN_HEIGTH)
    food = Food(b,snake)
    
  
    while True:
        clock.tick(10)
        #events
        
        screen.blit(surface,(0,0))

        
        
        food.draw(surface)
      
       
        snake.draw(surface)
        snake.move_loop()
        print(snake.x1,snake.y1)
        snake.handle_keys()

        
        pygame.display.update()

main()
    