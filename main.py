import pygame
from snake import Snake


# Globals
SCREEN_DIM = [800, 400]
BLOCK_SIZE = [10, 10]
GAME_FPS = 20


def init_window(screen_dim):
    pygame.init()
    _screen = pygame.display.set_mode(tuple(screen_dim))
    pygame.display.set_caption('tron-snake')

    return _screen


def main():
    screen = init_window(SCREEN_DIM)
    fps_clock = pygame.time.Clock()

    # Game setup
    s1 = Snake("Phillip", (255, 0, 0), [20, 5], BLOCK_SIZE)

    running = True
    while running:
        event_list = pygame.event.get()

        # Check for quit command
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

        s1.update(event_list)

        screen.fill((40, 40, 40))
        s1.render(screen)

        pygame.display.update()
        fps_clock.tick(GAME_FPS)


if __name__ == '__main__':
    main()
