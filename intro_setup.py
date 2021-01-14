import pygame


class IntroSetup:
    """ Initialise the game parameters """

    MENU_KEY_MAP = {"Up": pygame.K_UP,
                    "Down": pygame.K_DOWN,
                    "Select": pygame.K_RETURN,
                    "Back": pygame.K_ESCAPE}

    MENU_LIST = {"Main": 0,
                 "NumPlayers": 1,
                 "Unassigned": 999}

    MAIN_MENU = {"Number of Players": 0,
                 "Game setup": 1,
                 "Help": 2,
                 "Begin": 3,
                 "Exit": 4}

    NUM_PLAYERS = {"Player 1": 0,
                   "Player 2": 1,
                   "Player 3": 2,
                   "Player 4": 3,
                   "Back": 4}

    # TODO - add in menu item for "Are you Pooja?"

    def __init__(self, setup):
        self.screen_dim = setup["ScreenSize"]
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.countdown_font = pygame.font.Font('freesansbold.ttf', 48)

        # Status:
        # - 0   inactive
        # - 1   player
        # - 2   AI
        # - 3   [N/A - only for back button]
        self.player_status = [1, 0, 0, 0, None]
        self.player_colour = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), None]

        self.current_menu = 0
        self.current_selection = 0
        self.start_game = False
        self.exit = False

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == self.MENU_KEY_MAP["Up"]:
                    self.current_selection -= 1
                elif event.key == self.MENU_KEY_MAP["Down"]:
                    self.current_selection += 1
                elif event.key == self.MENU_KEY_MAP["Select"]:
                    self._apply_selection()
                elif event.key == self.MENU_KEY_MAP["Back"]:
                    self._apply_back()
        self.current_selection = self.current_selection % len(self._menu_items)

    def render(self, screen):
        if self.current_menu == self.MENU_LIST["Main"]:
            self._render_regular(screen)
        elif self.current_menu == self.MENU_LIST["NumPlayers"]:
            self._render_players(screen)

    def render_countdown(self, num, screen):
        f = self.countdown_font.render(str(num), True, (100, 100, 100))
        text_rect = f.get_rect(center=(self.screen_dim[0] / 2, self.screen_dim[1]/2))
        screen.blit(f, text_rect)

    def _apply_selection(self):
        if self.current_menu == self.MENU_LIST["Main"]:
            if self.current_selection == self.MAIN_MENU["Number of Players"]:
                self._main_num_players()
            elif self.current_selection == self.MAIN_MENU["Game setup"]:
                self._menu_unassigned()
            elif self.current_selection == self.MAIN_MENU["Help"]:
                self._menu_unassigned()
            elif self.current_selection == self.MAIN_MENU["Begin"]:
                self._begin_game()
            elif self.current_selection == self.MAIN_MENU["Exit"]:
                self._exit_game()

        elif self.current_menu == self.MENU_LIST["NumPlayers"]:
            if self.current_selection == self.NUM_PLAYERS["Back"]:
                self._apply_back()
            else:
                self._change_player_type()

    def _apply_back(self):
        if self.current_menu == self.MENU_LIST["NumPlayers"]:
            self.current_menu = self.MENU_LIST["Main"]
            self.current_selection = 0

    def _menu_unassigned(self):
        print("Menu not yet made")

    # Main menu functions
    def _main_num_players(self):
        self.current_menu = self.MENU_LIST["NumPlayers"]
        self.current_selection = 0

    def _begin_game(self):
        self.start_game = True

    def _exit_game(self):
        self.exit = True

    # Number of player functions
    def _change_player_type(self):
        self.player_status[self.current_selection] += 1
        self.player_status[self.current_selection] %= 3

    def _render_regular(self, screen):
        # Render current menu on screen
        y = self._render_y_start
        for i, item in enumerate(self._menu_items):
            if self.current_selection == i:
                c = (255, 255, 255)
            else:
                c = (125, 125, 125)
            f = self.font.render(item, True, c)
            text_rect = f.get_rect(center=(self.screen_dim[0] / 2, y))
            screen.blit(f, text_rect)
            y += 30

    def _render_players(self, screen):
        y = self._render_y_start

        for i, item in enumerate(self._menu_items):
            if self.current_selection == i:
                c = (255, 255, 255)
            else:
                c = (125, 125, 125)
            if self.player_status[i] == 0:
                msg = ":  Inactive"
            elif self.player_status[i] == 1:
                msg = ":  Player"
            elif self.player_status[i] == 2:
                msg = ":  AI"
            else:
                msg = ""

            f = self.font.render(item+msg, True, c)
            text_rect = f.get_rect(center=(self.screen_dim[0] / 2, y))
            screen.blit(f, text_rect)

            # Add player colour
            if self.player_colour[i] is not None:
                screen.fill(self.player_colour[i], (50, y, text_rect[0]-50-10, 5))
                x = text_rect[0]+text_rect[2]+10
                screen.fill(self.player_colour[i], (x, y, self.screen_dim[0]-x, 5))

            y += 30

    @property
    def snake_parameters(self):
        return list(zip(self.player_status[0:-1], self.player_colour[0:-1]))

    @property
    def _menu_items(self):
        if self.current_menu == self.MENU_LIST["Main"]:
            return list(self.MAIN_MENU.keys())
        elif self.current_menu == self.MENU_LIST["NumPlayers"]:
            return list(self.NUM_PLAYERS.keys())

    @property
    def _render_y_start(self):
        return int(self.screen_dim[1] / 2 - (len(self._menu_items) / 2) * 30)

