import pygame

class EndState:
    """ Operates end state of game """

    MENU_KEY_MAP = {"Up": pygame.K_UP,
                    "Down": pygame.K_DOWN,
                    "Select": pygame.K_RETURN,
                    "Back": pygame.K_ESCAPE}

    MAIN_MENU = {" ": 0,
                 "Rewatch game": 1,
                 "Rematch": 2,
                 "Main menu": 3,
                 "Exit": 4}

    def __init__(self, snakes, setup):
        self.snakes = snakes
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.screen_dim = setup["ScreenSize"]

        self.exit = False
        self.rematch = False
        self.intro_menu = False

        self.current_selection = 1
        self.result_msg = "There is no winner..."
        for sn in self.snakes:
            if sn.alive:
                self.result_msg = sn.name + " wins!"

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == self.MENU_KEY_MAP["Up"]:
                    self.current_selection -= 1
                elif event.key == self.MENU_KEY_MAP["Down"]:
                    self.current_selection += 1
                elif event.key == self.MENU_KEY_MAP["Select"]:
                    self._apply_selection()

            self.current_selection -= 1
            self.current_selection %= (len(self.MAIN_MENU)-1)
            self.current_selection += 1

    def render(self, screen):
        # Render main menu on screen
        y = self._render_y_start
        for i, item in enumerate(self.MAIN_MENU):
            if self.current_selection == i:
                c = (255, 255, 255)
            else:
                c = (125, 125, 125)

            if i == 0:
                f = self.font.render(self.result_msg, True, (80, 80, 80))
            else:
                f = self.font.render(item, True, c)
            text_rect = f.get_rect(center=(self.screen_dim[0] / 2, y))
            screen.blit(f, text_rect)
            y += 30

    def _apply_selection(self):
        if self.current_selection == self.MAIN_MENU["Rewatch game"]:
            self._menu_unassigned()
        elif self.current_selection == self.MAIN_MENU["Rematch"]:
            self._play_rematch()
        elif self.current_selection == self.MAIN_MENU["Main menu"]:
            self._main_menu()
        elif self.current_selection == self.MAIN_MENU["Exit"]:
            self._exit_game()

    def _menu_unassigned(self):
        print("Menu not yet made")

    def _play_rematch(self):
        self.rematch = True

    def _main_menu(self):
        self.intro_menu = True

    def _exit_game(self):
        self.exit = True

    @property
    def _render_y_start(self):
        return int(self.screen_dim[1] / 2 - (len(self.MAIN_MENU) / 2) * 30)
