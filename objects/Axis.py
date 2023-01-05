from objects.Point import Point
from pygame import draw
from pygame.gfxdraw import filled_polygon
from data.constants.color import color
from utils.helpers import hex_rgb


class Axis:
    padding = 40

    def __init__(self, system, color):
        self.width, self.height = system.width, system.height
        self.screen = system.screen
        self.color = color

    def draw(self):
        point1, point2 = self._get_points()
        self.draw_line(point1, point2)
        self.draw_arrow(
            point1,
            Point((point1.x + 25, point1.y - 7)),
            Point((point1.x + 25, point1.y + 7)),
        )
        self.draw_arrow(
            point2,
            Point((point2.x - 25, point2.y - 7)),
            Point((point2.x - 25, point2.y + 7)),
        )

    def draw_line(self, point1: Point, point2: Point):
        draw.line(
            self.screen, hex_rgb(self.color), point1.__tuple__(), point2.__tuple__(), 1
        )

    def draw_arrow(self, point1: Point, point2: Point, point3: Point):
        filled_polygon(
            self.screen,
            [point1.__tuple__(), point2.__tuple__(), point3.__tuple__()],
            hex_rgb(self.color),
        )

    def _get_points(self):
        y = self.height // 2
        point1 = Point((self.padding, y))
        point2 = Point((self.width - self.padding, y))
        return (point1, point2)
