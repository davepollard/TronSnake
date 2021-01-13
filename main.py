import pygame
from snake import Snake
from intro_setup import IntroSetup


# Globals
GAME_SETUP = {"ScreenSize": [800, 400],
              "BlockSize": [10, 10],
              "GameFPS": 15}

GAME_STATE = {"Intro": 0,
              "Running": 1,
              "End": 2}


def init_window(screen_dim):
    pygame.init()
    _screen = pygame.display.set_mode(tuple(screen_dim))
    pygame.display.set_caption('tron-snake')

    return _screen


def main():
    screen = init_window(GAME_SETUP["ScreenSize"])
    fps_clock = pygame.time.Clock()

    # Game setup
    s1 = Snake("Phillip", (255, 0, 0), [20, 5], GAME_SETUP)
    intro_menu = IntroSetup(GAME_SETUP)

    running = True
    game_state = 0

    while running:
        event_list = pygame.event.get()

        # Check for quit command
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

        screen.fill((40, 40, 40))

        if game_state == GAME_STATE["Intro"]:
            intro_menu.update(event_list)
            intro_menu.render(screen)
            if intro_menu.progress:
                game_state = 1

        elif game_state == GAME_STATE["Running"]:
            s1.update(event_list)
            s1.render(screen)

        elif game_state == GAME_STATE["End"]:
            pass

        pygame.display.update()
        fps_clock.tick(GAME_SETUP["GameFPS"])


if __name__ == '__main__':
    main()
