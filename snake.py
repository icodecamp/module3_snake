import utils
from collections import deque
import pygame

up = utils.DIRECTIONS.Up
down = utils.DIRECTIONS.Down
left = utils.DIRECTIONS.Left
right = utils.DIRECTIONS.Right

class Snake(object):
    def __init__(self, direction=right, 
            point=(0, 0), color=None):
        self.tailmax = 4
        self.score = 0
        self.direction = direction 
        self.deque = deque()
        self.deque.append(point)
        self.color = color
        self.nextDir = deque()

    def increase_score(self):
        self.tailmax += 2
        self.score += 1
    
    def get_color(self):
        return WHITE
    
    def process_keyboard_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.nextDir.appendleft(up)
                elif event.key == pygame.K_DOWN:
                    self.nextDir.appendleft(down)
                elif event.key == pygame.K_RIGHT:
                    self.nextDir.appendleft(right)
                elif event.key == pygame.K_LEFT:
                    self.nextDir.appendleft(left)

    def move(self):
        if len(self.nextDir) != 0:
            next_dir = self.nextDir.pop()
        else:
            next_dir = self.direction
        head = self.deque.pop()
        self.deque.append(head)
        next_move = head
        if (next_dir == up):
            if self.direction != down:
                next_move =  (head[0] - 1, head[1])
                self.direction = next_dir
            else:
                next_move =  (head[0] + 1, head[1])
        elif (next_dir == down):
            if self.direction != up:
                next_move =  (head[0] + 1, head[1])
                self.direction = next_dir
            else:
                next_move =  (head[0] - 1, head[1])
        elif (next_dir == left):
            if self.direction != right:
                next_move =  (head[0], head[1] - 1)
                self.direction = next_dir
            else:
                next_move =  (head[0], head[1] + 1)
        elif (next_dir == right):
            if self.direction != left:
                next_move =  (head[0], head[1] + 1)
                self.direction = next_dir
            else:
                next_move =  (head[0], head[1] - 1)
        return next_move