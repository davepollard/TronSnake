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

    def __init__(self, name, colour, start_pos, setup):
        # Initialise snake class
        # Inputs:
        # - id          id assigned to snake
        # - start_pos   start position
        # - setup       game initialisation parameters

        self.name = name
        self.colour = colour
        self.current_pos = start_pos
        self.block = setup["BlockSize"]
        self.trail = [self.current_pos]
        self.map_limits = [int(setup["ScreenSize"][i] / setup["BlockSize"][i]) for i in [0, 1]]

        self.current_movement = self.MOVEMENT["Right"]
        self.alive = True

    def update(self, event_list):
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

        new_pos = [self.trail[-1][0] + self.current_movement[0], self.trail[-1][1] + self.current_movement[1]]
        self.trail.append(new_pos)
        self._check_limits()
        self.alive = not self._trail_collision()

    def render(self, screen):
        # Renders snake onto screen
        for p in self.trail:
            r = (p[0] * self.block[0], p[1] * self.block[1], self.block[0], self.block[1])
            screen.fill(self.colour, r)

    def _check_limits(self):
        if self.trail[-1][0] < 0 or self.trail[-1][0] > self.map_limits[0]:
            self.alive = False
            print("dead x")
        if self.trail[-1][1] < 0 or self.trail[-1][1] > self.map_limits[1]:
            self.alive = False
            print("dead y")

    def _trail_collision(self):
        if self.trail[-1] in self.trail[0:-1]:
            print("own collision")
            return True
        return False
