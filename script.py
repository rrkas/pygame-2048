import pygame

pygame.font.init()

from components.methods import *
from components.models import Py2048


def main():
    pygame.init()
    pygame.display.set_caption(constants.appname)

    s_width = constants.s_size + 2 * constants.s_padding
    s_height = constants.s_size + 2 * constants.s_padding + constants.margin_top

    surface = pygame.display.set_mode((s_width, s_height))
    game = Py2048()
    game.new_number(2)

    running = True
    while running:
        draw_game(surface, game)
        pygame.display.update()
        key = wait_for_key()
        if key == "q":
            running = False
        elif key in "lrud":
            old_grid = game.grid.copy()
            game.move(key)
            if all((game.grid != 0).flatten()):
                break
            if all((game.grid == old_grid).flatten()):
                continue
            game.new_number()

    pygame.display.quit()


if __name__ == "__main__":
    main()
