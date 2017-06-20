from collections import deque
import random
import pygame
from snake import Snake
import utils

SNAKE_SPEED = 3

def initialize_game():
    clock = pygame.time.Clock()
    board = utils.get_board()
    snake = Snake()
    board[0][0] = 1
    food = utils.generate_food(board)
    return clock, board, snake, food

def end_game(game, score):
    if utils.play_again(game, score):
        return run(game)
    else:             
        return "done"

def run(game): 
    clock, board, snake, food = initialize_game()
    while True:
        clock.tick(5*SNAKE_SPEED)

        ##### Look for keyboard events! #########
        new_direction = None
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
                return "done"
            if event.type == pygame.KEYDOWN:
                new_direction = event.key

        ## Move snake
        next_head = snake.move(new_direction)

        if (utils.is_wall(board, next_head)):
            return end_game(game, snake.score)

        if utils.is_food(board, next_head):
            snake.increase_score()
            food = utils.generate_food(board)

        snake.deque.append(next_head)

        if len(snake.deque) > snake.tailmax:
            snake.deque.popleft()
        game.fill(utils.BLACK) 
        board = utils.update_board(game, [snake], food)
        pygame.display.update()

def main():
    game = utils.initialize_board()
    if utils.start_screen(game):
        run(game)
    pygame.quit()

if __name__ == "__main__":
    main()
