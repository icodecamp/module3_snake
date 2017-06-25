from collections import deque
import pygame
up = pygame.K_UP
down = pygame.K_DOWN
right = pygame.K_RIGHT
left = pygame.K_LEFT

valid_directions = [up, down, left, right]

class Snake(object):
    def __init__(self):
        self.tailmax = 4
        self.score = 0
        self.current_direction = right
        self.deque = deque()
        self.deque.append((12, 15))

    def increase_score(self):
        self.tailmax += 2
        self.score += 1

    def get_head_location(self):
        location = self.deque.pop()
        self.deque.append(location)
        return location
        
    def get_opposite_direction(self):
        if self.current_direction == left:
            return right
        if self.current_direction == right:
            return left
        if self.current_direction == up:
            return down
        if self.current_direction == down:
            return up

    def move(self, input_direction):
        if input_direction != None:
            if self.get_opposite_direction() != input_direction:
                self.current_direction = input_direction

        location = self.get_head_location()
        move_right = (location[0], location[1] + 1)
        move_left = (location[0], location[1] - 1)
        move_up = (location[0] - 1, location[1])
        move_down = (location[0] + 1, location[1])
        direction =  self.current_direction

        if (direction == up):
            return move_up
        elif (direction == down):
            return move_down
        elif (direction == left):
            return move_left
        else:
            return move_right
