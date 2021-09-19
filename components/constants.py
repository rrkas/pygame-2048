import pygame


class Constants:
    def __init__(self):
        # strings
        self.appname = "2048"

        # dimensions
        self.side_cell_count = 5

        self.spacing = 2

        self.margin_top = 80
        self.s_padding = 10
        self.s_size = 400
        self.border_radius = 8

        # colors
        self.bg_color = (0, 0, 0, 128)
        self.number_color = (0, 0, 0)
        self.label_color = (255, 255, 255)
        self.best_score_color = (255, 255, 0)
        self.tile_colors = {
            0: (204, 192, 179),
            2: (238, 228, 219),
            4: (240, 226, 202),
            8: (242, 177, 121),
            16: (236, 141, 85),
            32: (250, 123, 92),
            64: (234, 90, 56),
            128: (237, 207, 114),
            256: (242, 208, 75),
            512: (237, 200, 80),
            1024: (227, 186, 19),
            2048: (236, 196, 2),
            4096: (96, 217, 146),
        }


constants = Constants()
