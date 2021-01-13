import pygame


class Snake:
    """ Operate a generic snake """

    KEY_MAP = {"Down": pygame.K_DOWN,
               "Up": pygame.K_UP,
               "Left": pygame.K_LEFT,
               "Right": pygame.K_RIGHT}

    MOVEMENT = {"Up": [0, -1],
                     "Down": [0, 1],
                     "Left": [-1, 0],
                     "Right": [1, 0]}

    def __init__(self, name, colour, start_pos, block):
        # Initialise snake class
        # Inputs:
        # - id          id assigned to snake
        # - start_pos   start position
        # - block       block size [x, y]

        self.name = name
        self.colour = colour
        self.current_pos = start_pos
        self.block = block
        self.trail = [self.current_pos]

        self.current_movement = self.MOVEMENT["Right"]

    def update(self, event_list):
        # Update movement
        # Inputs:
        # - event_key   event key list
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == self.KEY_MAP["Up"] and self.current_movement != self.MOVEMENT["Down"]:
                    self.current_movement = self.MOVEMENT["Up"]
                elif event.key == self.KEY_MAP["Down"] and self.current_movement != self.MOVEMENT["Up"]:
                    self.current_movement = self.MOVEMENT["Down"]
                elif event.key == self.KEY_MAP["Left"] and self.current_movement != self.MOVEMENT["Right"]:
                    self.current_movement = self.MOVEMENT["Left"]
                elif event.key == self.KEY_MAP["Right"] and self.current_movement != self.MOVEMENT["Left"]:
                    self.current_movement = self.MOVEMENT["Right"]

        new_pos = [self.trail[-1][0] + self.current_movement[0], self.trail[-1][1] + self.current_movement[1]]
        self.trail.append(new_pos)


    def render(self, screen):
        # Renders snake onto screen
        for p in self.trail:
            r = (p[0] * self.block[0], p[1] * self.block[1], self.block[0], self.block[1])
            screen.fill(self.colour, r)
