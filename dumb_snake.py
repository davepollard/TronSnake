import pygame
from snake import Snake
from random import random


class DumbSnake(Snake):
    """
    A very dumb snake. Rotates to the left or right whenever player uses input.
    """

    def __init__(self, name, colour, start_pos, setup):
        super(DumbSnake, self).__init__(name, colour, start_pos, setup)
        self.rotation_order = ["Up", "Left", "Down", "Right"]
        if random() > 0.5:
            self.rotation_order = self.rotation_order[::-1]
        self.rotation_idx = 0
        self.has_rotated = False

    def update(self, event_list, move_snake=True):
        # don't update if not alive
        if not self.alive:
            return

        for event in event_list[::-1]:
            if event.type == pygame.KEYDOWN and not self.has_rotated:
                self.rotation_idx += 1
                self.rotation_idx = self.rotation_idx % 4
                self.current_movement = self.MOVEMENT[self.rotation_order[self.rotation_idx]]
                break

        if move_snake:
            self._apply_current_movement()
