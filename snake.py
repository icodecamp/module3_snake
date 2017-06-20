from collections import deque


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
        
    def move(self, input_direction):
        location = self.get_head_location()
        return (location[0], location[1] + 1)
        # TODO: Check to see if input_direction is valid
        # TODO: If input_direction is right, new location that is 1 block right 
        # TODO: If input_direction is left, new location that is 1 block left 
        # TODO: If input_direction is up, new location that is 1 block up 
        # TODO: If input_direction is down, new location that is 1 block down 
