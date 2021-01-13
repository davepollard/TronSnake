import pygame


class IntroSetup:
    """ Initialise the game parameters """

    MENU_KEY_MAP = {"Up": pygame.K_UP,
                    "Down": pygame.K_DOWN,
                    "Select": pygame.K_RETURN}

    MENU_LIST = {"Main": 0}

    MAIN_MENU = {"Number of Players": 0,
                 "Game setup": 1,
                 "Help": 2,
                 "Begin": 3,
                 "Exit": 4}

    # TODO - add in menu item for "Are you Pooja?"

    def __init__(self, setup):
        self.screen_dim = setup["ScreenSize"]
        self.font = pygame.font.Font('freesansbold.ttf', 24)

        self.current_menu = 0
        self.current_selection = 0
        self.progress = False

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == self.MENU_KEY_MAP["Up"]:
                    self.current_selection -= 1
                elif event.key == self.MENU_KEY_MAP["Down"]:
                    self.current_selection += 1
                elif event.key == self.MENU_KEY_MAP["Select"]:
                    self._apply_selection()

        self.current_selection = self.current_selection % len(self.MAIN_MENU.keys())

    def render(self, screen):
        # Render current menu on screen
        y = int(self.screen_dim[1] / 2 - (len(self.MAIN_MENU.keys()) / 2) * 30)
        for i, item in enumerate(self.MAIN_MENU.keys()):
            if self.current_selection == i:
                c = (255, 255, 255)
            else:
                c = (125, 125, 125)
            f = self.font.render(item, True, c)
            text_rect = f.get_rect(center=(self.screen_dim[0] / 2, y))
            screen.blit(f, text_rect)
            y += 30

    def _apply_selection(self):
        # TODO
        print('boop')
