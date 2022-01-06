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

    def __init__(self, name, colour, start_pos, setup, key_map=None):
        # Initialise snake class
        # Inputs:
        # - id          id assigned to snake
        # - colour      --
        # - start_pos   start position
        # - setup       game initialisation parameters

        self.name = name
        self.colour = colour

        if key_map is not None:
            self.KEY_MAP = key_map

        self.block = setup["BlockSize"]
        self.initial_pos = start_pos
        self.trail = [start_pos]
        self.map_limits = [int(setup["ScreenSize"][i] / setup["BlockSize"][i]) for i in [0, 1]]

        self.current_movement = self.MOVEMENT["Right"]
        self.alive = True

        # Loaded with other snakes in the game
        self.other_snakes = []

    def check_snake_collision(self):
        # Collision with another snake?
        for sn in self.other_snakes:
            if self.trail[-1] in sn.trail:
                self.alive = False

    def update(self, event_list, move_snake=True):
        # Update movement
        # Inputs:
        # - event_key   event key list

        # Skip update if not alive
        if not self.alive:
            return

        direction_changed = False
        for event in event_list[::-1]:
            if event.type == pygame.KEYDOWN:
                if event.key == self.KEY_MAP["Up"] and self.current_movement != self.MOVEMENT["Down"]:
                    self.current_movement = self.MOVEMENT["Up"]
                    direction_changed = True
                elif event.key == self.KEY_MAP["Down"] and self.current_movement != self.MOVEMENT["Up"]:
                    self.current_movement = self.MOVEMENT["Down"]
                    direction_changed = True
                elif event.key == self.KEY_MAP["Left"] and self.current_movement != self.MOVEMENT["Right"]:
                    self.current_movement = self.MOVEMENT["Left"]
                    direction_changed = True
                elif event.key == self.KEY_MAP["Right"] and self.current_movement != self.MOVEMENT["Left"]:
                    self.current_movement = self.MOVEMENT["Right"]
                    direction_changed = True
                # Only take most recent direction command
                if direction_changed:
                    break

        if move_snake:
            self._apply_current_movement()

    def render(self, screen):
        # Renders snake onto screen
        # Inputs
        # - screen          Surface to render snake on
        for p in self.trail:
            r = (p[0] * self.block[0], p[1] * self.block[1], self.block[0], self.block[1])
            screen.fill(self.colour, r)

    def reset(self):
        # Reset the snake keeping the same parameters
        self.trail = [self.initial_pos]
        self.alive = True

    def _apply_current_movement(self):
        # Add new position
        new_pos = [self.trail[-1][0] + self.current_movement[0], self.trail[-1][1] + self.current_movement[1]]
        self.trail.append(new_pos)
        self._check_limits()
        if self._trail_collision():
            self.alive = False

    def _check_limits(self):
        # Within map area
        if self.trail[-1][0] < 0 or self.trail[-1][0] > self.map_limits[0]:
            self.alive = False
        if self.trail[-1][1] < 0 or self.trail[-1][1] > self.map_limits[1]:
            self.alive = False

    def _trail_collision(self):
        # self collision?
        if self.trail[-1] in self.trail[0:-1]:
            return True
        return False
