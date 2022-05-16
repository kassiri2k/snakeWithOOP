import pygame, sys, random, time


class Food(object):
    def __init__(self, board, snake):
        self.foodxy = board.grid  # the grid for the game
        self.flag = True  # a flag to break so that we go out of the loop we got the first collision
        self.food_size = 20

        # coordinates of the food
        self.x1 = (self.foodxy[random.randint(0, len(self.foodxy) - 1)])[0]
        self.y1 = (self.foodxy[random.randint(0, len(self.foodxy) - 1)])[1]
        self.cube = pygame.Rect(
            self.x1, self.y1, self.food_size, self.food_size
        )  # the food

    def randomize(self):
        self.x1 = (self.foodxy[random.randint(0, len(self.foodxy) - 1)])[0]
        self.y1 = (self.foodxy[random.randint(0, len(self.foodxy) - 1)])[1]

    def draw(self, screen, snake):
        self.cube = pygame.Rect(self.x1, self.y1, self.food_size, self.food_size)
        pygame.draw.rect(screen, "Red", self.cube)
