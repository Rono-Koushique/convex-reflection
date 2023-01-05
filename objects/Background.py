from data.constants.color import color
from pygame import draw


class Background:
    grid_gap = 50

    def __init__(
        self, system, color=color.white, grid_on=False, grid_color=color.gray_300
    ) -> None:
        self.width = system.width
        self.height = system.height
        self.background_color = color
        self.grid_on = grid_on
        self.screen = system.screen
        self.grid_color = grid_color

    def draw_grid(self):
        start_x = (self.width % self.grid_gap) // 2
        start_y = (self.height % self.grid_gap) // 2
        for i in range(start_y, self.height, self.grid_gap):
            draw.line(self.screen, self.grid_color, (0, i), (self.width, i), 1)
        for i in range(start_x, self.width, self.grid_gap):
            draw.line(self.screen, self.grid_color, (i, 0), (i, self.height), 1)

    def draw(self):
        self.screen.fill(self.background_color)
        if self.grid_on:
            self.draw_grid()
