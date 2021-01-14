import pygame


def get_player_keybinding(player_num):
    # Provide key bindings for different players
    if player_num == 0:
        k = {"Down": pygame.K_DOWN,
             "Up": pygame.K_UP,
             "Left": pygame.K_LEFT,
             "Right": pygame.K_RIGHT}
    elif player_num == 1:
        k = {"Down": pygame.K_k,
             "Up": pygame.K_i,
             "Left": pygame.K_j,
             "Right": pygame.K_l}
    elif player_num == 2:
        k = {"Down": pygame.K_c,
             "Up": pygame.K_f,
             "Left": pygame.K_x,
             "Right": pygame.K_v}
    else:
        k = {"Down": pygame.K_s,
             "Up": pygame.K_w,
             "Left": pygame.K_a,
             "Right": pygame.K_d}
    return k
