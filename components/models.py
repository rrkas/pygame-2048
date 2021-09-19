import random

import numpy as np

from .constants import constants


class Py2048:
    def __init__(self):
        self.grid = np.zeros(
            (constants.side_cell_count, constants.side_cell_count), dtype=int
        )
        self.score = 0
        self.best_score = False

    def new_number(self, k=1):
        free_pos = list(zip(*np.where(self.grid == 0)))
        for pos in random.sample(free_pos, k=k):
            if random.random() < 0.1:
                self.grid[pos] = 4
            else:
                self.grid[pos] = 2

    def _get_nums(self, grid):
        from .methods import save_best_score

        this_n = grid[grid != 0]
        this_n_sum = []
        skip = False
        for j in range(len(this_n)):
            if skip:
                skip = False
                continue
            if j != len(this_n) - 1 and this_n[j] == this_n[j + 1]:
                new_n = this_n[j] * 2
                self.score += new_n
                self.best_score = save_best_score(self.score)
                skip = True
            else:
                new_n = this_n[j]
            this_n_sum.append(new_n)

        return np.array(this_n_sum)

    def move(self, move):
        for i in range(constants.side_cell_count):
            if move in "lr":
                this = self.grid[i, :]
            elif move in "ud":
                this = self.grid[:, i]
            else:
                this = None

            flipped = False
            if move in "rd":
                flipped = True
                this = this[::-1]

            this_n = self._get_nums(this)
            new_this = np.zeros_like(this)
            new_this[: len(this_n)] = this_n

            if flipped:
                new_this = new_this[::-1]

            if move in "lr":
                self.grid[i, :] = new_this
            elif move in "ud":
                self.grid[:, i] = new_this

    def play(self):
        self.new_number(2)
        while True:
            print(self.grid)
            cmd = input()
            if cmd == "q":
                break
            elif cmd in "lrud":
                old_grid = self.grid.copy()
                self.move(cmd)
                if all((old_grid == self.grid).flatten()):
                    continue
                self.new_number()

    def __str__(self):
        return str(self.grid)
