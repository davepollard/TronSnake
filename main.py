import pygame
from snake import Snake
from intro_setup import IntroSetup
from end_state import EndState


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
    end_state = None

    snakes = []

    running = True
    game_state = 0
    initialisation_count = None

    # --- DEBUG
    game_state = GAME_STATE["Initialising"]
    initialisation_count = 1
    intro_menu.player_status = [1,1,1,1,None]
    # --- DEBUG

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
                intro_menu.start_game = False
                game_state = GAME_STATE["Initialising"]

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

                # Add reference to other trails
                for sn in snakes:
                    temp_lst = snakes.copy()
                    temp_lst.remove(sn)
                    sn.other_snakes = temp_lst

            # render snakes
            for sn in snakes:
                sn.update(event_list, move_snake=False)
                sn.render(screen)

            intro_menu.render_countdown(int(initialisation_count/GAME_SETUP["GameFPS"]), screen)

            initialisation_count -= 1
            if initialisation_count <= 0:
                initialisation_count = None
                game_state = GAME_STATE["Running"]

        elif game_state == GAME_STATE["Running"]:
            # Check for collisions
            for sn in snakes:
                sn.check_snake_collision()

            # Update for next state
            for sn in snakes:
                sn.update(event_list)
                sn.render(screen)

            # Check for state change
            num_alive = 0
            for sn in snakes:
                if sn.alive:
                    num_alive += 1
            if num_alive <= 1:
                game_state = GAME_STATE["End"]

        # Not an elif - possible for single snake to be about to run into wall/snake
        if game_state == GAME_STATE["End"]:
            if end_state is None:
                end_state = EndState(snakes, GAME_SETUP)
            end_state.update(event_list)
            end_state.render(screen)

            if end_state.exit:
                running = False
            elif end_state.rematch:
                for sn in snakes:
                    sn.reset()
                game_state = GAME_STATE["Initialising"]
                end_state = None
            elif end_state.intro_menu:
                game_state = GAME_STATE["Intro"]
                end_state = None

        pygame.display.update()
        fps_clock.tick(GAME_SETUP["GameFPS"])


if __name__ == '__main__':
    main()
