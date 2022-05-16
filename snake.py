import pygame, sys

pygame.init()


class Snake(object):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGTH):
        self.x1 = SCREEN_WIDTH / 2
        self.y1 = SCREEN_HEIGTH / 2
        self.length = 1
        self.snake_block = 20
        self.change = [0, 0]
        self.snake_rect_list = [
            pygame.Rect(self.x1, self.y1, self.snake_block, self.snake_block)
        ]
        self.snake_list = [(self.snake_rect_list[0].left, self.snake_rect_list[0].top)]
        self.direction = {"left": True, "down": True, "right": True, "up": True}
        self.ret = [pygame.Rect(self.x1, self.y1, self.snake_block, self.snake_block)]
        self.xy = [(self.snake_rect_list[0].left, self.snake_rect_list[0].top)]

    def inc_length(self):
        self.length += 1

    def get_head_positon(self):
        return self.snake_list[0]

    def get_head(self):
        return self.snake_rect_list[0]

        # return True if the snake it in the vertical position and update the position

    def turn_left(self):
        if self.direction["up"] or self.direction["down"]:
            self.direction.update(
                {"left": True, "down": False, "right": False, "up": False}
            )
            self.move_left()

    def turn_down(self):
        if self.direction["right"] or self.direction["left"]:
            self.direction.update(
                {"left": False, "down": True, "right": False, "up": False}
            )
            self.move_down()

    def turn_right(self):
        if self.direction["up"] or self.direction["down"]:
            self.direction.update(
                {"left": False, "down": False, "right": True, "up": False}
            )
            self.move_right()

    def turn_up(self):
        if self.direction["right"] or self.direction["left"]:
            self.direction.update(
                {"left": False, "down": False, "right": False, "up": True}
            )
            self.move_up()

    def move_left(self):
        self.change[0] = -self.snake_block
        self.change[1] = 0

    def move_right(self):
        self.change[0] = self.snake_block
        self.change[1] = 0

    def move_up(self):
        self.change[1] = -self.snake_block
        self.change[0] = 0

    def move_down(self):
        self.change[1] = self.snake_block
        self.change[0] = 0

        # this function makes the snake moving continuously

    def move_loop(self):
        self.x1 += self.change[0]
        self.y1 += self.change[1]
        self.snake_rect_list.append(
            pygame.Rect(self.x1, self.y1, self.snake_block, self.snake_block)
        )
        self.snake_list.append((self.x1, self.y1))

        if (
            len(self.snake_list) > self.length
            or len(self.snake_rect_list) > self.length
        ):
            del self.snake_list[0]
            del self.snake_rect_list[0]

    # this function updates the snake when he eats the food
    def update_snake(self, food, screen):

        self.inc_length()
        r = pygame.Rect(
            food.cube.left, food.cube.top, self.snake_block, self.snake_block
        )
        self.snake_rect_list.append(r)
        self.snake_list.append((r.left, r.top))

        if len(self.snake_list) > self.length:
            del snake_list[0]

    def reset(self):
        self.snake_list.clear()

    def draw(self, screen):

        for rect in self.snake_rect_list:

            pygame.draw.rect(screen, "Blue", rect)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    self.turn_up()
                if event.key == pygame.K_DOWN:
                    self.turn_down()
                if event.key == pygame.K_LEFT:
                    self.turn_left()
                if event.key == pygame.K_RIGHT:
                    self.turn_right()

    def update(self, food):
        r = pygame.Rect(
            food.cube.left, food.cube.top, self.snake_block, self.snake_block
        )
        self.ret.append(r)
        self.xy.append((food.cube.left, food.cube.top))
        self.inc_length()

    def you_lost(self):
        bound = (
            (self.snake_list[0])[0] > SCREEN_WIDTH
            or (self.snake_list[0])[0] > 0
            or (self.snake_list[0])[0] > SCREEN_HEIGTH
            or (self.snake_list[0])[0] < 0
        )
        return bound
