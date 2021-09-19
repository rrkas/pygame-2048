import pygame
from pygame.locals import *
from pygame.surface import Surface

from components.constants import constants
from components.models import Py2048


def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return "q"
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    return "u"
                elif event.key == K_RIGHT:
                    return "r"
                elif event.key == K_LEFT:
                    return "l"
                elif event.key == K_DOWN:
                    return "d"
                elif event.key == K_q or event.key == K_ESCAPE:
                    return "q"


def draw_game(surface: Surface, game: Py2048):
    grid = game.grid
    surface.fill(constants.bg_color)

    number_font = pygame.font.SysFont("comicsans", constants.margin_top - 10)
    label = number_font.render(
        f"score: {game.score}",
        True,
        constants.best_score_color if game.best_score else constants.label_color,
    )
    label_rect = label.get_rect(
        center=(
            constants.s_padding + constants.s_size / 2,
            constants.s_padding + constants.margin_top / 2,
        )
    )
    surface.blit(label, label_rect)

    number_font = pygame.font.SysFont("Comic Sans MS", 30)
    for i in range(constants.side_cell_count):
        for j in range(constants.side_cell_count):
            n = grid[i][j]

            rect_x = (
                j * constants.s_size // constants.side_cell_count
                + constants.spacing
                + constants.s_padding
            )
            rect_y = (
                i * constants.s_size // constants.side_cell_count
                + constants.spacing
                + constants.margin_top
                + constants.s_padding
            )
            rect_w = constants.s_size // constants.side_cell_count - constants.spacing
            rect_h = constants.s_size // constants.side_cell_count - constants.spacing

            pygame.draw.rect(
                surface,
                constants.tile_colors[n],
                pygame.Rect(rect_x, rect_y, rect_w, rect_h),
            )
            if n > 0:
                text_surface = number_font.render(f"{n}", True, constants.number_color)
                text_rect = text_surface.get_rect(
                    center=(rect_x + rect_w / 2, rect_y + rect_h / 2)
                )
                surface.blit(text_surface, text_rect)


def get_best_score() -> int:
    try:
        with open("best_score.txt", "r") as f:
            score = f.readline()
            return 0 if len(score) == 0 else int(score)
    except:
        return 0


def save_best_score(score: int) -> bool:
    if get_best_score() < score:
        with open("best_score.txt", "w") as f:
            f.write(str(score))
        return True
    return False
