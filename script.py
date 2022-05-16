import pygame, sys, random, time
from food import *
from snake import *
from board import *


SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600


GRIDSIZE = 20


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    surface = pygame.Surface(screen.get_size())
    surface.convert()
    b = Board(SCREEN_WIDTH, SCREEN_HEIGTH, GRIDSIZE)
    b.draw_grid(surface, SCREEN_WIDTH, SCREEN_HEIGTH, GRIDSIZE)

    snake = Snake(SCREEN_WIDTH, SCREEN_HEIGTH)
    food = Food(b, snake)
    start = True

    while True:
        clock.tick(10)
        #events

        screen.blit(surface, (0, 0))

        snake.move_loop()
        snake.draw(screen)
        food.draw(screen, snake)
        if food.cube.colliderect(snake.snake_rect_list[-1]):

            food.randomize()
            food.draw(screen, snake)
            snake.update(food)

        snake.handle_keys()

        pygame.display.update()


main()
