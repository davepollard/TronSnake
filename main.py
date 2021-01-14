import pygame
from snake import Snake
from intro_setup import IntroSetup


# Globals
GAME_SETUP = {"ScreenSize": [800, 400],
              "BlockSize": [10, 10],
              "GameFPS": 15}

GAME_STATE = {"Intro": 0,
              "Initialising": 1,
              "Running": 2,
              "End": 3}


def get_snake_start(player_num):
    x, y = [(GAME_SETUP["ScreenSize"][i]/GAME_SETUP["BlockSize"][i])/4 for i in [0, 1]]
    if player_num == 0:
        return [x, y]
    elif player_num == 1:
        return [3*x, y]
    elif player_num == 2:
        return [x, 3*y]
    else:
        return [3*x, 3*y]


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

    snakes = []

    running = True
    game_state = 0
    initialisation_count = None

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

            snakes = []

            if intro_menu.exit:
                running = False

            if intro_menu.start_game:
                game_state = 1

        elif game_state == GAME_STATE["Initialising"]:
            if initialisation_count is None:
                initialisation_count = GAME_SETUP["GameFPS"] * 5

            # Initialise snakes
            if not snakes:
                for i, param in enumerate(intro_menu.snake_parameters):
                    if param[0] == 1:  # Human player
                        snakes.append(Snake("Player %d" % (i+1), param[1], get_snake_start(i), GAME_SETUP))
                    elif param[0] == 2:  # Human player
                        snakes.append(Snake("Player %d" % (i+1), param[1], get_snake_start(i), GAME_SETUP))

            # render snakes
            for sn in snakes:
                sn.render(screen)

            intro_menu.render_countdown(int(initialisation_count/GAME_SETUP["GameFPS"]), screen)

            initialisation_count -= 1
            if initialisation_count <= 0:
                initialisation_count = None
                game_state = GAME_STATE["Running"]

        elif game_state == GAME_STATE["Running"]:
            # Check for collisions


            # Update for next state
            for sn in snakes:
                sn.update(event_list)
                sn.render(screen)

        elif game_state == GAME_STATE["End"]:
            pass

        pygame.display.update()
        fps_clock.tick(GAME_SETUP["GameFPS"])


if __name__ == '__main__':
    main()
